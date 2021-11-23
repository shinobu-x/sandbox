import numpy as np
import math
from PIL import Image

pi=math.pi
h = 256
w = 256
c = 3
arr = np.ones((h, w, c), dtype=np.uint8) * 255 # white
center = (h/2,w/2)
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
colors = np.array([d0,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15])
x_center = center[0] - 96
y_center = center[1] + 96
distance_from_center = 15
margin = 4
rectangle_origin_x = x_center - distance_from_center - margin
rectangle_origin_y = y_center - distance_from_center - margin
rectangle_to_x = int(x_center + (distance_from_center + margin))
rectangle_to_y = int(rectangle_origin_y) + (distance_from_center + margin) * 2
for i in range(int(rectangle_origin_x), rectangle_to_x):
    for j in range(int(rectangle_origin_y), rectangle_to_y):
        arr[i, j] = 192, 192, 192
arr[int(x_center), int(y_center)] = 255, 0, 0
for i in range(0, 2):
    for j in range(0, 2):
        arr[int(x_center)+i, int(y_center)+j] = 255, 0, 0
        arr[int(x_center)+i, int(y_center)-j] = 255, 0, 0
        arr[int(x_center)-i, int(y_center)-j] = 255, 0, 0
        arr[int(x_center)-i, int(y_center)+j] = 255, 0, 0
#arr[int(rectangle_origin_x), int(rectangle_origin_y)] = 255, 0, 0
for i in range(16): # 0~15
    radian = pi * i / 16 * 2
    sin = math.sin(radian)
    cos = math.cos(radian)
    x = x_center + distance_from_center * sin
    y = y_center + distance_from_center * cos
    arr[int(x_center), int(y_center)] = 255, 0, 0
    for j in range(0, 2):
        for k in range(0, 2):
            arr[int(x)+j, int(y)+k] = colors[i]
            arr[int(x)+j, int(y)-k] = colors[i]
            arr[int(x)-j, int(y)-k] = colors[i]
            arr[int(x)-j, int(y)+k] = colors[i]

img = Image.fromarray(arr)
img.show()
