
#!/usr/bin/env python3
"""
AQARION STRUCTURAL FINGERPRINT (ASF) Encoder - Minimal Universal Engine
Implements height convention fix and structural passport.
"""
import math
from collections import Counter, defaultdict, deque

class ASFEncoder:
    def __init__(self, T, name="UNKNOWN"):
        self.T = T
        self.name = name
        self.states = list(T.keys()) if isinstance(T, dict) else list(range(len(T)))
        self.N = len(self.states)

    def _find_cycles_and_height(self):
        # Handle both dict and list T
        if isinstance(self.T, dict):
            T = self.T
            def get_next(x): return T.get(x, x)
        else:
            Tlist = self.T
            def get_next(x): return Tlist[x] if 0 <= x < len(Tlist) else x

        visited = {}
        height = {}
        cycles = []
        root = {}

        for start in self.states:
            if start in visited:
                continue
            path = []
            pos = {}
            cur = start
            while cur not in visited:
                visited[cur] = 0  # temporary
                pos[cur] = len(path)
                path.append(cur)
                cur = get_next(cur)
                if cur not in self.states and not isinstance(self.T, list):
                    # sink outside
                    break
            # Check if cur in pos => cycle
            if cur in pos:
                cyc = path[pos[cur]:]
                cycles.append(cyc)
                for node in cyc:
                    height[node] = 0
                    root[node] = node
            # back-propagate
            for node in reversed(path):
                if node in height:
                    continue
                nxt = get_next(node)
                if nxt in height:
                    height[node] = height[nxt] + 1
                    root[node] = root.get(nxt, nxt)
            for node in path:
                visited[node] = 1

        # Any remaining without height (isolated) -> 0
        for s in self.states:
            if s not in height:
                height[s] = 0
                root[s] = s

        return height, cycles, root

    def encode(self):
        height, cycles, root = self._find_cycles_and_height()
        N = self.N
        levels = Counter(height.values())
        # quotient = distinct (height, root)
        quotient = len(set((h, root.get(x, x)) for x, h in height.items()))
        max_h = max(height.values()) if height else 0

        # branching entropies
        def h_layer():
            vals = [math.log(n)/t for t, n in levels.items() if t>0 and n>0]
            return max(vals) if vals else 0.0
        def beta():
            max_h_local = max_h
            b = {}
            for t in range(1, max_h_local+1):
                b[t] = sum(1 for h in height.values() if 0 < h <= t)
            return b
        beta_dict = beta()
        h_branch_finite = max([math.log(b)/t for t,b in beta_dict.items() if b>0], default=0.0)

        return {
            "ASF_version": "1.0",
            "identity": {"system": self.name, "origin": "OG-AQARION-001", "state_type": "finite" if isinstance(self.T, dict) or isinstance(self.T, list) else "infinite_approx"},
            "space": {"size": N, "finite": True},
            "dynamics": {
                "map_type": "functional_graph",
                "cycles": {"count": len(cycles), "sizes": [len(c) for c in cycles]},
                "height": {"value": max_h, "convention": "distance_to_cycle", "cycle_nodes": {"included": False, "height": 0}, "indexing": "zero_based"}
            },
            "geometry": {
                "levels": dict(sorted(levels.items())),
                "inverse_branching": {"max_indegree": "computed via census engine", "beta": beta_dict}
            },
            "compression": {"quotient_size": quotient, "ratio": quotient/N if N else 0},
            "closure": {"observable": "(height, root)", "D_pi": "ZERO" if quotient==N else "NONZERO", "status": "EXACT" if quotient==N else "APPROXIMATE"},
            "branching": {
                "layer_entropy": h_layer(),
                "finite_beta_entropy": h_branch_finite,
                "asymptotic_branch_entropy": 0
            },
            "classification": self.classify(N, quotient, max_h, len(cycles))
        }

    def classify(self, N, Q, H, num_cycles=1):
        result=[]
        if N>0: result.append("FINITE")
        result.append("FUNCTIONAL_GRAPH")
        if H==0: result.append("PURE_PERIODIC")
        if H<10: result.append("LOW_DEPTH")
        else: result.append("HIGH_DEPTH")
        if Q/N <0.01: result.append("HIGH_COMPRESSION")
        elif Q/N <0.1: result.append("MEDIUM_COMPRESSION")
        else: result.append("LOW_COMPRESSION")
        if Q<N: result.append("QUOTIENT_STRUCTURE")
        if Q==N: result.append("EXACT_QUOTIENT")
        else: result.append("APPROXIMATE_QUOTIENT")
        if H>0 and Q/N<0.01: result.append("TREE_LIKE")
        if num_cycles==1 and H>0: result.append("SINGLE_BASIN")
        return result

if __name__=="__main__":
    # Example Kaprekar D4
    def kaprekar_map(x):
        s=f"{x:04d}"
        return int("".join(sorted(s, reverse=True))) - int("".join(sorted(s)))
    T={n: kaprekar_map(n) for n in range(10000)}
    enc=ASFEncoder(T, "Kaprekar_D4")
    import json
    print(json.dumps(enc.encode(), indent=2))
