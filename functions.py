import pygame


def Rect(dis, color, rect):
    pygame.draw.rect(dis, color, rect)
def Circle(dis, color, pos, radius):
    pygame.draw.circle(dis, color, pos, radius)
def line(dis, color, sta, end, width = 1):
    pygame.draw.line(dis, color, sta, end, width)

