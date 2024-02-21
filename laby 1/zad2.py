import random
import math
from typing import List, Tuple
import matplotlib.pyplot as plt
import numpy as np

def projectile_motion(initial_height, launch_angle, initial_speed, x):
    g = 9.81
    return initial_height + x * math.tan(math.radians(launch_angle)) - (g * x**2) / (2 * (initial_speed**2) * math.cos(math.radians(launch_angle))**2)

def calculate_distance(v0: float, theta: float, h0: float = 0.0) -> float:
    g = 9.81
    return v0 * math.cos(math.radians(theta)) * (v0 * math.sin(math.radians(theta)) + math.sqrt((v0 * math.sin(math.radians(theta)))**2 + 2 * g * h0)) / g


def main():
    height = 100
    initial_velocity = 50.0
    distance = random.randint(50,340)
    print(f"Odległość do celu: {distance}m")
    alpha = float(input("Podaj kąt rzutu: "))
    
    target_hit = False
    while not target_hit:
        if abs(calculate_distance(initial_velocity, alpha, height) - distance) <= 5:
            print("Cel trafiony!")
            target_hit = True
        else:
            print(f"Pudło!, rzut wynosił: {calculate_distance(initial_velocity, alpha, height)}m")
            alpha = float(input("Podaj kąt rzutu: "))

    x = np.linspace(0, calculate_distance(initial_velocity, alpha, height), 100)
    plt.plot(x, projectile_motion(height, alpha, initial_velocity, x), linestyle='solid')

    plt.show()
if __name__ == "__main__":
    main()