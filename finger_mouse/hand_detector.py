import cv2
import mediapipe as mp
import time
import math
import numpy as np

class HandDetector():
    def __init__(self,mode=False,max_hands=2,detection_confidence=0.5,tracking_confidence=0.5):
        self.mode=mode
        self.max_hands=max_hands
        self.detection_confidence=detection_confidence
        self.tracking_confidence=tracking_confidence
        self.solution_hands=mp.solutions.hands
        self.hands=self.solution_hands.Hands()
        self.solution_drawing=mp.solutions.drawing_utils
        self.ids=[4,8,12,16,20]

    def get_hands(self,frame,draw=True):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(frame)
        if self.results.multi_hand_landmarks:
            for hand_lms in self.results.multi_hand_landmarks:
                if draw:
                    self.solution_drawing.draw_landmarks(frame,hand_lms,self.solution_hands.HAND_CONNECTIONS)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        return frame

    def get_position(self, frame, hands=0, draw=True):
        x_list = []
        y_list = []
        bbox = []
        bbox_size = 20
        self.landmarks_list = []
        if self.results.multi_hand_landmarks:
            hand = self.results.multi_hand_landmarks[hands]
            for id, landmark in enumerate(hand.landmark):
                h,w,c=frame.shape
                x=int(landmark.x*w)
                y=int(landmark.y*h)
                x_list.append(x)
                y_list.append(y)
                self.landmarks_list.append([id,x,y])
                if draw: cv2.circle(frame,(x,y),5,(0,128,128),cv2.FILLED)
            x_min = min(x_list)
            x_max = max(x_list)
            y_min = min(y_list)
            y_max = max(y_list)
            bbox=x_min,y_min,x_max,y_max
            if draw: cv2.rectangle(frame, (bbox[0]-bbox_size,bbox[1]-bbox_size),(bbox[2]+bbox_size,bbox[3]+bbox_size),(0,128,128),2)
        return self.landmarks_list,bbox

    def get_fingers(self):
        fingers = []
        if self.landmarks_list[self.ids[0]][1] > self.landmarks_list[self.ids[0]-1][1]:
            fingers.append(1)
        else: fingers.append(0)
        for id in range(1,5):
            if self.landmarks_list[self.ids[id]][2] < self.landmarks_list[self.ids[id]-2][2]:
                fingers.append(1)
            else: fingers.append(0)
        return fingers

    def get_distance(self,p1,p2,frame,draw=True,r=15,t=3):
        x1=self.landmarks_list[p1][1]
        y1=self.landmarks_list[p1][2]
        x2=self.landmarks_list[p2][1]
        y2=self.landmarks_list[p2][2]
        x=(x1+x2)//2
        y=(y1+y2)//2
        if draw:
            cv2.line(frame,(x1,y1),(x2,y2),(255,0,255),t)
            cv2.circle(frame,(x1,y1),r,(255,0,255),cv2.FILLED)
            cv2.circle(frame,(x2,y2),r,(255,0,255),cv2.FILLED)
            cv2.circle(frame,(x,y),r,(0,0,255),cv2.FILLED)
        length=math.hypot(x2-x1,y2-y1)
        return length,frame,[x1,y1,x2,y2,x,y]

def detect_and_track():
    previous_time=0
    current_time=0
    capture=cv2.VideoCapture(0)
    detector=HandDetector()
    while True:
        _,frame=capture.read()
        frame=detector.get_hands(frame)
        landmarks_list,bbox=detector.get_position(frame)
        if len(landmarks_list)!=0:
            print(landmarks_list[4])
        current_time=time.time()
        fps=1/(current_time-previous_time)
        previous_time=current_time
        cv2.putText(frame,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,255),3)
        cv2.imshow('image',frame)
        cv2.waitKey(1)

if __name__ == '__main__':
    detect_and_track()
