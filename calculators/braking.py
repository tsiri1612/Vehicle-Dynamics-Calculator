# Braking Distance Calculator
# Estimates stopping distance using vehicle speed, road surface and driver condition.

GRAVITY = 9.81

ROAD_CONDITIONS = {
    1: ("Dry", 0.8),
    2: ("Wet", 0.5),
    3: ("Snow", 0.2),
    4: ("Ice", 0.1),
}

DRIVER_CONDITIONS = {
    1: ("Alert", 0.8),
    2: ("Average", 1.5),
    3: ("Fatigued", 2.0),
    4: ("Distracted", 2.5),
}


def calculate_stopping(speed_kmh, road_condition, driver_condition):
    """Return (reaction_m, braking_m, stopping_m, road_label, driver_label)."""
    speed = speed_kmh / 3.6
    road_label, mu = ROAD_CONDITIONS[road_condition]
    driver_label, rxn_time = DRIVER_CONDITIONS[driver_condition]

    braking_distance = (speed ** 2) / (2 * mu * GRAVITY)
    reaction_distance = speed * rxn_time

    return reaction_distance, braking_distance, reaction_distance + braking_distance, road_label, driver_label


if __name__ == "__main__":
    print("\n" + "=" * 55)
    print("           BRAKING DISTANCE CALCULATOR")
    print("=" * 55)

    speed_kmh = float(input("\nEnter speed (km/h): "))

    print("\nRoad Conditions")
    print("-" * 20)
    for key, (label, _) in ROAD_CONDITIONS.items():
        print(f"{key}. {label}")

    road = int(input("\nSelect road condition: "))
    if road not in ROAD_CONDITIONS:
        print("Invalid road condition")
        exit()

    print("\nDriver Conditions")
    print("-" * 20)
    for key, (label, _) in DRIVER_CONDITIONS.items():
        print(f"{key}. {label}")

    driver = int(input("\nSelect driver condition: "))
    if driver not in DRIVER_CONDITIONS:
        print("Invalid driver condition")
        exit()

    reaction_distance, braking_distance, stopping_distance, _, _ = calculate_stopping(speed_kmh, road, driver)

    print("\n" + "=" * 55)
    print("               STOPPING DISTANCE REPORT")
    print("=" * 55)

    print(f"{'Estimated reaction distance':<30}: {reaction_distance:.2f} m")
    print(f"{'Estimated braking distance':<30}: {braking_distance:.2f} m")
    print(f"{'Total stopping distance':<30}: {stopping_distance:.2f} m")

    print("=" * 55)
