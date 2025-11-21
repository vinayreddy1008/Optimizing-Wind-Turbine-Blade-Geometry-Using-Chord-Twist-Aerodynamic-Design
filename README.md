# 🌬️ Wind Turbine Blade Optimization (Chord–Twist Design)

This project performs a simplified but realistic optimization of a wind turbine blade by tuning the **chord** and **twist** distributions along the blade radius. The goal is to **maximize Annual Energy Production (AEP)** using:

- A **Blade Element Momentum (BEM)** aerodynamic model  
- Real **S826 airfoil polar data**  
- A **Weibull wind-speed distribution**  
- A **constrained nonlinear optimizer (SLSQP)**

This work represents one focused sub-problem of full wind turbine design and is inspired by the MIT blade optimization study (reference included).

---

## 📁 Contents of This Repository

```
├── Wind-Turbine-Blade-Optimization-Report.pdf   → Full project report
├── wind_blade_optimization.ipynb                → Jupyter/Kaggle notebook (code)
└── Wind Turbine Blade Design Optimization.pdf   → MIT OCW project used as inspiration
```

---

## 🚀 How to Use

### **Run the Jupyter Notebook**
1. Open `wind_blade_optimization.ipynb`.
2. Run all cells from top to bottom.  
3. The notebook will:
   - Load S826 airfoil polar data (embedded in code)
   - Run the iterative BEM aerodynamic solver
   - Compute AEP over a Weibull wind distribution
   - Optimize chord & twist using SLSQP
   - Compare baseline vs optimized AEP

No external dataset is needed — everything is included inside the notebook.

---

## 📊 Summary of the Work

- Blade divided into **8 sections**
- 16 design variables (chord + twist)
- Bounds + smoothness penalties keep blade realistic
- BEM solver computes performance at different wind speeds
- Optimization improves AEP compared to baseline geometry

All explanations, equations, diagrams, and complete code are provided in the PDF report.

---

## 📎 Reference

This project is conceptually inspired by the wind turbine optimization project from MIT OpenCourseWare.  
The reference PDF (`Wind Turbine Blade Design Optimization.pdf`) is included in the repository.

---

## 👤 Author

**Vinay Reddy Y**  
BT2024174  
Team: **QWERT**
