#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 11:45:26 2018

@author: suffiyan
"""


import cv2
from matplotlib import pyplot as plt
import pytesseract
from PIL import Image
img=cv2.imread('/home/suffiyan/Desktop/project.jpg',1)#read the input image 
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#convert it in to gray scale
print(gray.size)
print(gray.shape)



resize=cv2.resize(gray,(400,400))
imgplot=plt.imshow(resize)

ret,thresh1=cv2.threshold(resize,127,255,cv2.THRESH_BINARY)#threshold the image to remove background
imgplot=plt.imshow(thresh1)

text=(pytesseract.image_to_string(Image.fromarray(thresh1)))
print(text)



