import pygame,random
from pygame import *
import time
pygame.init
Clock = pygame.time.Clock()
screen = pygame.display.set_mode((500,500))


playerd = pygame.image.load("player.png")
block_1 = pygame.image.load("Block.png")
block_1_x = 400

playerd_x = 230
playerd_y = 255
gravity = 0
run =  True

while run:
    class player:
        def drawing():
            global playerd
            
            screen.blit(playerd,(playerd_x,playerd_y))
        def gravity():
            global playerd_y,gravity
            
            
            gravity += 0.5
            playerd_y += gravity


            
    class block_obstical:
        def drawing():
            block_1_y = 0
            screen.blit(block_1,(block_1_x, block_1_y))
        def moving():
            global block_1_x
            block_1_x -= 1


    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key ==  pygame.K_SPACE:
                gravity -= 20
        if event.type == pygame.QUIT:
            run = False



    screen.fill((255,255,255))
    Player = player
    Player.drawing()
    Player.gravity()
    Block = block_obstical
    Block.drawing()
    Block.moving()
    pygame.display.flip()
    Clock.tick(60)