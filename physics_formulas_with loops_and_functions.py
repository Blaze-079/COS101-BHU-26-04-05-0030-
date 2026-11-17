def potential_energy():
    mass = float(input("Enter the mass (in kg): "))
    height = float(input("Enter the height (in meters): "))
    gravity = 9.8
    potential_energy = mass * gravity * height
    print(f"The potential energy is {potential_energy}J")


def momentum():
    mass = float(input("Enter the mass (in kg): "))
    velocity = float(input("Enter the velocity (in m/s): "))
    momentum = mass * velocity
    print(f"The momentum is {momentum}kgm/s")


def density():
    mass = float(input("Enter the mass (in kg): "))
    volume = float(input("Enter the volume (in m³): "))
    density = mass / volume
    print(density)
    print(f"The density is {density}kg/m³")


def pressure():
    force = float(input("Enter the force (in N): "))
    area = float(input("Enter the area (in m²): "))
    pressure = force / area
    print(pressure)
    print(f"The pressure is {pressure}Pa")


def ohms_law():
    current = float(input("Enter the current (in A): "))
    resistance = float(input("Enter the resistance (in Ω): "))
    voltage = current * resistance
    print(voltage)
    print(f"The voltage is {voltage}V")


while True:
    print("Physics Calculator")

    formula = ["1. Potential Energy", "2. Momentum", "3. Density", "4. Pressure", "5. Ohm's Law"]

    for form in formula:
        print(form)

    entry = input("Enter a quantity: ")

    if entry == "1":
        potential_energy()
    elif entry == "2":
        momentum()
    elif entry == "3":
        density()
    elif entry == "4":
        pressure()
    elif entry == "5":
        ohms_law()
    else:
        print("Input a valid quantity")

    again = input("Do you want to calculate something else? (yes or no): ")

    if again.lower() == "yes":
        continue
    else:
        print("Thank you")
        break
