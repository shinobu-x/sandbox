import numpy as np
import matplotlib.pyplot as plt
from utils import coordination_2d, rotation, visualization_2d

factor = 8
unit_vector = (1, 0)
fig, ax = plt.subplots(1, 1, figsize=(5, 5))
coordination_2d(ax, [-1.5, 1.5], [-1.5, 1.5])
rotated_vector = rotation(unit_vector, np.pi/factor) 
for _ in range(360//(180//factor)):
    rotated_vector = rotation(rotated_vector, np.pi/factor)
    visualization_2d(ax, (0, 0), rotated_vector, color="blue")
#ax.text(unit_vector[0], unit_vector[1]+0.05, "u", color="blue", size=16)
#visualization_2d(ax, (0, 0), rotated_vector, color="red")
#ax.text(rotated_vector[0], rotated_vector[1], "Ru", color="red", size=16)
plt.show()

