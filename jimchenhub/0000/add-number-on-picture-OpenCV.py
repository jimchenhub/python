#-*- coding:utf8 -*-
import cv2
import numpy as np

img = cv2.imread("./head.jpg")
height, width = img.shape[0], img.shape[1]
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'4',(width - 40, 40), font, 1,(0, 0, 255),2)

cv2.imwrite("target.jpg", img)