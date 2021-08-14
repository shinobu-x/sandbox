import numpy as np
import cv2
import scipy.stats as sstats
import matplotlib.pyplot as plt

def func2(luv):
    l, u, v = cv2.split(luv)
    mode_l = sstats.mode(l[l.nonzero()])[0][0]
    mode_u = sstats.mode(u[l.nonzero()])[0][0]
    mode_v = sstats.mode(v[l.nonzero()])[0][0]
    mode = np.array([mode_l, mode_u, mode_v], dtype=int)
    a = (mode - luv)**2
    b = 0.*a[:, :, 0] + a[:, :, 1] +  a[:, :, 2]
    c = (b >= 9).astype(np.uint8)
    cs = np.stack([c] * 3, axis=2)
    luv = luv * cs
    return luv

## 前景切り抜き
img = cv2.imread('image/neko.png')
luv = cv2.cvtColor(img, cv2.COLOR_BGR2Luv)
luvk = func2(luv)
neko = cv2.cvtColor(luvk, cv2.COLOR_Luv2BGR)
cv2.imwrite("results/neko.png",neko)
rgb = neko[:, :, [2, 1, 0]]
#cv2.imshow('neko',neko)
#cv2.waitKey(0)

## Mask掛け
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
bin_img = cv2.inRange(hsv, (0, 10, 0), (255, 255, 255))
#bin_img = ~cv2.inRange(hsv, (62, 100, 0), (79, 255, 255))
#contours, _ = \
#        cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours, _ = \
        cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#cv2.imshow('image', bin_img)
#cv2.waitKey(0)
# 輪郭抽出
contours, _ = cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour = max(contours, key=lambda x: cv2.contourArea(x))
mask = np.zeros_like(bin_img)
cv2.drawContours(mask, [contour], -1, color = 255, thickness = -1)
cv2.imwrite('results/masked.png', mask)
cv2.imshow('mask', mask)
cv2.waitKey(0)
