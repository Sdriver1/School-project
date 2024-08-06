# Constants
G = 6.67E-11  # Gravitational Constant (m^3 kg^-1 s^-2)
E = 1.6E-19   # Elementary Charge (Coulombs)
K = 8.99E9    # Coulomb's Constant (N m^2 C^-2)
C = 3E8       # Speed of Light in Vacuum (m/s)
h = 6.626E-34 # Planck's Constant (Js)
R = 8.314     # Ideal Gas Constant (J/(mol K))

# Basic Functions
def velo():
    d = float(input("Enter the distance (m): "))
    t = float(input("Enter the time (s): "))
    v = d/t
    print("The velocity is: ", v, "m/s")

def accel():
    v = float(input("Enter the change in velocity (m/s): "))
    t = float(input("Enter the time (s): "))
    a = v/t
    print("The acceleration is: ", a, "m/s^2")

def force():
    m = float(input("Enter the mass (kg): "))
    a = float(input("Enter the acceleration (m/s^2): "))
    f = m*a
    print("The force is: ", f, "N")

def momentum():
    m = float(input("Enter the mass (kg): "))
    v = float(input("Enter the velocity (m/s): "))
    p = m*v
    print("The momentum is: ", p, "kg m/s")

def ke():
    m = float(input("Enter the mass (kg): "))
    v = float(input("Enter the velocity (m/s): "))
    ke = 0.5*m*v**2
    print("The kinetic energy is: ", ke, "J")

def pe():
    m = float(input("Enter the mass (kg): "))
    h = float(input("Enter the height (m): "))
    g = float(input("Enter the acceleration due to gravity (m/s^2): "))
    pe = m*g*h
    print("The potential energy is: ", pe, "J")

def grav_force():
    m1 = float(input("Enter the mass of the first object (kg): "))
    m2 = float(input("Enter the mass of the second object (kg): "))
    r = float(input("Enter the distance between the objects (m): "))
    f = G * (m1 * m2) / r**2
    print("The gravitational force is: ", f, "N")

def coulomb_force():
    q1 = float(input("Enter the charge of the first object (C): "))
    q2 = float(input("Enter the charge of the second object (C): "))
    r = float(input("Enter the distance between the charges (m): "))
    f = K * (q1 * q2) / r**2
    print("The Coulomb force is: ", f, "N")

def wave_energy():
    f = float(input("Enter the frequency of the wave (Hz): "))
    E_wave = h * f
    print("The energy of the wave is: ", E_wave, "J")

def einstein_energy():
    m = float(input("Enter the mass (kg): "))
    E_mass = m * C**2
    print("The energy equivalent of the mass is: ", E_mass, "J")

def ohms_law():
    V = float(input("Enter the voltage (V): "))
    R = float(input("Enter the resistance (Ohms): "))
    I = V/R
    print("The current is: ", I, "A")

def power():
    V = float(input("Enter the voltage (V): "))
    I = float(input("Enter the current (A): "))
    P = V * I
    print("The power is: ", P, "W")

def pressure():
    F = float(input("Enter the force (N): "))
    A = float(input("Enter the area (m^2): "))
    P = F/A
    print("The pressure is: ", P, "Pa")

def ideal_gas_law():
    P = float(input("Enter the pressure (Pa): "))
    V = float(input("Enter the volume (m^3): "))
    n = float(input("Enter the amount of substance (mol): "))
    T = float(input("Enter the temperature (K): "))
    PVnRT = P * V / (n * R * T)
    print("PV/nRT is: ", PVnRT) 

def heat_energy():
    m = float(input("Enter the mass (kg): "))
    c = float(input("Enter the specific heat capacity (J/(kg K)): "))
    dT = float(input("Enter the change in temperature (K): "))
    Q = m * c * dT
    print("The heat energy is: ", Q, "J")

def main():
    functions = {
        1: velo,
        2: accel,
        3: force,
        4: momentum,
        5: ke,
        6: pe,
        7: grav_force,
        8: coulomb_force,
        9: wave_energy,
        10: einstein_energy,
        11: ohms_law,
        12: power,
        13: pressure,
        14: ideal_gas_law,
        15: heat_energy,
    }
    
    print("Welcome to the Physics Calculator!")
    print("Choose a function:")
    print("1. Velocity | 2. Acceleration | 3. Force ")
    print("4. Momentum | 5. Kinetic Energy | 6. Potential Energy")
    print("7. Gravitational Force | 8. Coulomb Force | 9. Wave Energy")
    print("10. Einstein Energy | 11. Ohm's Law | 12. Power")
    print("13. Pressure | 14. Ideal Gas Law | 15. Heat Energy")
    
    choice = int(input("Enter the number of the function: "))
    
    func = functions.get(choice)
    if func:
        func()
    else:
        print("Invalid choice. Please try again.")
    
    cont = input("Would you like to perform another calculation? (y/n): ")
    if cont.lower() == "y":
        main()
    else:
        print("Thank you for using the Physics Calculator!")

if __name__ == "__main__":
    main()
