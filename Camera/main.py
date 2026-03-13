import os
import cv2
import time
from emailing import send_email
import glob
from threading import Thread

video= cv2.VideoCapture(0)
time.sleep(1)
firstFrame = None
status_list = []
count=1

def clean_folder():
    print("cleaning folder started")
    images = glob.glob("images/*")
    for image in images:
        os.remove(image)
    print("cleaning folder finished")

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
            cv2.imwrite(f"images/{count}", frame)
            count = count + 1
        all_images = glob.glob("images/*.png")
        middle_image = int(len(all_images)/2)
        image_to_send = all_images[middle_image]
    status_list.append(status)
    status_list = status_list[-2:]
    if status_list[0] ==1 and status_list[1] == 0:
        email_thread = Thread(target = send_email,args = (image_to_send,))
        email_thread.daemon = True
        clean_thread = Thread(target = clean_folder)
        clean_thread.daemon = True
        email_thread.start()
    cv2.imshow('My video', frame)
    key = cv2.waitKey(1)



    if key == ord('q'):
        break
video.release()
clean_thread.start()

