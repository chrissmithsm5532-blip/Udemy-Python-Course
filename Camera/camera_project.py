import cv2
import streamlit as st
from datetime import datetime

st.title("Motion Detector")
start = st.button("Start Camera")

if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = camera.read()
        framc = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        day = datetime.now().strftime("%A")
        time = datetime.now().strftime("%H:%M:%S")

        cv2.ptText(img=frame,text=day,org=(30,80),
                   fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=3,
                   color=(255,255,255),
                   thickness=2,lineType=cv2.LINE_AA)
        cv2.ptText(img=frame, text=time, org=(30, 140),
                   fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=3,
                   color=(255, 0, 0),
                   thickness=2, lineType=cv2.LINE_AA)

        streamlit_image.image(frame)