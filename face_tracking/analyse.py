import cv2

import matplotlib.pyplot as plt

import dlib

import numpy as np

from transformers import pipeline

from PIL import Image

def analyse(pic):
    image = cv2.imread(pic)


    # convert image to RGB colour
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image_pil = Image.fromarray(image_rgb)
    # image_pil.save("output.jpg")

    # plot image with matplotlib package
    plt.imshow(image_rgb)

    # create a copy of the cropped image to be used later
    image_template = image_rgb.copy()

    # convert image to Grayscale
    image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)
    
    detector = dlib.get_frontal_face_detector()

    # Detect faces using the haarcascade classifier on the "grayscale image"
    faces = detector(image_gray, 1)

    # Print coordinates of detected faces
    print("Faces:\n", faces)


    landmark_detector = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    for face in faces:

        x = face.left()
        y = face.top()
        x1 = face.right()
        y1 = face.bottom()
        cv2.rectangle(image_template, (x, y), (x1, y1), (0, 0, 255), 2)

        landmarks = landmark_detector(image_gray, face)
        
        # Get coordinates of each landmark point
        points = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(68)]
        
        # Draw circles at each landmark
        for (x, y) in points:
            cv2.circle(image_rgb, (x, y), 2, (255, 255, 255), -1)

        for i in range(67):
            cv2.line(image_rgb, points[i], points[i+1], (255, 255, 255), 1)


    classifier = pipeline('image-classification', model='dima806/facial_emotions_image_detection')
    emotion = classifier(image_pil)[0]['label']


    return emotion, image_rgb

