import pygame

class Sanke():
    def __init__(self, screen_width, screen_height, cell_size):
        self.snake_list = [[int(screen_width/2), int(screen_height/2 )]]
        self.snake_list.append([int(screen_width/2) + cell_size, int(screen_height/2 )])
        self.snake_list.append([int(screen_width/2) + 2 * cell_size, int(screen_height/2 )])
        self.isRight = False
        self.isLeft = False
        self.isUp = True
        self.isDown = False

    def draw(self, screen, cell_size):
        for i in range(len(self.snake_list)):
            pygame.draw.rect(screen, (255,0,0), (self.snake_list[i][0], self.snake_list[i][1], cell_size, cell_size), 0)
    
    def move(self, cell_size):
        if(self.isLeft):
            val1 = self.snake_list[0][0] - cell_size
            val2 = self.snake_list[0][1] 
            self.snake_list.insert(0,[val1, val2])
        elif(self.isRight):
            val1 = self.snake_list[0][0] + cell_size
            val2 = self.snake_list[0][1] 
            self.snake_list.insert(0,[val1, val2])
        elif(self.isUp):
            val1 = self.snake_list[0][0]
            val2 = self.snake_list[0][1] - cell_size
            self.snake_list.insert(0,[val1, val2])
        elif(self.isDown):
            val1 = self.snake_list[0][0]
            val2 = self.snake_list[0][1] + cell_size
            self.snake_list.insert(0,[val1, val2])
