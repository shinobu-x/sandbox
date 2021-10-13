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

for i in range(16): # 0~15
    radian = pi * i / 16 * 2
    sin = math.sin(radian)
    cos = math.cos(radian)
    x = center[0] + 10 * sin
    y = center[1] + 10 * cos
    arr[int(center[0]), int(center[1])] = 255, 0, 0
    arr[int(x), int(y)] = colors[i]

img = Image.fromarray(arr)
img.show()
