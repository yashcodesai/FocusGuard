import cv2
import numpy as np

def detect_focus(frame):
    height, width, _ = frame.shape
    center_x, center_y = width // 2, height // 2

    # Simulated logic: If face is near center, assume focused
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face_center_x = x + w // 2
        face_center_y = y + h // 2
        if abs(face_center_x - center_x) < width * 0.2 and abs(face_center_y - center_y) < height * 0.2:
            return True
    return False