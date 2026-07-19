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

d = (speed ** 2)/(2 * mu * GRAVITY)

print(f"\nEstimated braking distance: {d:.2f} m\n")