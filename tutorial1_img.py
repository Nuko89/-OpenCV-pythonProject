import cv2

img = cv2.imread('doro.jpg')

#img = cv2.resize(img, (100, 100))#fix img size 100x100
img = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)#fix img size 0.5 width x0.5 height

cv2.imshow('img', img)
#cv2.waitKey(2000)#wait 2 sec
cv2.waitKey(0)#wait for forever