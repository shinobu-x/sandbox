import cv2
import numpy as np

class Box:
    def __init__(self, x, y, w, h):
        self.box = []
        self.box.append([x,y,w,h])

    def __getitem__(self,i):
        return self.box[i]

def boxing(image, boxes, color, alpha):
    image = image.copy()
    for box in boxes:
        overlay = image.copy()
        p1 = (int(box[0]), int(box[1]))
        p2 = (int(box[0]+box[2]), int(box[1]+box[3]))
        cv2.rectangle(overlay, p1, p2, color, -1)
        image = cv2.addWeighted(image, alpha, overlay, 1-alpha, 0)
    cv2.imshow('img', image)
    cv2.waitKey()
image = cv2.imread('./neko.jpeg',
                   cv2.IMREAD_IGNORE_ORIENTATION|cv2.IMREAD_COLOR)

boxes = Box(30, 60, 100, 100)
boxing(image, boxes, (255,0,0), 0.5)
