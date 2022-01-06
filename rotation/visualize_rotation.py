import io
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import torch
from utils import coordination_2d, rotation, visualization_2d, colors_list

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
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    Image.fromarray(image).save('./rgb.jpg')
    cv2.imshow('pixel check',image)
    cv2.setMouseCallback('pixel check',on_click,image)
    cv2.waitKey(0)

def orientation_circle_from_pil():
    factor = 8
    unit_vector = (1, 0)
    fig=plt.figure(figsize = (4,4))
    ax = fig.add_subplot(111)
    coordination_2d(ax, [-1.5,1.5],[-1.5,1.5],grid=True,xyline=True)
    rotated_vector = rotation(unit_vector, np.pi/factor)
    for i in range(360//(180//factor)):
        rotated_vector = rotation(rotated_vector, np.pi/factor)
        visualization_2d(ax, (0, 0), rotated_vector, color=colors_list[i])
    buffer = io.BytesIO()
    plt.savefig(buffer,format='png')
    image = Image.open(buffer)
    data = np.frombuffer(buffer.getvalue(),dtype=np.uint8)
    data = cv2.imdecode(data, 1)
    data = data[:,:,::-1]
    #data = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)
    #pixel_checker(data)
    img=Image.fromarray(data)
    #img=img.convert('RGB')
    img.save('orientation_circle_from_pil.png','PNG')

def orientation_circle_from_numpy():
    w = 256
    h = 256
    circle = np.ones((h, w, 3), dtype=np.uint8)
    x_center = w/2 #- 224
    y_center = h/2 #+ 224
    distance_from_center = 45
    dot_size = 3
    margin = 4
    rectangle_origin_x = x_center - distance_from_center - margin
    rectangle_origin_y = y_center - distance_from_center - margin
    move_to = distance_from_center + margin
    rectangle_to_x = int(x_center) + move_to
    rectangle_to_y = int(rectangle_origin_y) + move_to * 2
    for i in range(int(rectangle_origin_x), rectangle_to_x):
        for j in range(int(rectangle_origin_y), rectangle_to_y):
            circle[i, j] = 192,192,192
    for i in range(16):
        radian = np.pi * i / 16 * 2
        sin = np.sin(radian)
        cos = np.cos(radian)
        x = x_center + distance_from_center * sin
        y = y_center + distance_from_center * cos
        circle[int(x_center), int(y_center)] = 255, 0, 0
        for j in range(0, dot_size):
            for k in range(0, dot_size):
                circle[int(x)+j, int(y)+k] = colors_list[i][0]
                circle[int(x)+j, int(y)-k] = colors_list[i][0]
                circle[int(x)-j, int(y)-k] = colors_list[i][0]
                circle[int(x)-j, int(y)+k] = colors_list[i][0]
    image=Image.fromarray(circle)
    image.save('orientation_circle_from_array.png', 'PNG')

orientation_circle_from_pil()
orientation_circle_from_numpy()
