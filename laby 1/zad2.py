import random
import math
from typing import List, Tuple
import matplotlib.pyplot as plt
import numpy as np

def projectile_motion(initial_height, launch_angle, initial_speed, x):
    g = 9.81
    vx = initial_speed * math.cos(math.radians(launch_angle))
    vy = initial_speed * math.sin(math.radians(launch_angle))
    return -g/(2*launch_angle**2) * x**2 + math.tan(launch_angle) * x + initial_height

def calculate_distance(v0: float, theta: float, h0: float = 0.0) -> float:
    return v0 * math.sin(math.radians(theta)) + math.sqrt(v0**2 * math.sin(math.radians(theta))**2 + 2 * 9.81 * h0) * math.cos(math.radians(theta)) * v0 / 9.81


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

    x = np.linspace(0, 340, 100)
    plt.plot(x, projectile_motion(height, alpha, initial_velocity, x), linestyle='solid')

    # plt.axis([0, 300, 0, 140])
    plt.show()
if __name__ == "__main__":
    main()