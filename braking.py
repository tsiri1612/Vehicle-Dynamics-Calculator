# Braking Distance Calculator 
# Estimates braking distance using vehicle speed and road surface friction. 

print("\nBraking Distance Calculator\n")

speeeed=float(input("Enter speed (km/h): "))
speed = speeeed/3.6

print("\nRoad conditions")
print("1.Dry")
print("2.Wet")
print("3.Snow")
print("4.Ice")

road=int(input("\nSelect road condition: "))

mu = 0

if road == 1:
    mu = 0.8
elif road == 2:
    mu = 0.5
elif road == 3:
    mu = 0.2
elif road == 4:
    mu = 0.1
else:
    print("Invalid road condition")
    exit()

GRAVITY=9.81

braking_distance = (speed ** 2)/(2 * mu * GRAVITY)

print("\nDriver conditions")
print("1.Alert")
print("2.Average")
print("3.Fatigued")
print("4.Distracted")

driver=int(input("\nSelect driver condition: "))

rxn_time=0

if driver == 1:
    rxn_time = 0.8
elif driver == 2:
    rxn_time = 1.5
elif driver == 3:
    rxn_time = 2.0
elif driver == 4:
    rxn_time = 2.5
else:
    print("Invalid driver condition")
    exit()

reaction_distance = speed * rxn_time

stopping_distance = braking_distance + reaction_distance

print(f"\n{'Estimated reaction distance':<30}: {reaction_distance:.2f} m")
print(f"{'Estimated braking distance':<30}: {braking_distance:.2f} m")
print(f"{'Total stopping distance':<30}: {stopping_distance:.2f} m\n")