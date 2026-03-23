import numpy as np
from ioimp_datalib import dopant_data

# the math

def doping_profile(dopant, energy, dose):
    if energy not in dopant_data[dopant]:
        energies = sorted(dopant_data[dopant].keys())
        closest_energy = (min(energies, key=lambda x: abs(x - energy)))
        rp, drp = dopant_data[dopant][closest_energy]
    
    else:
        rp, drp = dopant_data[dopant][energy]

    x = np.linspace(0, 1000, 500)

    # the formulas

    cp = dose / (np.sqrt(2 * 3.14) * drp)
    cx = cp * np.exp(-(x - rp)**2 / (2 * (drp)**2))

    return x, cx

# execute

if __name__ == "__main__":
    depth, conc = calculate = doping_profile("Boron", 100, 1e15)
    print(f"Peak Concentration: {max(conc):.2e} atoms/cm^3")



