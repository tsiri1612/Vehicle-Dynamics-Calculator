# Calculates Aerodynamic Drag Force of Vehicle

from data.vehicle_database import cars

AIR_DENSITY = 1.225  #kg/m³ 

print("\n" + "=" * 55)
print("              AERODYNAMIC DRAG CALCULATOR")
print("=" * 55)

vehicle = input("Enter vehicle name: ").strip()

found = False

for name, details in cars.items():
    if vehicle.lower() == name.lower():
        cd = details["cd"]
        area = details["area"]

        print(f"\nVehicle: {name}")
        print(f"Drag Coefficient (Cd): {cd}")
        print(f"Frontal Area: {area} m²")

        found = True
        break

if not found:
    print("Vehicle not found in database. Enter details manually.")
    cd = float(input("Enter drag coefficient: "))
    area = float(input("Enter frontal area: "))

speed_kmh = float(input("Enter Vehicle Speed (km/h): "))
speed_ms = speed_kmh / 3.6

drag_force = 0.5 * AIR_DENSITY * cd * area * (speed_ms ** 2)

print("\n" + "=" * 55)
print("                       RESULTS")
print("=" * 55)

if found:
    print(f"\nVehicle: {name}")
else:
    print(f"\nVehicle: {vehicle}")

print(f"Speed: {speed_kmh} km/h")

print(f"Aerodynamic Drag Force: {drag_force:.2f} N")
drag_power = drag_force * speed_ms
print(f"Drag Power: {drag_power / 745.7:.2f} hp\n")