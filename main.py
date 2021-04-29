import numpy as np
import cv2

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 0 = the numbers of your camera, i got one camera so he's name would be 0

face = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
Glasses = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")

while True:
    ret, frame = video.read()  # return the frame itself (so the video) and ret = if the capture work properly

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.3, 5)
    # (x,y) is the left corner of the camera; w is the width; h is the height
    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 4)
        cv2.putText(frame, "you hehe", (x + w, y - 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye.detectMultiScale(roi_gray, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 4)

            glasses = Glasses.detectMultiScale(roi_gray, 1.3, 5)
            for (gx, gy, gw, gh) in glasses:
                cv2.rectangle(roi_color, (gx, gy), (gx + gw, gy + gh), (255, 0, 0), 4)

    cv2.imshow('TEST', frame)
    if cv2.waitKey(1) == ord('q'):  # ord('q') represent the ASCII value of 'q'
        break
video.release()  # Now we stop the utilisation of the camera so other software can use it now (like OBS)
cv2.destroyAllWindows()
