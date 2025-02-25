from djitellopy import Tello
import time

# Initialize the Tello drone object
drone = Tello()

# Connect to the drone
drone.connect()

# Print the battery level (optional)
print(f"Battery: {drone.get_battery()}%")

# Take off
drone.takeoff()

# Wait for a second to stabilize
time.sleep(1)

# Move forward 30 cm to position 30 cm away from the point
drone.move_forward(30)

# Time to perform the circular motion around the point.
# We'll do this in steps by combining small forward movements and rotations.

# Number of steps in the circle (higher means smoother circle)
steps = 12
# The angle to turn at each step to complete a full circle (360°/steps)
angle_per_step = 360 // steps
# The distance to move left at each step to simulate a smooth orbit
distance_per_step = 20  # Adjust this to control orbit radius (in cm)

# Orbit around the point while facing it (clockwise orbit)
for _ in range(steps):
    drone.move_left(distance_per_step)   # Move left to simulate the orbit
    drone.rotate_clockwise(angle_per_step)  # Rotate to face the point

# Wait for a second after completing the orbit
time.sleep(1)

# Reverse the circular motion to return to the starting point (counter-clockwise orbit)
for _ in range(steps):
    drone.move_right(distance_per_step)   # Move right to retrace the orbit
    drone.rotate_counter_clockwise(angle_per_step)  # Rotate to face the point

# Move backward 30 cm to return to the exact takeoff point
drone.move_back(30)

# Land the drone at the same spot
drone.land()

# End the connection
drone.end()
