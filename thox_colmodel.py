import numpy as np
from main_conversions import nox

# the math

def oxide_color(thickness_nm):
    if thickness_nm < 10:
        return "#C0C0C0"
    
    quench_wavelength = None
    for m in range(5):
        lambda_val = (2 * nox * thickness_nm) / (m + 0.5)
        if 380 <= lambda_val <= 750:
            quench_wavelength = lambda_val
            break
    
    if quench_wavelength:
        return comp_color(quench_wavelength)
        
    return "#D2B48C"

def comp_color(w):
    if 380 <= w <= 440: return "#D2B48C"
    if 440 <= w <= 490: return "#DAA520"
    if 490 <= w <= 550: return "#8B4513"
    if 550 <= w <= 580: return "#0000FF"
    if 580 <= w <= 620: return "#00FFFF"
    if 620 <= w <= 750: return "#00FF00"
    return "#D3D3D3"

# execute

if __name__ == "__main__":
    print(oxide_color(71.08))