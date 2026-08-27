# Aerodynamic Drag Calculator
# Calculates aerodynamic drag force and drag power of a vehicle.

from data.vehicle_database import cars

AIR_DENSITY = 1.225  # kg/m³


def find_vehicle(name):
    """Look up a vehicle in the database. Returns (name, cd, area) or None."""
    for key, details in cars.items():
        if name.strip().lower() == key.lower():
            return key, details["cd"], details["area"]
    return None


def calculate_drag(speed_kmh, cd, area):
    """Return (drag_force_N, drag_power_hp, speed_ms)."""
    speed_ms = speed_kmh / 3.6
    drag_force = 0.5 * AIR_DENSITY * cd * area * (speed_ms ** 2)
    drag_power_hp = drag_force * speed_ms / 745.7
    return drag_force, drag_power_hp, speed_ms


if __name__ == "__main__":
    print("\n" + "=" * 55)
    print("              AERODYNAMIC DRAG CALCULATOR")
    print("=" * 55)

    vehicle = input("Enter vehicle name: ").strip()
    found = find_vehicle(vehicle)

    if found:
        name, cd, area = found
        print(f"\nVehicle: {name}")
        print(f"Drag Coefficient (Cd): {cd}")
        print(f"Frontal Area: {area} m²")
    else:
        print("Vehicle not found in database. Enter details manually.")
        cd = float(input("Enter drag coefficient: "))
        area = float(input("Enter frontal area: "))

    speed_kmh = float(input("Enter Vehicle Speed (km/h): "))
    drag_force, drag_power_hp, _ = calculate_drag(speed_kmh, cd, area)

    print("\n" + "=" * 55)
    print("                       RESULTS")
    print("=" * 55)

    print(f"\nVehicle: {found[0] if found else vehicle}")
    print(f"Speed: {speed_kmh} km/h")
    print(f"Aerodynamic Drag Force: {drag_force:.2f} N")
    print(f"Drag Power: {drag_power_hp:.2f} hp\n")
