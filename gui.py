import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from phymodel import thickness_computation
from colmodel import oxide_color

st.set_page_config(page_title="VLSI Thermal Oxidation Lab", layout="wide")

st.sidebar.header("Process Controls")
crystal = st.sidebar.selectbox("Crystal Orientation", ["(100) Silicon", "(111) Silicon"])
mode = st.sidebar.radio("Environment", ["Dry O2", "Wet H2O"], index=0)
st.sidebar.markdown("---")
st.sidebar.info("Model: Deal-Grove with Arrhenius Dependence")

st.title("Thermal Oxidation Predictive Dashboard")
st.markdown("---")

col1, col2, col3 = st.columns(3)
with col1:
    temp_c = st.slider("Temperature (°C)", 700, 1200, 1000)
with col2:
    t_min = st.number_input("Oxidation Time (min)", min_value=1, max_value=1440, value=60)
with col3:
    pressure = st.slider("Process Pressure (atm)", 0.1, 15.0, 1.00)

st.markdown("---")

res_col1, res_col2 = st.columns([1, 2])

with res_col1:
    st.subheader("Physical Output")
    
    thickness = thickness_computation(temp_c, t_min, pressure, mode.lower()[:3])
    color_hex = oxide_color(thickness)
    
    st.metric(label="Oxide Thickness ($x_o$)", value=f"{thickness:.2f} nm")
    
    st.write("**Visual Color Profile**")
    st.markdown(
        f"""
        <div style="
            background-color:{color_hex}; 
            width:100%; 
            height:150px; 
            border-radius:15px; 
            border:3px solid #444; 
            display:flex; 
            align-items:center; 
            justify-content:center; 
            color:white; 
            font-size:20px;
            font-weight:bold; 
            text-shadow: 2px 2px 4px #000;">
            {color_hex.upper()}
        </div>
        """, 
        unsafe_allow_html=True
    )
    st.caption(f"Estimated visible color for {thickness:.1f}nm $SiO_2$")

with res_col2:
    st.subheader("Real-time Growth Curve")
    
    times = np.linspace(1, max(t_min * 1.5, 200), 100)
    thicknesses = [thickness_computation(temp_c, t, pressure, mode.lower()[:3]) for t in times]
    
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(times, thicknesses, color='#1f77b4', linewidth=2.5, label='Oxide Thickness')
    ax.scatter([t_min], [thickness], color='red', s=100, zorder=5, label='Current Point')
    
    ax.set_xlabel("Time (min)", fontsize=10)
    ax.set_ylabel("Thickness (nm)", fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()
    
    st.pyplot(fig)

st.markdown("---")
st.caption("Developed by Indrajith (and AI)")