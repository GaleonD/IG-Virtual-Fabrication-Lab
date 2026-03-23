# 🔬 **VLSI Virtual FabLab: Process Predictive Dashboard**<br>
A multi-module Python application built with Streamlit to simulate and visualize core semiconductor manufacturing processes. This project focuses on physical modeling for bridging the gap between theoretical VLSI equations and real-world fab results.
<br><br>
## **Project Overview**<br>
Originally developed as a Thermal Oxidation validator against the BYU Cleanroom "Gold Standard," this tool evolved into a comprehensive suite covering the three fundamental pillars of the IC fabrication cycle: Additive, Modificative, and Subtractive processes.
<br><br>
**Thermal Oxidation (Additive)**<br>
**Physics:** Implements the Deal-Grove Model with Arrhenius temperature dependence for linear ($B/A$) and parabolic ($B$) growth.<br>
**Validation:** Calibrated to match BYU benchmarks (e.g., 71.1 nm at $1000^\circ\text{C}$ for 60 min, Dry $O_2$).<br>
**Visualization:** Maps oxide thickness to a dynamic Thin-Film Interference color profile (Tan/Brown, Purple, Blue, etc.).
<br><br>
**Ion Implantation (Modificative)**<br>
**Physics:** Models dopant concentration using a Gaussian Distribution based on LSS Theory.<br>
**Parameters:** Supports Boron, Phosphorus, and Arsenic species with variable Energy (keV) and Dose ($atoms/cm^2$).<br>
**Visualization:** Features a Semi-Logarithmic Profile ($Log(C)$ vs. Depth) to accurately identify electrical junction depths ($x_j$).
<br><br>
**Etch Rate & Selectivity (Subtractive)**<br>
**Physics:** Simulates material removal for $SiO_2$ and $Si_3N_4$ using various chemistries like Buffered HF, KOH, and Plasma RIE.<br>
**Metrics:** Calculates Selectivity (S) ratios and provides critical feedback on Substrate Loss during over-etching.<br>
**Visualization:** A real-time cross-sectional "stack" view showing the physical thinning of layers.
<br><br>
## Roadmap & Future Development<br>
**Photolithography Module (In Development)**<br><br>
The final pillar of the "Virtual Fab" is currently being engineered. This module will move the dashboard into the Optical Domain, including the implementation of the Rayleigh Criterion ($R = k_1 \frac{\lambda}{NA}$) to determine minimum feature sizes, calculating process windows ($DOF = k_2 \frac{\lambda}{NA^2}$) for different light sources (I-line, KrF, ArF), and a dynamic "Reticle-to-Wafer" scaling visualization to show how wavelength affects chip density.
<br><br>
**Quality of Life (QoL) & UI Enhancements**<br><br>
To make the "Virtual Fab" more comprehensive and reactive, the following upgrades are on the way:<br><br>
**Interactive Cross-Sections:** Real-time animations in the Etch Lab that respond instantly to slider movements for a "live etch" feel.<br>
**Process Chaining:** A feature to pass the output of one tab (e.g., Oxide Thickness) as the starting input for the next (e.g., Etch Target).<br>
**Advanced Error Handling:** "Safety Guardrails" that trigger visual warnings if process parameters (like Temperature or Dose) exceed physically realistic bounds.<br>
**Exportable Fab Reports:** A one-click "Download CSV/PDF" button to save simulation results and plots for academic lab reports.
<br><br>
## **🛠️ Tech Stack**<br>
Language: Python 3.10+.<br>
Framework: Streamlit (Web UI).<br>
Math/Stats: NumPy, SciPy.<br>
Visualization: Matplotlib.<br>
Other Tools: BYU Cleanroom Process Calculator(s), Google Gemini AI.
