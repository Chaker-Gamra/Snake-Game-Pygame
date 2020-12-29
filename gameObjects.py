import pygame
import random


class Apple:
    def __init__(self):
        self.xPos = random.randint(0, 19) * 25
        self.yPos = random.randint(0, 19) * 25

    def render(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.xPos, self.yPos, 25, 25))

