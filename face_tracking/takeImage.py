import cv2

# used to plot our images
import matplotlib.pyplot as plt

import dlib

import numpy as np

from transformers import pipeline

from PIL import Image

class TakeImage:
    lastEmotion = ""
    def __init__(self):
        pass
    @staticmethod
    def get_faces():
        cam_port = 0
        cam = cv2.VideoCapture(cam_port)

        # reading the input using the camera
        result, image = cam.read()

        # convert image to RGB colour
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        image_pil = Image.fromarray(image_rgb)

        # convert image to Grayscale
        image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)

        detector = dlib.get_frontal_face_detector()

        # Detect faces using the haarcascade classifier on the "grayscale image"
        faces = detector(image_gray, 1)

        # Print coordinates of detected faces
        print("Faces:\n", faces)

        landmark_detector = dlib.shape_predictor("face_tracking/shape_predictor_68_face_landmarks.dat")

        for face in faces:
            landmarks = landmark_detector(image_gray, face)

            # Get coordinates of each landmark point
            points = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(68)]

            # Draw circles at each landmark
            for (x, y) in points:
                cv2.circle(image_rgb, (x, y), 2, (0, 255, 0), -1)

            for i in range(67):
                cv2.line(image_rgb, points[i], points[i+1], (0, 255, 0), 1)


        classifier = pipeline('image-classification', model='dima806/facial_emotions_image_detection')
        if len(faces) == 0:
            TakeImage.lastEmotion = ""
        else:
            TakeImage.lastEmotion = "\n".join(f"{item['label'].capitalize()}: {item['score']:.5f}\n" for item in classifier(image_pil))

        plt.imshow(image_rgb)

        plt.axis("off")
        plt.savefig("face_tracking/output.png", bbox_inches='tight', pad_inches=0)