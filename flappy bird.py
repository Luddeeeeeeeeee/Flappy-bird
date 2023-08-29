import pygame
from pygame import *
import time
pygame.init
Clock = pygame.time.Clock()
screen = pygame.display.set_mode((500,500))


playerd = pygame.image.load("player.png")
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


            
            


    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key ==  pygame.K_SPACE:
                gravity -= 10
        if event.type == pygame.QUIT:
            run = False



    screen.fill((255,255,255))
    Player = player
    Player.drawing()
    Player.gravity()
    pygame.display.flip()
    Clock.tick(60)