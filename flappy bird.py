import pygame,random
from pygame import *
pygame.init
Clock = pygame.time.Clock()
screen = pygame.display.set_mode((500,500))

bl_rand = random.randint(0,11)
block1_move = 400
block2_move = 400

value = 255
gravity = 0
run =  True

while run:
   
    class player:
        def __init__(self):
            global value
            self.playerd = pygame.image.load("player.png")
            self.recte = self.playerd.get_rect()
            self.recte.y = value


        def gravity_and_out_of_bounds(self):
            global gravity,value

            gravity += 0.5
            value += gravity

            if self.recte.y > 500 or self.recte.y < 0:
                self.recte.y = 255

        def drawing(self):
            screen.blit(self.playerd,(230,self.recte.y))
            print(gravity)

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
    Player = player()
    Player.drawing()
    Player.gravity_and_out_of_bounds()

    Block = block_obstical()
    Block.drawing()
    Block.moving()
    Block.respawn()

    pygame.display.flip()
    Clock.tick(60)
    
    