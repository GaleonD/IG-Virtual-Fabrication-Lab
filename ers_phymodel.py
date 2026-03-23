from ers_datalib import etch_data

# the math

def etch_profile(etchant, initial_thickness, time):

    data = etch_data[etchant]
    target = data["SiO2"] if "SiO2" in data else data.get("Si3N4", 10)
    substrate = data["Silicon"]

    # the formulas
    
    selectivity = target / substrate if substrate > 0 else float('inf')
    
    etched_target = target * time
    remaining_target = max(0, initial_thickness - etched_target)
    
    time_to_clear = initial_thickness / target
    over_etch_time = max(0, time - time_to_clear)
    substrate_loss = over_etch_time * substrate
    
    return {

        "remaining_target": remaining_target,
        "substrate_loss": substrate_loss,
        "selectivity": selectivity,
        "is_cleared": remaining_target == 0

    }

# execute

if __name__ == "__main__":

    res = etch_profile("Hydrogen Fluoride (Buffered)", 100, 1.5)
    print(f"Remaining Oxide: {res['remaining_target']} nm")
    print(f"Substrate Loss: {res['substrate_loss']:.2f} nm")
    print(f"Selectivity: {res['selectivity']}:1")
