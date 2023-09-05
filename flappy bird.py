import pygame,random
from pygame import *
import time
pygame.init
Clock = pygame.time.Clock()
screen = pygame.display.set_mode((500,500))


playerd = pygame.image.load("player.png")
bl_rand = random.randint(0,11)
block1_move = 400
block2_move = 400

playerd_y = 255
gravity = 0
run =  True

while run:
    
    class player:
        def drawing():
            global playerd
            
            screen.blit(playerd,(230,playerd_y))
        def gravity_and_out_of_bounds():
            global playerd_y,gravity

            gravity += 0.5
            playerd_y += gravity

            if playerd_y > 500 or playerd_y < 0:
                playerd_y = 255

    class block_obstical:
        def __init__(self):
            self.y = [255,400,300,255,400,300,255,400,300,255,400,300]
            self.y2 = [-350,-200,-300,-350,-200,-300,-350,-200,-300,-350,-200,-300]
            self.rect_list = [pygame.Rect((block1_move,self.y[bl_rand]),(100,400)),pygame.Rect((block2_move,self.y2[bl_rand]),(100,400))]
            self.color = [(0,0,255),(0,0,0)]
            self.colra_var = 0

        def drawing(self):
            for rect in self.rect_list:
                pygame.draw.rect(screen,self.color[self.colra_var],rect,0)
                self.colra_var += 1
                

        @staticmethod
        def moving():
            global block2_move,block1_move
            block1_move -= 2
            block2_move -= 2
        @staticmethod
        def respawn():
            global block2_move,block1_move,bl_rand
            if block1_move == -100:
                block1_move = 600
                block2_move = 600
                bl_rand = random.randint(0,2)
                print(bl_rand)
                
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key ==  pygame.K_SPACE:
                gravity -= 20
        if event.type == pygame.QUIT:
            run = False
        

    screen.fill((255,255,255))
    Player = player
    Player.drawing()
    Player.gravity_and_out_of_bounds()

    Block = block_obstical()
    Block.drawing()
    Block.moving()
    Block.respawn()
    
    pygame.display.flip()
    Clock.tick(60)
    