import pygame
import pygame.transform
import graphic
import display_number
import radio
from random import randint
from controltime import Delay
from time import sleep


def show_score_relax(dis, Name, Score):
    dis.fill((0, 0, 0))
    myfont = pygame.font.Font(None, 200)
    fontname = pygame.font.Font(None, 150)
    fontpress = pygame.font.Font(None, 40)
    Name_img = myfont.render(Name, True, (0,255,255))
    score_img = fontname.render("Score : " + str(Score), True, (255, 255, 255))
    press_enter = fontpress.render("Press Enter to continue!!!", True, (119,136,153))

    radio.showratio1.play(-1)
    dis.blit(Name_img, ((1200 - Name_img.get_width()) // 2, 100))
    dis.blit(score_img, ((1200 - score_img.get_width()) // 2, 200 + Name_img.get_height()))
    dis.blit(press_enter, ((1200 - press_enter.get_width()) // 2,600))
    pygame.display.update()
    
    waiting = True 
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                radio.showratio1.stop()
                raise SystemExit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False
                    radio.showratio1.stop()




    

    




