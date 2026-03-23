#🔬 **VLSI Virtual FabLab: Process Predictive Dashboard**#<br>
A multi-module Python application built with Streamlit to simulate and visualize core semiconductor manufacturing processes. This project focuses on high-fidelity physical modeling, bridging the gap between theoretical VLSI equations and real-world fab results.
<br><br>
##**Project Overview**##<br>
Originally developed as a Thermal Oxidation validator against the BYU Cleanroom "Gold Standard," this tool has evolved into a comprehensive suite covering the three fundamental pillars of the IC fabrication cycle: Additive, Modificative, and Subtractive processes.
<br><br>
**1. Thermal Oxidation (Additive)**<br>
Physics: Implements the Deal-Grove Model with Arrhenius temperature dependence for linear ($B/A$) and parabolic ($B$) growth.<br>
Validation: Calibrated to match BYU benchmarks (e.g., 71.1 nm at $1000^\circ\text{C}$ for 60 min, Dry $O_2$).<br>
Visualization: Maps oxide thickness to a dynamic Thin-Film Interference color profile (Tan/Brown, Purple, Blue, etc.).<br>
<br><br>
**2. Ion Implantation (Modificative)**<br>
Physics: Models dopant concentration using a Gaussian Distribution based on LSS Theory.<br>
Parameters: Supports Boron, Phosphorus, and Arsenic species with variable Energy (keV) and Dose ($atoms/cm^2$).<br>
Visualization: Features a Semi-Logarithmic Profile ($Log(C)$ vs. Depth) to accurately identify electrical junction depths ($x_j$).<br>
<br><br>
**3. Etch Rate & Selectivity (Subtractive)**<br>
Physics: Simulates material removal for $SiO_2$ and $Si_3N_4$ using various chemistries like Buffered HF, KOH, and Plasma RIE.<br>
Metrics: Calculates Selectivity (S) ratios and provides critical feedback on Substrate Loss during over-etching.<br>
Visualization: A real-time cross-sectional "stack" view showing the physical thinning of layers.<br>
<br><br>
##**🛠️ Tech Stack**##<br>
Language: Python 3.10+.<br>
Framework: Streamlit (Web UI).<br>
Math/Stats: NumPy, SciPy.<br>
Visualization: Matplotlib.<br>
Other Tools: BYU Cleanroom Process Calculator(s), Google Gemini AI.
