import pygame,random
from pygame import *
import time
pygame.init
Clock = pygame.time.Clock()
screen = pygame.display.set_mode((500,500))


playerd = pygame.image.load("player.png")

blocks_rand = random.randint(-300,0)
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

            self.rect_list = [pygame.Rect((block1_move,-200),(100,400)),pygame.Rect((block2_move,400),(100,400))]

        def drawing(self):
            for rect in self.rect_list:
                pygame.draw.rect(screen,(0,0,255),rect,0)

        @staticmethod
        def moving():
            global block2_move,block1_move
            block1_move -= 2
            block2_move -= 2
        @staticmethod
        def respawn():
            global block2_move,block1_move
            if block1_move == -100:
                block1_move = 600
                block2_move = 600

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
