import numpy as np
import matplotlib.pyplot as plt
from utils import coordination_2d, rotation, visualization_2d

d0 =  [199,  21, 133] # MediumVioletRed
d1 =  [220,  20,  60] # Crimson
d2 =  [255,  99,  71] # Tomato
d3 =  [255, 218, 185] # PeachPuff
d4 =  [255, 228, 181] # Moccasin
d5 =  [ 34, 139,  34] # ForestGreen
d6 =  [  0, 255, 255] # Aqua
d7 =  [ 30, 144, 255] # DodgerBlue
d8 =  [135, 206, 235] # SkyBlue
d9 =  [ 47,  79,  79] # DarkSlateGray
d10 = [245, 255, 250] # MintCream
d11 = [253, 245, 230] # OldLace
d12 = [255, 228, 225] # MistyRose
d13 = [218, 112, 214] # Orchid
d14 = [138,  43, 226] # VlueViolet
d15 = [ 75,   0, 130] # Indigo
colors_list = [[d0],[d1],[d2],[d3],[d4],[d5],[d6],[d7],[d8],[d9],[d10],[d11],[d12],[d13],[d14],[d15]]
factor = 8
unit_vector = (1, 0)
fig, ax = plt.subplots(1, 1, figsize=(5, 5))
coordination_2d(ax, [-1.5, 1.5], [-1.5, 1.5])
rotated_vector = rotation(unit_vector, np.pi/factor)
for i in range(360//(180//factor)):
    print(i)
    visualization_2d(ax, (0.5, 0.5), rotated_vector, color=colors_list[i])
    rotated_vector = rotation(rotated_vector, np.pi/factor)
plt.show()
