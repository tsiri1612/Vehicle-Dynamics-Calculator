#Engine RPM Calculator using vehicle speed, tyre diameter, gear ratio, final drive (differential) ratio
import math

print("\n" + "=" * 55)
print("              ENGINE RPM CALCULATOR")
print("=" * 55)

speed = float(input(f"\n{'Vehicle Speed (km/h)':<35}: "))
tyre_inches = float(input(f"{'Tyre Diameter (inches)':<35}: "))
gear_ratio = float(input(f"{'Gear Ratio':<35}: "))
final_drive_ratio = float(input(f"{'Final Drive (Differential) Ratio':<35}: "))

tyre_metres = tyre_inches * 0.0254
tyre_circumference = (math.pi) * tyre_metres
speed_m_per_min = speed * 16.6667

wheel_rpm = speed_m_per_min / tyre_circumference
engine_rpm = wheel_rpm * gear_ratio * final_drive_ratio

print("\n" + "=" * 55)
print("               STOPPING DISTANCE REPORT")
print("=" * 55)

print(f"\n{'Wheel RPM':<30}: {wheel_rpm:.2f} RPM")
print(f"{'Estimated Engine RPM':<30}: {engine_rpm:.2f} RPM\n")