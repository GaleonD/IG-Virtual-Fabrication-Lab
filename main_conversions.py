kb = 8.617e-5  
nox = 1.46     

def c_to_k(T_c):
    return T_c + 273.15

def min_to_hr(t_min):
    return t_min / 60

def μm_to_nm(x_μm):
    return x_μm * 1000

def nm_to_μm(x_nm):
    return x_nm / 1000

def clamp(val, min_val, max_val):
    return max(min_val, min(val, max_val))