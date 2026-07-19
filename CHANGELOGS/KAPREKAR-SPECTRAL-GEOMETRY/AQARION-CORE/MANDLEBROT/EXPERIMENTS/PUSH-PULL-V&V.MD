Push/Pull V&V - Mandelbrot ID-TAG
Pull Verification
Question: Does the observation preserve behavior?
Test:

same pixel class        |        vsame future class?
If yes: DΠ=0DΠ​=0, exact quotient.
Mandelbrot expected: No. Boundary pixels contain both escaping and bounded points that share same coarse observation but diverge.
Metric: ϵ(r)=∣DΠ∣/∣X∣ϵ(r)=∣DΠ​∣/∣X∣ for resolution rr.
As r→∞r→∞, ϵ(r)ϵ(r) should decay slowly due to fractal boundary, not exponentially.
Push Verification
Question: If we reconstruct hidden states from observation, where does error appear?
Measure: DΠ(n)=(I−Π)KnΠDΠ(n)​=(I−Π)KnΠ
Experiment:
n=1,2,10,100
Track leakage horizon
For Kaprekar: leakage horizon = H (max height) then 0, exact closure.
For Mandelbrot: leakage persists for all n, scale-dependent >0, defect-dominated.
Research Value
Anchor systems:
Kaprekar: finite exact, D=0
Random map: finite chaotic, usually D>0, low compression
Mandelbrot: infinite-limit approximation, scale-dependent D>0
This supports: Finite observation induces measurable dynamical leakage.
