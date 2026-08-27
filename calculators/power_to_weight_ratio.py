# Power-to-Weight Ratio Calculator


def calculate_power_to_weight(power_hp, weight_kg):
    """Return (ratio_hp_per_tonne, kg_per_hp)."""
    weight_tonne = weight_kg / 1000
    ratio = power_hp / weight_tonne
    kg_per_hp = weight_kg / power_hp
    return ratio, kg_per_hp


if __name__ == "__main__":
    print("=" * 50)
    print("        POWER-TO-WEIGHT RATIO CALCULATOR")
    print("=" * 50)

    power_hp = float(input(f"{'Engine Power (hp)':<30}: "))
    weight_kg = float(input(f"{'Vehicle Weight (kg)':<30}: "))

    ratio, kg_per_hp = calculate_power_to_weight(power_hp, weight_kg)

    print("-" * 50)

    print(f"{'Power-to-Weight ratio':<30}: {ratio:.2f} hp/tonne")
    print(f"{'Weight per Horsepower':<30}: {kg_per_hp:.2f} kg/hp\n")
