import pygame
import random

def starting_screen(screen, text_font, snake, screen_width, screen_height, cell_size):
    screen.fill('black')
    top_text = text_font.render('Snake game',False,'green')
    top_text_rect = top_text.get_rect(center=(300, 100))

    bottom_text = text_font.render('Press "Space" to run!',False,'green')
    bottom_text_rect = bottom_text.get_rect(center = (300, 500))

    screen.blit(top_text, top_text_rect)
    screen.blit(bottom_text, bottom_text_rect)
    snake.__init__(screen_width, screen_height, cell_size) #za każdym wywołaniem inicjalizuje snake od nowa

def display_score(screen, score, text_font):
    score_text = text_font.render('Score: ' + str(score), False,'blue')
    score_text_rect = score_text.get_rect(center = (300,50))

    screen.blit(score_text, score_text_rect)

def set_boundries(snake):
    if snake.snake_list[0][0]== -20 or snake.snake_list[0][1]== -20 or snake.snake_list[0][0]== 600 or snake.snake_list[0][1]== 600:
        return False
    elif snake.snake_list[0] in snake.snake_list[1:]: #sprawdzenie czy koordynaty head == z koordynatami jakiegoś innego segmentu
        return False
    else:
        return True
    
def check_collision(snake, food):
    if snake.snake_list[0][0] == food.randx and snake.snake_list[0][1] == food.randy:
        food.randx = random.randrange(0,580,20)
        food.randy = random.randrange(0,580,20)
        food.food_rect = pygame.Rect(food.randx, food.randy, 20,20)

        #snake.move()
        return True