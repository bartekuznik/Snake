import pygame
import random

class Food():
    def __init__(self):
        self.randx = random.randrange(0, 580, 20)
        self.randy = random.randrange(0, 580, 20)
        self.food_rect = pygame.Rect(self.randx, self.randy, 20,20)

    def draw(self, screen):
        pygame.draw.rect(screen, (0,255,0), self.food_rect ,0)