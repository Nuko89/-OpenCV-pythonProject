import cv2
import numpy as np

cap = cv2.VideoCapture(0)#open computer camera #'0' is camera number

#blue orange
penColorHSV = [[109, 113, 137, 118, 255, 255]]#,
               #[  4,  18, 117, 190, 179, 227]]

penColorBGR = [[255, 0, 0],
               [0, 255, 0],
               [0, 0, 255]]

#[x, y, colorID]
drawPoints = []

def findContour(img):
    countours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)#抓出圖形

    x, y, w, h = -1, -1, -1, -1
    for cnt in countours:
        #cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 4)#畫出圖形框
        area = cv2.contourArea(cnt)#算每個圖形面積

        if area > 500:
            peri = cv2.arcLength(cnt, True);#算每個圖形邊長
            vertices = cv2.approxPolyDP(cnt, peri * 0.02, True)#算每個圖形頂點
            x, y, w, h = cv2.boundingRect(vertices)#框出圖形

    return x + w // 2, y

def findPen(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for i in range(len(penColorHSV)):
        lower = np.array(penColorHSV[i][ :3])
        upper = np.array(penColorHSV[i][3:6])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    penX, penY = findContour(mask)
    cv2.circle(imgContour, (penX, penY), 10, penColorBGR[i], cv2.FILLED)#畫點

    #畫線
    if penY != -1:
        drawPoints.append([penX, penY, i])

    #cv2.imshow('result', result)

def draw(drawpoints):
    for point in drawpoints:
        cv2.circle(imgContour, (point[0], point[1]), 10, penColorBGR[point[2]], cv2.FILLED)#畫點

while True:
    ret, frame = cap.read()
    if ret:
        imgContour = frame.copy()
        cv2.imshow('video', frame)
        findPen(frame)
        draw(drawPoints)
        cv2.imshow('Contour', imgContour)
    else:
        break

    if cv2.waitKey(10) == ord('q'):#press 'q' to end video
        break