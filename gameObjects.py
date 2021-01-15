import pygame
import random


class Apple:
    def __init__(self):
        self.xPos = random.randint(0, 19) * 25
        self.yPos = random.randint(0, 19) * 25

    def update_position(self):
        self.xPos = random.randint(0, 19) * 25
        self.yPos = random.randint(0, 19) * 25

    def render(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.xPos, self.yPos, 25, 25))


class Snake:
    def __init__(self, xPos, yPos):
        self.head = (xPos, yPos)
        self.body = [self.head]
        self.motion = [1, 0]
        self.score = 0

    def hit_itself(self):
        for i in range(len(self.body) - 1):
            if self.head == self.body[i]:
                return True

        return False

    def update(self, apple):
        if self.head[0] == apple.xPos and self.head[1] == apple.yPos:
            apple.update_position()
            pygame.mixer.Sound("eat_apple.mp3").play()
            self.score += 1
        else:
            self.body.pop(0)

        x = self.head[0] + self.motion[0]*25
        y = self.head[1] + self.motion[1]*25

        if x == 500:
            x = 0
        elif x < 0:
            x = 475
        if y == 500:
            y = 0
        elif y < 0:
            y = 475

        new_head = (x, y)
        self.body.append(new_head)
        self.head = new_head

    def render(self, screen):
        i = 1
        for chunk in self.body:
            if i == len(self.body):
                pygame.draw.rect(screen, (0, 0, 0), (chunk[0], chunk[1], 25, 25))
            else:
                pygame.draw.rect(screen, (255, 255, 0), (chunk[0], chunk[1], 25, 25))
            i += 1







