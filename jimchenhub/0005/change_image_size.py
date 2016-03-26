#! /usr/bin/env python
#-*- encoding: utf-8 -*-

import cv2
import numpy as np

# static value for iphone 5
I5_WIDTH = 640.0
I5_HEIGHT = 1136.0
#get basic value for calculate zooming rate
img = cv2.imread("./head.jpg")
height, width = img.shape[0], img.shape[1]
zoomR = max(I5_WIDTH/width, I5_HEIGHT/height)
# resize the image
target = cv2.resize(img,(width/zoomR,height/zoomR),interpolation=cv2.INTER_CUBIC)
#save target image
cv2.imwrite("target.jpg", target)