import pygame

from face_tracking.takeImage import TakeImage
from sprites import *
import time
import sys

class HelloScreen:
    def __init__(self):
        self.face = Face(1)
        self.components = []
        self.nextState = SmileScreen
        self.aiDescription = "***The user is now on the intro screen. After asking two or three questions say you are going to move on."

class SmileScreen:
    def __init__(self):
        self.face = Face(0.3)
        self.components = [Camera()]
        self.nextState = PhotoScreen
        self.aiDescription = "***The user is now on a screen with a camera in the middle. Tell them to smile in a funny way"

class PhotoScreen:
    def __init__(self):
        self.face = Face(0.3)
        # sort out the image
        print("TAKING PICTURE")
        TakeImage.get_faces()
        self.components = [Image("face_tracking/output.png",0.5), Text(TakeImage.lastEmotion, 30, pygame.Rect(SCREEN_WIDTH-200,SCREEN_HEIGHT*0.5,200,500),200)]
        self.nextState = ThanksScreen
        if TakeImage.lastEmotion == "":
            self.aiDescription = "***The user is now being shown the picture that was taken, unfortunatly no people were deteceted in the photo. Please say that you can't seen anyone in the photo but pretend that you are phsycic and make stuff up about them. Don't suggest that they should try again because that isn't possible"
        else:
            self.aiDescription = "***The user is now being shown the picture that was taken. Here is some info about their emotions: " + TakeImage.lastEmotion + " Please make up some stuff about them and what their ideal drink would be"

class ThanksScreen:
    def __init__(self):
        self.face = Face(1)
        self.components = []
        self.nextState = None
        self.aiDescription = "***This is the final screen, the drink you created is now being dispensed"
