import mediapipe as mp
import cv2
import streamlit as st
import numpy as np
from mediapipe.framework.formats import landmark_pb2
import tempfile


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(model_complexity=1)
        

video_cote = st.file_uploader("Vue de cote", type=["mp4", "avi", "mov"])


if st.button("Analyser", use_container_width=True):
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video_cote.read())

    cap = cv2.VideoCapture(tfile.name)

    global dataPx, enregistre

    # Tableau de stockage des données
    dataPx = np.ones((10,2))


    SideConnections = [[0,1],[2,3],[3,4],[2,5],[5,6],[6,7],[7,8],[8,9]]

    enregistre = []

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = float(cap.get(cv2.CAP_PROP_FPS))

    timing = 0
    delta = 1/fps
    im = 0

    while cap.isOpened():
        ret, image = cap.read()
        if not ret:
            break

        results = pose.process(image)

        if results.pose_landmarks:
            
            landmarks_subset = landmark_pb2.NormalizedLandmarkList(
                landmark = [
                results.pose_landmarks.landmark[0],
                results.pose_landmarks.landmark[7], 
                results.pose_landmarks.landmark[11],
                results.pose_landmarks.landmark[13],
                results.pose_landmarks.landmark[15],
                results.pose_landmarks.landmark[23],
                results.pose_landmarks.landmark[25],
                results.pose_landmarks.landmark[27],
                results.pose_landmarks.landmark[29],
                results.pose_landmarks.landmark[31],
                ])
        
            mp_drawing.draw_landmarks(image, landmarks_subset, SideConnections)

            for id, lm in enumerate(landmarks_subset.landmark):  
                # Coordonnées en x et y corrigées 
                Cx, Cy = int(lm.x*width), int(lm.y*height)
            
                dataPx[id] = [Cx, Cy]
            
        cv2.imshow('Video originale',image)
        cv2.waitKey(1)

        timing += delta




