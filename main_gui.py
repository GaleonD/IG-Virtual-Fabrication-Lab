import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from thox_phymodel import thickness_computation
from thox_colmodel import oxide_color
from ioimp_phymodel import doping_profile

st.set_page_config(page_title="IG's Virtual FabLab", layout="wide")

st.title("VLSI Process Predictive Dashboard")
st.caption("Developed by Indrajith (and AI)")
st.markdown("---")

tab1, tab2 = st.tabs(["Thermal Oxidation", "Ion Implantation"])

with tab1:
    st.header("Thermal Oxidation Lab")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        temp_c = st.slider("Temperature (°C)", 700, 1200, 1000, key="ox_temp")
        crystal = st.selectbox("Crystal Orientation", ["(100) Silicon", "(111) Silicon"])
    with col2:
        t_min = st.number_input("Oxidation Time (min)", 1, 1440, 60, key="ox_time")
        mode = st.radio("Environment", ["Dry O2", "Wet H2O"], index=0)
    with col3:
        pressure = st.slider("Process Pressure (atm)", 0.1, 15.0, 1.0, key="ox_pres")

    res_col1, res_col2 = st.columns([1, 2])
    
    with res_col1:
        thickness = thickness_computation(temp_c, t_min, pressure, mode.lower()[:3])
        color_hex = oxide_color(thickness)
        st.metric("Oxide Thickness ($x_o$)", f"{thickness:.2f} nm")
        
        st.markdown(f"""
            <div style="background-color:{color_hex}; width:100%; height:100px; border-radius:10px; 
            border:2px solid #444; display:flex; align-items:center; justify-content:center; 
            color:white; font-weight:bold; text-shadow: 1px 1px 2px #000;">
                {color_hex.upper()}
            </div>""", unsafe_allow_html=True)
        st.caption("Estimated Visual Color")

    with res_col2:
        times = np.linspace(1, max(t_min * 1.5, 200), 100)
        thick_vals = [thickness_computation(temp_c, t, pressure, mode.lower()[:3]) for t in times]
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(times, thick_vals, label="Growth Curve", color="#1f77b4")
        ax.scatter([t_min], [thickness], color="red")
        ax.set_xlabel("Time (min)")
        ax.set_ylabel("Thickness (nm)")
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)

with tab2:
    st.header("Ion Implantation Lab")
    
    icol1, icol2, icol3 = st.columns(3)
    with icol1:
        dopant = st.selectbox("Dopant Species", ["Boron", "Phosphorus", "Arsenic"])
    with icol2:
        energy = st.select_slider("Implant Energy (keV)", options=[10, 30, 50, 100, 200], value=100)
    with icol3:
        dose = st.number_input("Dose (atoms/cm²)", value=1e15, format="%.1e")

    ires_col1, ires_col2 = st.columns([1, 2])
    
    depths, concentrations = doping_profile(dopant, energy, dose)
    
    with ires_col1:
        st.metric("Peak Concentration", f"{max(concentrations):.2e} cm⁻³")
        st.write(f"**Target Dopant:** {dopant}")
        st.info("The profile follows a Gaussian distribution centered at the Projected Range ($R_p$).")

    with ires_col2:
        fig2, ax2 = plt.subplots(figsize=(8, 4))
        ax2.plot(depths, concentrations, color="#2ca02c", lw=2)
        ax2.set_yscale('log')
        ax2.set_ylim(1e12, max(concentrations) * 10)
        ax2.set_xlabel("Depth (nm)")
        ax2.set_ylabel("Concentration (atoms/cm³)")
        ax2.grid(True, which="both", ls="-", alpha=0.2)
        ax2.set_title(f"{dopant} Implantation Profile")
        st.pyplot(fig2)