#QUESTION 4

import numpy as np

cartesian_points=np.random.rand(10,2)*10 

r = np.sqrt(cartesian_points[:, 0]**2 + cartesian_points[:, 1]**2)
theta = np.arctan(cartesian_points[:, 1], cartesian_points[:, 0])

print("Cartesian Coordinates (x, y):\n", cartesian_points)
for i in range(len(cartesian_points)):
    print(f"Point {i+1}: (x, y) = ({cartesian_points[i][0]:.2f},{cartesian_points[i][1]:.2f} ) => (r, theta) = ({r[i]:.2f}, {theta[i]:.2f})")

