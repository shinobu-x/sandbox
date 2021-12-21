import cv2
import time
import numpy as np
import pyautogui
from hand_detector import HandDetector

frame_width=512
frame_height=512
frame_reduction=100
smoothing=8
previous_time=0
previous_x=0
previous_y=0
current_x=0
current_y=0
capture=cv2.VideoCapture(0)
detector=HandDetector(max_hands=1)
screen_width,screen_height=pyautogui.size()
while True:
    _,frame = capture.read()
    frame=detector.get_hands(frame)
    landmarks_list,bbox=detector.get_position(frame)
    if len(landmarks_list) > 0:
        x,y = landmarks_list[0][1:]
        fingers = detector.get_fingers()
        width = frame_width-frame_reduction
        height = frame_height-frame_reduction
        cv2.rectangle(frame,(frame_reduction,frame_reduction),(width,height),(0,0,255),2)
        if fingers[1] == 1 and fingers[2] == 0:
            x2 = np.interp(x,(frame_reduction,width),(0,screen_width))
            y2 = np.interp(y,(frame_reduction,height),(0, screen_height))
            current_x = previous_x+(x2-previous_x)/smoothing
            current_y = previous_y+(y2-previous_y)/smoothing
            pyautogui.moveTo(frame_width-current_x,current_y)
            cv2.circle(frame,(x,y),15,(255,0,255),cv2.FILLED)
            previous_x,previous_y=current_x,current_y
        if fingers[1]==1 and fingers[2]==1:
            length,frame,vertices=detector.get_distance(8,12,frame)
            if length < 30:
                cv2.circle(frame,(vertices[4], vertices[5]),15,(0,255,0),cv2.FILLED)
                pyautogui.click()
    current_time=time.time()
    fps=1/(current_time-previous_time)
    previous_time=current_time
    cv2.putText(frame,str(int(fps)),(20,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow('sample',frame)
    cv2.waitKey(1)
