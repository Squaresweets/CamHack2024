import pygame
import os
from var import *

class Line:
    def __init__(self, start_pos, end_pos, width=5):
        self.packed = (terminal_green, start_pos, end_pos, width)

class Face:
    def __init__(self, scale=1.0):
        self.scale = scale
        self.thickness = int(5 * self.scale)

        self.w, self.h = pygame.display.get_surface().get_size()

        self.face_border = (terminal_green, pygame.Rect(
            (self.w * 0.1 * self.scale, self.h * 0.1 * self.scale),
            (self.w * 0.8 * self.scale, self.h * 0.8 * self.scale)),
                            self.thickness)
        self.components = []

        self.state_map = {

        }
        self.closed()


    def smile(self):
        self.components = [
            Line( (int(self.w*0.15*self.scale), int(self.h*0.4*self.scale)), (int(self.w*0.2*self.scale), int(self.h*0.2*self.scale))),
            Line( (int(self.w*0.2*self.scale), int(self.h*0.2*self.scale)), (int(self.w*0.25*self.scale), int(self.h*0.4*self.scale))),
            Line( (int(self.w*0.75*self.scale), int(self.h*0.4*self.scale)), (int(self.w*0.8*self.scale), int(self.h*0.2*self.scale))),
            Line( (int(self.w*0.8*self.scale), int(self.h*0.2*self.scale)), (int(self.w*0.85*self.scale), int(self.h*0.4*self.scale))), #eyes

            Line( (int(self.w*0.2*self.scale), int(self.h*0.5*self.scale)), (int(self.w*0.3*self.scale), int(self.h*0.8*self.scale))),
            Line( (int(self.w*0.3*self.scale), int(self.h*0.8*self.scale)), (int(self.w*0.7*self.scale), int(self.h*0.8*self.scale))),
            Line( (int(self.w*0.7*self.scale), int(self.h*0.8*self.scale)), (int(self.w*0.8*self.scale), int(self.h*0.5*self.scale))),
            self.face_border
        ]

    def open(self):
        self.components = [
            Line( (int(self.w*0.15*self.scale), int(self.h*0.4*self.scale)), (int(self.w*0.2*self.scale), int(self.h*0.2*self.scale))),
            Line( (int(self.w*0.2*self.scale), int(self.h*0.2*self.scale)), (int(self.w*0.25*self.scale), int(self.h*0.4*self.scale))),
            Line( (int(self.w*0.75*self.scale), int(self.h*0.4*self.scale)), (int(self.w*0.8*self.scale), int(self.h*0.2*self.scale))),
            Line( (int(self.w*0.8*self.scale), int(self.h*0.2*self.scale)), (int(self.w*0.85*self.scale), int(self.h*0.4*self.scale))), #eyes
            Line( (int(self.w*0.2*self.scale), int(self.h*0.6*self.scale)), (int(self.w*0.3*self.scale), int(self.h*0.8*self.scale))),
            Line( (int(self.w*0.3*self.scale), int(self.h*0.8*self.scale)), (int(self.w*0.7*self.scale), int(self.h*0.8*self.scale))),
            Line( (int(self.w*0.7*self.scale), int(self.h*0.8*self.scale)), (int(self.w*0.8*self.scale), int(self.h*0.6*self.scale))),
            Line( (int(self.w*0.2*self.scale), int(self.h*0.6*self.scale)), (int(self.w*0.3*self.scale), int(self.h*0.4*self.scale))),
            Line( (int(self.w*0.3*self.scale), int(self.h*0.4*self.scale)), (int(self.w*0.7*self.scale), int(self.h*0.4*self.scale))),
            Line( (int(self.w*0.7*self.scale), int(self.h*0.4*self.scale)), (int(self.w*0.8*self.scale), int(self.h*0.6*self.scale))),
            self.face_border
        ]

    def half_open(self):
        self.components = [
            Line( (int(self.w*0.15*self.scale), int(self.h*0.4*self.scale)), (int(self.w*0.2*self.scale), int(self.h*0.2*self.scale))),
            Line( (int(self.w*0.2*self.scale), int(self.h*0.2*self.scale)), (int(self.w*0.25*self.scale), int(self.h*0.4*self.scale))),
            Line( (int(self.w*0.75*self.scale), int(self.h*0.4*self.scale)), (int(self.w*0.8*self.scale), int(self.h*0.2*self.scale))),
            Line( (int(self.w*0.8*self.scale), int(self.h*0.2*self.scale)), (int(self.w*0.85*self.scale), int(self.h*0.4*self.scale))), #eyes
            Line((int(self.w*0.2*self.scale), int(self.h*0.6*self.scale)), (int(self.w*0.3*self.scale), int(self.h*0.7*self.scale))),
            Line((int(self.w*0.3*self.scale), int(self.h*0.7*self.scale)), (int(self.w*0.7*self.scale), int(self.h*0.7*self.scale))),
            Line((int(self.w*0.7*self.scale), int(self.h*0.7*self.scale)), (int(self.w*0.8*self.scale), int(self.h*0.6*self.scale))),
            Line((int(self.w*0.2*self.scale), int(self.h*0.6*self.scale)), (int(self.w*0.3*self.scale), int(self.h*0.5*self.scale))),
            Line((int(self.w*0.3*self.scale), int(self.h*0.5*self.scale)), (int(self.w*0.7*self.scale), int(self.h*0.5*self.scale))),
            Line((int(self.w*0.7*self.scale), int(self.h*0.5*self.scale)), (int(self.w*0.8*self.scale), int(self.h*0.6*self.scale))),
            self.face_border
        ]

    def closed(self):
        self.components = [
            Line( (int(self.w*0.15*self.scale), int(self.h*0.4*self.scale)), (int(self.w*0.2*self.scale), int(self.h*0.2*self.scale))),
            Line( (int(self.w*0.2*self.scale), int(self.h*0.2*self.scale)), (int(self.w*0.25*self.scale), int(self.h*0.4*self.scale))),
            Line( (int(self.w*0.75*self.scale), int(self.h*0.4*self.scale)), (int(self.w*0.8*self.scale), int(self.h*0.2*self.scale))),
            Line( (int(self.w*0.8*self.scale), int(self.h*0.2*self.scale)), (int(self.w*0.85*self.scale), int(self.h*0.4*self.scale))), #eyes
            Line((int(self.w*0.2*self.scale), int(self.h*0.6*self.scale)), (int(self.w*0.8*self.scale), int(self.h*0.6*self.scale))),

            self.face_border
        ]

    def update(self, state):
        if state == "happy":
            self.closed()
        else:
            self.half_open()


    def draw(self,surface):
        for e in self.components:
            if type(e) == Line:
                pygame.draw.line(surface,*e.packed)
            else:
                pygame.draw.rect(surface,*e)

