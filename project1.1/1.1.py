# -*- coding:utf-8 -*-
"""
created on 2020/11/17 8:18
@author WangChenghua
"""
import cv2
import numpy as np
img = cv2.imread("project1.1/huang.jpg")
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
buffer = cv2.waitKey(0) & 0xFF
if buffer == 27:
    cv2.destroyWindow(img)
elif buffer == ord('s'):
    cv2.imwrite("project1.1/new_huang.jpg", img)
    cv2.destroyWindow(img)
