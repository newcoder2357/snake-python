import pygame 
pygame.init()
import graphic
import random
import setting 
import login
import intro_game
import radio
import one_player
from option import *
from game_mode import *
from load_map import load_map
from display_number import draw_num
from functions import Rect, Circle, line
from time import sleep
from collections import defaultdict



dis = pygame.display.set_mode((setting.WIDTH, setting.HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption(setting.CAPTION)

clock.tick(60)

blue = (30,144,255)
red = (255,0,0)
slate_gray = (112,128,144)
saddle = (139,69,19)
black = (0, 0, 0)
white = (255, 255, 255)
tomato = (255,99,71)
aqua = (0,255,255)

Fence = load_map()

while True:
    Relax(dis, Fence)
    

#one_player.play(dis, Fence[0], "Duc")


pygame.quit()