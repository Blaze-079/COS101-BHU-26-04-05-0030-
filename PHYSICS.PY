# 1. Potential Energy
mass = float(input("Enter mass (kg): "))
gravity = float(input("Enter gravitational acceleration (m/s²): "))
height = float(input("Enter height (m): "))
potential_energy = mass * gravity * height
print("Potential Energy =", potential_energy, "J")


# 2. Momentum
mass = float(input("Enter mass (kg): "))
velocity = float(input("Enter velocity (m/s): "))
momentum = mass * velocity
print("Momentum =", momentum, "kg·m/s")


# 3. Density
mass = float(input("Enter mass (kg): "))
volume = float(input("Enter volume (m³): "))
density = mass / volume
print("Density =", density, "kg/m³")


# 4. Pressure
force = float(input("Enter force (N): "))
area = float(input("Enter area (m²): "))
pressure = force / area
print("Pressure =", pressure, "Pa")


# 5. Ohm's Law
current = float(input("Enter current (A): "))
resistance = float(input("Enter resistance (Ω): "))
voltage = current * resistance
print("Voltage =", voltage, "V")