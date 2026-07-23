# Power-to-Weight Ratio Calculator

print("=" * 50)
print("        POWER-TO-WEIGHT RATIO CALCULATOR")
print("=" * 50)

power_hp = float(input(f"{'Engine Power (hp)':<30}: "))
weight_kg = float(input(f"{'Vehicle Weight (kg)':<30}: "))

weight_tonne = weight_kg / 1000

power_to_weight = power_hp / weight_tonne
kg_per_hp = weight_kg / power_hp

print("-" * 50)

print(f"{'Power-to-Weight ratio':<30}: {power_to_weight:.2f} hp/tonne")
print(f"{'Weight per Horsepower':<30}: {kg_per_hp:.2f} kg/hp\n")