class Camera:
    def __init__(self):
        self.thickness = 5

        self.w, self.h = pygame.display.get_surface().get_size()

        self.components = [
            (terminal_green, pygame.Rect(
                                                        (self.w * 0.3 , self.h * 0.3), 
                                                        (self.w * 0.4 , self.h * 0.4)
                                                      ), self.thickness, 50),
            (terminal_green, pygame.Rect(
                                                        (self.w * 0.4 , self.h * 0.2), 
                                                        (self.w * 0.2 , self.h * 0.105)
                                                      ), self.thickness),
            (terminal_green, (self.w*0.5, self.h*0.5), self.w*0.1, self.thickness)
            

        ]
        self.is_visible = False

    def draw(self,surface):
            pygame.draw.rect(surface,*self.components[0])
            pygame.draw.rect(surface,*self.components[1])
            pygame.draw.circle(surface,*self.components[2])

class Text:
    def __init__(self, txt, size, rect, max_width):
        self.w, self.h = pygame.display.get_surface().get_size()
        self.font = pygame.font.SysFont('sfnsmono', size) # CHANGE LATER
        self.text = txt
        self.rect = rect
        self.max_width = max_width

    def draw(self, surface):
        # Split text by lines first
        raw_lines = self.text.split('\n')
        lines = []

        for raw_line in raw_lines:
            words = raw_line.split()
            current_line = []

            for word in words:
                current_line.append(word)
                # Check the width of the current line
                if self.font.size(' '.join(current_line))[0] > self.max_width:
                    current_line.pop()  # Remove the word that caused the overflow
                    lines.append(' '.join(current_line))  # Add the completed line
                    current_line = [word]  # Start a new line with the overflow word

            # Add any remaining words in the current line
            if current_line:
                lines.append(' '.join(current_line))

        # Draw the lines onto the surface
        y_offset = self.rect.top
        for line in lines:
            text_surface = self.font.render(line, True, terminal_green)
            text_width = text_surface.get_width()
            x_position = self.rect.left + (self.max_width - text_width) // 2 - self.max_width // 2  # Center the line
            surface.blit(text_surface, (x_position, y_offset))
            y_offset += self.font.get_linesize()

class Image:
    def __init__(self, path_to_image, width):
        self.image = pygame.image.load(os.path.join(os.getcwd(), path_to_image))
        self.image_rect = self.image.get_rect()
        self.image_rect.center = (SCREEN_WIDTH//2,SCREEN_HEIGHT//2)

    def draw(self,surface):
        surface.blit(self.image, self.image_rect)
