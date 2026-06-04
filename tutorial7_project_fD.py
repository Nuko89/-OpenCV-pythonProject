import cv2
faceCascade = cv2.CascadeClassifier('faceDetect.xml')

cap = cv2.VideoCapture(0)#open computer camera #'0' is camera number

while True:
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faceRect = faceCascade.detectMultiScale(gray, 1.1, 3)

        face_count = len(faceRect)
        text = f"Faces: {face_count}"

        cv2.putText(frame, text, (5, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))

        for (x, y, w, h) in faceRect:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('video', frame)
    else:
        break

    if cv2.waitKey(10) == ord('q'):#press 'q' to end video
        break
