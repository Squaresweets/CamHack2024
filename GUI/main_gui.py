
# Example file showing a basic pygame "game loop"
import pygame

from Intelligence.intellegence import aiChat
from Speech.speech import *
from sprites import *
from screens import *
from var import *
from enum import Enum
import re

# pygame setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

c = 0

currentScreen = HelloScreen()
aiChat.new_chat()
currentResponse = aiChat.send_message(currentScreen.aiDescription)
Listen.start_daemon()

currentlyTalking = True
textCounter = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    screen.fill((0,0,0))

    # Render the current screen
    if c == 120:
        currentScreen.face.update("sad")
        c = 0
    if c == 60:
        currentScreen.face.update("happy")
    currentScreen.face.draw(screen)
    for x in currentScreen.components:
        x.draw(screen)

    # Sort out the ai and the caption text:
    if not currentlyTalking:
        if Listen.currentState == 0:
            Listen.currentState = 1
        elif Listen.currentState == 2:
            Listen.currentState = 0
            currentResponse = aiChat.send_message(Listen.lastInput)
            if "***" in currentResponse:
                currentResponse = " "
            textCounter = 0
            currentlyTalking = True
    else:
        textCounter += 1
        if textCounter >= len(currentResponse) + (0 if '?' in currentResponse else 100) and not currentScreen.nextState is None:
            currentlyTalking = False
            if not '?' in currentResponse:
                currentScreen = currentScreen.nextState()
                currentResponse = aiChat.send_message(currentScreen.aiDescription)
                textCounter = 0
                currentlyTalking = True
    Text(currentResponse[0:textCounter],50, pygame.Rect(SCREEN_WIDTH/2,SCREEN_HEIGHT*0.75,1400,00),1400).draw(screen)
    if Listen.currentState == 1:
        Text("Listening...", 60, pygame.Rect(SCREEN_WIDTH/2,20,700,200),700).draw(screen)
    else:
        Text(Listen.lastInput, 60, pygame.Rect(SCREEN_WIDTH/2,20,700,200),700).draw(screen)

    pygame.display.flip()

    clock.tick(60)
    c += 1

pygame.quit()
