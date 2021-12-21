import io
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import torch
from utils import coordination_2d, rotation, visualization_2d

def on_click(event, x, y, flags, image):
    if event ==cv2.EVENT_LBUTTONDOWN:
        crop_img=image[[y],[x]]
        b=crop_img.T[0].flatten().mean()
        g=crop_img.T[1].flatten().mean()
        r=crop_img.T[2].flatten().mean()
        print('==============================================')
        print(f'coordinate({x},{y})\n color({r},{g},{b})')
        print('==============================================')

def pixel_checker(image):
    cv2.imshow('pixel check',image)
    cv2.setMouseCallback('pixel check',on_click,image)                         
    cv2.waitKey(0)

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
fig, ax = plt.subplots(1, 1, figsize=(4,4))
fig.patch.set_alpha(0)
ax.axes.xaxis.set_ticks([])
ax.axes.yaxis.set_ticks([])
coordination_2d(ax, [-1.5, 1.5], [-1.5, 1.5], grid=False, xyline=False)
rotated_vector = rotation(unit_vector, np.pi/factor)
for i in range(360//(180//factor)):
    rotated_vector = rotation(rotated_vector, np.pi/factor)
    visualization_2d(ax, (0, 0), rotated_vector, color=colors_list[i])
plt.axis('off')
buffer = io.BytesIO()
plt.savefig(buffer,format='png')
data = np.frombuffer(buffer.getvalue(),dtype=np.uint8)
data = cv2.imdecode(data, 1)
data = data[:,:,::-1]
pixel_checker(data)
#img=Image.fromarray(data)
#img=img.convert('RGB')
