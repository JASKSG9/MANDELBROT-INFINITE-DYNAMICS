{
  "system": "Mandelbrot_grid",
  "origin_id": "OG-AQARION-MANDELBROT-001",
  "samples": 640000,
  "projection_defect": {
    "D_pi_estimate": 11,
    "status": "MEASURED",
    "scale_dependence": [
      {
        "resolution": 50,
        "samples": 2500,
        "defect": 10,
        "defect_ratio": 0.004,
        "collision_examples": [
          {
            "obs": [
              "ESCAPE",
              0
            ],
            "future_branching": 2
          },
          {
            "obs": [
              "BOUND",
              100
            ],
            "future_branching": 7
          },
          {
            "obs": [
              "ESCAPE",
              4
            ],
            "future_branching": 4
          }
        ]
      },
      {
        "resolution": 100,
        "samples": 10000,
        "defect": 10,
        "defect_ratio": 0.001,
        "collision_examples": [
          {
            "obs": [
              "ESCAPE",
              0
            ],
            "future_branching": 2
          },
          {
            "obs": [
              "BOUND",
              100
            ],
            "future_branching": 10
          },
          {
            "obs": [
              "ESCAPE",
              1
            ],
            "future_branching": 5
          }
        ]
      },
      {
        "resolution": 200,
        "samples": 40000,
        "defect": 11,
        "defect_ratio": 0.000275,
        "collision_examples": [
          {
            "obs": [
              "ESCAPE",
              0
            ],
            "future_branching": 2
          },
          {
            "obs": [
              "BOUND",
              100
            ],
            "future_branching": 11
          },
          {
            "obs": [
              "ESCAPE",
              1
            ],
            "future_branching": 6
          }
        ]
      },
      {
        "resolution": 400,
        "samples": 160000,
        "defect": 11,
        "defect_ratio": 6.875e-05,
        "collision_examples": [
          {
            "obs": [
              "ESCAPE",
              0
            ],
            "future_branching": 2
          },
          {
            "obs": [
              "BOUND",
              100
            ],
            "future_branching": 11
          },
          {
            "obs": [
              "ESCAPE",
              1
            ],
            "future_branching": 10
          }
        ]
      },
      {
        "resolution": 800,
        "samples": 640000,
        "defect": 11,
        "defect_ratio": 1.71875e-05,
        "collision_examples": [
          {
            "obs": [
              "ESCAPE",
              0
            ],
            "future_branching": 2
          },
          {
            "obs": [
              "BOUND",
              100
            ],
            "future_branching": 11
          },
          {
            "obs": [
              "ESCAPE",
              1
            ],
            "future_branching": 11
          }
        ]
      }
    ],
    "epsilon_r": [
      {
        "resolution": 50,
        "epsilon": 0.004
      },
      {
        "resolution": 100,
        "epsilon": 0.001
      },
      {
        "resolution": 200,
        "epsilon": 0.000275
      },
      {
        "resolution": 400,
        "epsilon": 6.875e-05
      },
      {
        "resolution": 800,
        "epsilon": 1.71875e-05
      }
    ]
  },
  "push_pull_VV": {
    "pull_verification": "Does observation preserve behavior? Test same pixel class -> same future class",
    "push_verification": "If reconstruct hidden states from observation, where does error appear?",
    "leakage_horizon": [
      {
        "n": 1,
        "defect": 11,
        "defect_ratio": 0.000275
      },
      {
        "n": 2,
        "defect": 11,
        "defect_ratio": 0.000275
      },
      {
        "n": 10,
        "defect": 11,
        "defect_ratio": 0.000275
      },
      {
        "n": 100,
        "defect": 11,
        "defect_ratio": 0.000275
      }
    ]
  },
  "interpretation": {
    "expected": "D_Pi != 0, FINITE_APPROXIMATION, NONZERO_OBSERVATION_DEFECT, BOUNDARY_COMPLEXITY",
    "meaning": "Observation partition is not dynamically closed"
  },
  "verification": {
    "type": "computational",
    "status": "PASS"
  }
}
