#ChatGPT nie zrozumiał (lub właśnie zrozumiał zbyt dosłownie) zadanego promptu, który brzmiał:
'''
User
Let's say I have a trebuchet. 
Given initial height of the projectile = 100m, initial speed = 50m/s and some initial angle given by the user, 
calculate whether the projectile hit the target (within +-5 meters) located at a random location 50-340 m away on the ground.
If the target is hit, write "Cel trafiony!", if not, give the user tries until it is hit. 
Create a plot of the projectile position in matplotlib. Write the program in python
'''


import numpy as np
import matplotlib.pyplot as plt

def projectile_motion(angle, target_distance):
    # Constants
    g = 9.81  # acceleration due to gravity (m/s^2)
    initial_height = 100  # initial height of the projectile (m)
    initial_speed = 50  # initial speed of the projectile (m/s)
    
    # Convert angle to radians
    angle_rad = np.radians(angle)
    
    # Calculate time of flight
    time_of_flight = (initial_speed * np.sin(angle_rad) + np.sqrt((initial_speed * np.sin(angle_rad))**2 + 2 * g * initial_height)) / g
    
    # Calculate horizontal range
    horizontal_range = initial_speed * np.cos(angle_rad) * time_of_flight
    
    # Check if the projectile hits the target
    if abs(horizontal_range - target_distance) <= 5:
        print("Cel trafiony!")
        return True
    else:
        print("Pudło! Spróbuj ponownie.")
        return False

# Generate a random target distance between 50 and 340 meters
target_distance = np.random.randint(50, 341)

# Ask user for initial angle
while True:
    try:
        initial_angle = float(input("Podaj kąt początkowy (w stopniach): "))
        break
    except ValueError:
        print("Podaj poprawną liczbę.")

# Plot projectile motion
angle_rad = np.radians(initial_angle)
time_of_flight = (50 * np.sin(angle_rad) + np.sqrt((50 * np.sin(angle_rad))**2 + 2 * 9.81 * 100)) / 9.81
time = np.linspace(0, time_of_flight, num=1000)
x = 50 * np.cos(angle_rad) * time
y = 100 + 50 * np.sin(angle_rad) * time - 0.5 * 9.81 * time**2

plt.plot(x, y)
plt.xlabel('Odległość (m)')
plt.ylabel('Wysokość (m)')
plt.title('Rzut ukośny')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

# Check if the projectile hits the target
hit = False
while not hit:
    hit = projectile_motion(initial_angle, target_distance)
