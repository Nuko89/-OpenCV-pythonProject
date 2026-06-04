import cv2

#cap = cv2.VideoCapture('UAV.mp4')#open mp4
cap = cv2.VideoCapture(0)#open computer camera #'0' is camera number

while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (0, 0), fx = 0.5, fy = 0.5)
        cv2.imshow('video', frame)
    else:
        break

    if cv2.waitKey(10) == ord('q'):#press 'q' to end video
        break