import pygame
import sys
import random
from snake import *
from food import *
from functions import *

pygame.init()

screen_width = 600
screen_height = 600

cell_size = 20

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

text_font = pygame.font.Font('font/123.ttf', 50)

snake = Sanke(screen_width, screen_height, cell_size)
food = Food()
isActive = False
score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if isActive:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake.isRight != True:
                    snake.isRight = False
                    snake.isLeft = True
                    snake.isUp = False
                    snake.isDown = False
                elif event.key == pygame.K_RIGHT and snake.isLeft != True:
                    snake.isRight = True
                    snake.isLeft = False
                    snake.isUp = False
                    snake.isDown = False
                elif event.key == pygame.K_UP and snake.isDown != True:
                    snake.isRight = False
                    snake.isLeft = False
                    snake.isUp = True
                    snake.isDown = False
                elif event.key == pygame.K_DOWN and snake.isUp != True:
                    snake.isRight = False
                    snake.isLeft = False
                    snake.isUp = False
                    snake.isDown = True
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    isActive = True

    if isActive:
        screen.fill('black')   
        food.draw(screen)
        snake.draw(screen, cell_size)
        #snake.snake_list = snake.snake_list[:-1]
        #snake.move()
        if check_collision(snake,food): #normalnie wywołuję funkcję jednoczesnie sprawdzając czy zwróci true, wtedy podbijam score
            score+=1
        else:
            snake.snake_list = snake.snake_list[:-1]
        snake.move(cell_size)

        display_score(screen, score, text_font)
        isActive = set_boundries(snake)
    else:
        starting_screen(screen,  text_font, snake, screen_width, screen_height, cell_size)

        

    pygame.display.update()
    clock.tick(5)