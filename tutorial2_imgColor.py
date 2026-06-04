import cv2
import numpy as np
import random

#img = cv2.imread('doro.jpg')
#print(img.shape)
#B G R

img = np.empty((300, 300, 3), np.uint8)#create array

for row in range(300):
    for col in range(300):
        #img[row][col] = [0, 255, 0]#green
        img[row][col] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

cv2.imshow('img', img)
cv2.waitKey(0)