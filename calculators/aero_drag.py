# Calculates Aerodynamic Drag Force of Vehicle

from data.vehicle_database import cars

AIR_DENSITY = 1.225  #kg/m³ 

print("\n" + "=" * 55)
print("              AERODYNAMIC DRAG CALCULATOR")
print("=" * 55)

'''cars = {
    # HATCHBACKS
    "Maruti Suzuki Swift": {"cd": 0.32, "area": 2.05},
    "Maruti Suzuki Baleno": {"cd": 0.31, "area": 2.08},
    "Hyundai i20": {"cd": 0.31, "area": 2.08},
    "Volkswagen Polo": {"cd": 0.32, "area": 2.03},
    "Tata Altroz": {"cd": 0.32, "area": 2.10},

    # SEDANS
    "Honda City": {"cd": 0.29, "area": 2.20},
    "Hyundai Verna": {"cd": 0.28, "area": 2.20},
    "Honda Civic": {"cd": 0.27, "area": 2.18},
    "Volkswagen Virtus": {"cd": 0.30, "area": 2.23},
    "Skoda Slavia": {"cd": 0.29, "area": 2.23},
    "Maruti Suzuki Ciaz": {"cd": 0.29, "area": 2.21},
    "Audi A4": {"cd": 0.26, "area": 2.22},
    "Mercedes-Benz S-Class": {"cd": 0.22, "area": 2.40},

    # SUVs
    "Hyundai Venue": {"cd": 0.35, "area": 2.30},
    "Maruti Suzuki Brezza": {"cd": 0.35, "area": 2.35},
    "Toyota Hyryder": {"cd": 0.34, "area": 2.38},
    "Maruti Suzuki Grand Vitara": {"cd": 0.34, "area": 2.38},
    "Hyundai Creta": {"cd": 0.36, "area": 2.45},
    "Kia Seltos": {"cd": 0.35, "area": 2.43},
    "Tata Nexon": {"cd": 0.36, "area": 2.38},
    "Tata Harrier": {"cd": 0.36, "area": 2.55},
    "MG Hector": {"cd": 0.37, "area": 2.60},
    "Mahindra XUV700": {"cd": 0.35, "area": 2.60},
    "Mahindra Scorpio-N": {"cd": 0.40, "area": 2.70},
    "Toyota Fortuner": {"cd": 0.38, "area": 2.75},
    "Mahindra Thar": {"cd": 0.52, "area": 2.65},
    "Toyota Land Cruiser 300": {"cd": 0.35, "area": 2.90},
    "Range Rover Sport": {"cd": 0.34, "area": 2.80},

    # MPVs
    "Toyota Innova Hycross": {"cd": 0.34, "area": 2.65},

    # SPORTS / PERFORMANCE
    "Toyota Supra MK5": {"cd": 0.31, "area": 2.00},
    "Porsche 911 Carrera": {"cd": 0.29, "area": 2.05},
    "BMW M3": {"cd": 0.34, "area": 2.25},
    "BMW M4 Competition": {"cd": 0.34, "area": 2.18},
    "Audi S5": {"cd": 0.29, "area": 2.20},
    "Ford Mustang GT": {"cd": 0.36, "area": 2.25},
    "Nissan GT-R R35": {"cd": 0.26, "area": 2.10},
    "Bugatti Chiron": {"cd": 0.36, "area": 2.07},
    "Koenigsegg Jesko": {"cd": 0.28, "area": 1.95},

    # ELECTRIC VEHICLES
    "Tata Punch EV": {"cd": 0.36, "area": 2.30},
    "Tata Nexon EV": {"cd": 0.35, "area": 2.38},
    "Tata Curvv EV": {"cd": 0.30, "area": 2.42},
    "MG Windsor EV": {"cd": 0.29, "area": 2.45},
    "MG ZS EV": {"cd": 0.33, "area": 2.43},
    "Hyundai Creta Electric": {"cd": 0.34, "area": 2.42},
    "Mahindra BE 6": {"cd": 0.27, "area": 2.38},
    "Mahindra XEV 9e": {"cd": 0.26, "area": 2.50},
    "Tesla Model 3": {"cd": 0.23, "area": 2.22},
    "Tesla Model S": {"cd": 0.208, "area": 2.34}
}'''

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