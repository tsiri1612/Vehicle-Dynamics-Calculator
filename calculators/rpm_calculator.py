# Engine RPM Calculator
# Uses vehicle speed, tyre diameter, gear ratio and final drive (differential) ratio.
import math


def calculate_rpm(speed_kmh, tyre_inches, gear_ratio, final_drive_ratio):
    """Return (wheel_rpm, engine_rpm)."""
    tyre_metres = tyre_inches * 0.0254
    tyre_circumference = math.pi * tyre_metres
    speed_m_per_min = speed_kmh * 16.6667

    wheel_rpm = speed_m_per_min / tyre_circumference
    engine_rpm = wheel_rpm * gear_ratio * final_drive_ratio
    return wheel_rpm, engine_rpm


if __name__ == "__main__":
    print("\n" + "=" * 55)
    print("              ENGINE RPM CALCULATOR")
    print("=" * 55)

    speed = float(input(f"\n{'Vehicle Speed (km/h)':<35}: "))
    tyre_inches = float(input(f"{'Tyre Diameter (inches)':<35}: "))
    gear_ratio = float(input(f"{'Gear Ratio':<35}: "))
    final_drive_ratio = float(input(f"{'Final Drive (Differential) Ratio':<35}: "))

    wheel_rpm, engine_rpm = calculate_rpm(speed, tyre_inches, gear_ratio, final_drive_ratio)

    print("\n" + "=" * 55)
    print("               ENGINE RPM REPORT")
    print("=" * 55)

    print(f"\n{'Wheel RPM':<30}: {wheel_rpm:.2f} RPM")
    print(f"{'Estimated Engine RPM':<30}: {engine_rpm:.2f} RPM\n")
