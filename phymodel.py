import numpy as np
from conversions import c_to_k, min_to_hr, μm_to_nm

# the math

KB = 8.617e-5  
B0_DRY = 629.84    
BA0_DRY = 1.68e7

def thickness_computation(T_c, t_min, pressure=1.0, mode="dry"):
    T = c_to_k(T_c)
    t = min_to_hr(t_min)

    b = B0_DRY * np.exp(-1.24 / (KB * T)) * pressure
    ba = BA0_DRY * np.exp(-2.00 / (KB * T)) * pressure
    
    a = b / ba
    τ = 0 
    
    x_μm = (-a + np.sqrt(a**2 + 4 * b * (t + τ))) / 2
    
    return μm_to_nm(x_μm)

# execute

if __name__ == "__main__":
    res = thickness_computation(1000, 60, 1.0, "dry")
    print(f"{res:.2f} nm")