import cv2
import numpy as np

kernel = np.ones((3, 3), np.uint8)
kernel1 = np.ones((3, 3), np.uint8)

img = cv2.imread('f:/Code/python/opencvproject/doro.jpg')
img = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
Blur = cv2.GaussianBlur(img, (15, 15), 10)#GaussianBlur(img, kernel, Standard Deviation)
Canny = cv2.Canny(img, 150, 200)
dilate = cv2.dilate(Canny, kernel, iterations = 1)
erode = cv2.erode(dilate, kernel1, iterations = 1)

cv2.imshow('img', img)
cv2.imshow('gray', gray)
cv2.imshow('Blur', Blur)
cv2.imshow('Canny', Canny)
cv2.imshow('dilate', dilate)
cv2.imshow('erode', erode)
cv2.waitKey(0)