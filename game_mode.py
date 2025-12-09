from typing import ChainMap
import pygame
import login
import one_player
import intro_game
import radio
from option import *
import two_players

blue = (30,144,255)
red = (255,0,0)
white = (255, 255, 255)
pink = (255,20,147)



    

def Relax(dis, Fence):
    Name = login.login(dis, "Enter Nick Name 1", (255, 255, 255))
    # Name2 = login.login(dis, "Enter Nick Name 2", (255, 255, 255))
    Id_map = selec_map(dis)
    one_player.play(dis, Fence[Id_map - 1], Name)
    # intro_game.show_score_relax(dis, Name, Score)



