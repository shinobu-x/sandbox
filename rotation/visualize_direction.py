import os
import io
import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import pi
from utils import coordination_2d, rotation, visualization_2d
from utils import colors_list

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

def get_rotation(index):
    factor=8
    unit_vector=(1,0)
    fig,ax = plt.subplots(1,1,figsize=(1,1))
    ax.axes.xaxis.set_ticks([])
    ax.axes.yaxis.set_ticks([])
    coordination_2d(ax,[-1.5,1.5],[-1.5,1.5],grid=False,xyline=False)
    rotated_vector=rotation(unit_vector,index*(pi/factor))
    visualization_2d(ax,(0,0),rotated_vector,color=colors_list[index])
    plt.axis('off')
    buffer=io.BytesIO()
    plt.savefig(buffer,format='png')
    direction = np.frombuffer(buffer.getvalue(),dtype='uint8')
    direction = cv2.imdecode(direction,1)
    direction = direction[:,:,::-1]
    direction = np.where(direction==255.0,0,direction)
    return direction

def visualize_direction():
    factor=8
    unit_vector=(1,0)
    fig,ax = plt.subplots(1,1,figsize=(1,1))
    fig.patch.set_alpha(0)
    ax.axes.xaxis.set_ticks([])
    ax.axes.yaxis.set_ticks([])
    coordination_2d(ax,[-1.5,1.5],[-1.5,1.5],grid=False,xyline=False)
    rotated_vector=rotation(unit_vector,pi/factor)
    for i in range(360//(180//factor)):
        rotated_vector = rotation(rotated_vector,pi/factor)
        visualization_2d(ax,(0,0),rotated_vector,color=colors_list[i])
    plt.axis('off')
    buffer = io.BytesIO()
    plt.savefig(buffer,format='png')
    rotations=np.frombuffer(buffer.getvalue(),dtype='uint8')
    rotations=cv2.imdecode(rotations,1)
    rotations=rotations[:,:,::-1]
    rotations=np.where(rotations==255.0,0,rotations)
    rotations_h,rotations_w,_=rotations.shape
    distance_h,distance_w=rotations_h//2,rotations_w//2
    #pixel_checker(rotations)
    save_dir='./output'
    img_room = np.zeros((512,512,3),dtype='uint8')
    img_wall = np.zeros((512,512,3))
    img=cv2.imread(f'masked_sample.png')
    #cv2.imshow('sample',img)
    #cv2.setMouseCallback('sample',on_click)
    #cv2.waitKey(0)
    img_room[:,:,0]=np.where(img[:,:,0]==129.0,img[:,:,0],0)
    img_room[:,:,1]=np.where(img[:,:,1]==129.0,img[:,:,1],0)
    img_room[:,:,2]=np.where(img[:,:,2]==129.0,img[:,:,2],0)
    #cv2.imwrite(f'{save_dir}/sample_output1.png',img_room)
    #cv2.imshow('sample',img_room)
    #cv2.setMouseCallback('sample',on_click)
    #cv2.waitKey(0)
    img[:,:,0]=np.where(img[:,:,0]==129.0,0,img[:,:,0])
    img[:,:,1]=np.where(img[:,:,1]==129.0,1,img[:,:,1])
    img[:,:,2]=np.where(img[:,:,2]==129.0,2,img[:,:,2])
    #pixel_checker(img)
    img2=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower=np.array([0,0,0],dtype='uint8')
    upper=np.array([28,28,28],dtype='uint8')
    #img2=cv2.inRange(img2,lower,upper)
    img2=cv2.inRange(img,lower,upper)
    img2=cv2.blur(img2,(2,2))
    ret,img2=cv2.threshold(img2,0,255,cv2.THRESH_BINARY)
    img2=cv2.bitwise_not(img2)
    #cv2.imwrite(f'{save_dir}/sample_output2.png',img2)
    pixel_checker(img2)
    contours, hierarchy = cv2.findContours(img2, cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for i in range(0, len(contours)):
        if len(contours[i]) > 0:
            if cv2.contourArea(contours[i]) < 500:
                continue
        rectangle = contours[i]
        x,y,w,h=cv2.boundingRect(rectangle)
        x_min,x_max = x,x+w
        y_min,y_max = y,y+h
        cv2.rectangle(img, (x_min,y_min),(x_max,y_max),(255,0,0),1)
    img[:,:,0]+=img_room[:,:,0]
    img[:,:,1]+=img_room[:,:,1]
    img[:,:,2]+=img_room[:,:,2]
    pixel_checker(img)
    for i in range(0, len(contours)):
        if len(contours[i]) > 0:
            if cv2.contourArea(contours[i]) < 500:
                continue
    #cv2.polylines(img, contours[i], True,(255,0,0),5)
    rectangle = contours[i]
    x,y,w,h=cv2.boundingRect(rectangle)
    direction=get_rotation(i)
    c_x=x+(w//2)
    c_y=y+(h//2)
    cropped_img = img[c_y-distance_h:c_y+distance_h,
                      c_x-distance_w:c_x+distance_w]
    cropped_img_shape = cropped_img.shape
    print('==============================================')
    print(f'coordinate: ({x},{y})')
    print(f'center: ({c_y},{c_x})')
    print(f'distance: ({distance_h}, {distance_w})')
    print(f'pixel values: {img[y+h//4:y+1+h//4,x+w//4:x+w//4+1][0][0]}')
    print(f'cropped img shape: {cropped_img_shape}')
    print('==============================================')
    if cropped_img_shape==rotations.shape:
        if int(c_y) != 256 and int(c_x) != 256:
            #img[c_y-distance_h:c_y+distance_h,
            #    c_x-distance_w:c_x+distance_w]+=rotations
            img[c_y-distance_h:c_y+distance_h,
                c_x-distance_w:c_x+distance_w]+=direction
    #cv2.imshow('sample',img[c_y-10:c_y+10,c_x-10:c_x+10])
    #cv2.waitKey(0)
    cv2.circle(img,(c_x,c_y),1,(0,255,0),2)
    pixel_checker(img)

if __name__ == '__main__':
    visualize_direction()
