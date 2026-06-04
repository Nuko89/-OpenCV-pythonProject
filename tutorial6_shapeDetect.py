import cv2

img = cv2.imread('image.png')
imgContour = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
Canny = cv2.Canny(gray, 100, 200)
countours, hierarchy = cv2.findContours(Canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)#抓出圖形

for cnt in countours:
    #print(cnt)
    cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 4)
    area = cv2.contourArea(cnt)#算每個圖形面積
    #print(area)

    if area > 500:
        peri = cv2.arcLength(cnt, True);#算每個圖形邊長
        vertices = cv2.approxPolyDP(cnt, peri * 0.02, True)#算每個圖形頂點
        corners = len(vertices)#算每個圖形頂點
        x, y, w, h = cv2.boundingRect(vertices)#框出圖形
        cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 4)#畫方形(導入框框數值)
        if corners == 3:
            cv2.putText(imgContour, 'triangle', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
        elif corners == 4:
            cv2.putText(imgContour, 'retriangle', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
        elif corners == 5:
            cv2.putText(imgContour, 'pentagon', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
        elif corners > 5:
            cv2.putText(imgContour, 'circle', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))

cv2.imshow('img', img)
cv2.imshow('Canny', Canny)
cv2.imshow('imgCountour', imgContour)
cv2.waitKey(0)
