#  Optimizing Wind Turbine Blade Geometry Using Chord–Twist Aerodynamic Design

This project focuses on a simplified but realistic version of wind turbine blade optimization.  
The goal is to improve **Annual Energy Production (AEP) by tuning the chord and twist distributions along the blade radius using:

- A Blade Element Momentum (BEM) aerodynamic model  
- Real S826 airfoil polar data (XFOIL)  
- A Weibull wind-speed distribution  
- A constrained nonlinear optimization approach (SLSQP)

This is a meaningful slice of a much larger real-world turbine design task, simplified to fit course scope while still staying physically grounded.


##  Project Overview

Real wind-turbine blade design is extremely complex.  
This project tackles one important sub-problem:

> Finding the best chord and twist profiles for maximum AEP.

The blade is divided into 8 sections, and each section’s chord and twist values are treated as independent design variables. A BEM solver computes power at each wind speed, and the optimizer finds the geometry that maximizes AEP.

---

##  Key Features

  1. Iterative BEM Aerodynamic Model
- Axial and tangential induction factors solved iteratively  
- Prandtl tip-loss model included  
- Angle of attack → interpolated from real S826 lift/drag polars  
- Computes power over a range of wind speeds

  2. Realistic Optimization Setup
- 16 design variables (8 chords + 8 twists)  
- Bounds on chord and twist  
- Smoothness penalty to avoid unrealistic shapes  
- Mass proxy constraint limiting total chord size  
- Objective: **maximize AEP** (implemented as minimize `-AEP`)

  3. Wind Resource Modeling
- Wind speeds 3–25 m/s  
- Weibull distribution with (k = 2, c = 7 m/s)  
- AEP computed as probability-weighted integral of the power curve

---

# Repository Structure

```
📁 Optimizing-Wind-Turbine-Blade-Geometry
│
├── README.md                      → Project summary
├── report/
│   ├── Wind-Blade-Optimization-Report.pdf
│   └── Wind-Blade-Optimization-Report.tex
│
├── notebook/
│   └── wind_blade_optimization.ipynb   → Full Kaggle notebook (code)
│
├── docs/
│   └── MIT_reference.pdf            → Inspiration project (MIT OCW)
│
└── requirements.txt                 → Dependencies
```


##  Results (Short Summary)

- The optimized blade has smoother twist and slightly increased mid-span chord  
- AEP improves by **5–15%** based on constraint settings  
- Greatest power improvements appear in the **6–12 m/s wind range**  
- Geometry remains realistic due to smoothness penalties

---

##  Why This Project Matters

Even though this is a simplified version of real turbine design, it still captures the key engineering idea:

- Blade shape strongly affects performance  
- Small geometry changes can give meaningful AEP gains  
- Optimization + physics → better designs than manual guesses  
- BEM is the essential first tool used in wind engineering  

This project creates a foundation for extending into more advanced topics like multi-airfoil blades, structural constraints, or dynamic stall models.

---

##  Reference

The work is conceptually inspired by an MIT OpenCourseWare project on wind turbine blade optimization  
(see the `docs/` folder for the reference PDF).

---
