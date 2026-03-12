import cv2
import time
from emailing import send_email

video= cv2.VideoCapture(0)
time.sleep(1)
firstFrame = None
status_list = []

while True:
    status=0
    check, frame = video.read()
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey_frame_Gau = cv2.GaussianBlur(grey_frame, (21, 21), 0)

    if firstFrame is None:
        firstFrame = grey_frame_Gau

    delta_frame = cv2.absdiff(firstFrame, grey_frame_Gau)

    thresh_frame =  cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    cv2.imshow('My video', dil_frame)

    contours,check = cv2.findContours(dil_frame, cv2.RETR_TREE,
                                      cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        x,y,w,h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        if rectangle.any():
            status =1
    status_list.append(status)
    status_list = status_list[-2:]
    if status_list[0] ==1 and status_list[1] == 0:
        send_email()
    cv2.imshow('My video', frame)
    key = cv2.waitKey(1)



    if key == ord('q'):
        break
video.release()

