from pygame import font
import pygame.display 
import graphic
import random
import setting 
import login
import radio
import display_number
from functions import Rect, Circle, line
from time import sleep
from collections import defaultdict


fhead = defaultdict(lambda: None)
ftail = defaultdict(lambda: None)
fbody = defaultdict(int)

fhead[(0, -1)], fhead[(0, 1)], fhead[(-1, 0)], fhead[(1, 0)] = 0, 1, 2, 3
ftail[(0, -1)], ftail[(0, 1)], ftail[(-1, 0)], ftail[(1, 0)] = 0, 1, 2, 3
fbody[(1, 0, 0, 1)], fbody[(0, 1, 1, 0)], fbody[(0, 1, -1, 0)], fbody[(-1, 0, 0, 1)], fbody[(1, 0, 0, -1)], fbody[(0, -1, 1, 0)], fbody[(-1, 0, 0, -1)], fbody[(0, -1, -1, 0)], fbody[(1, 0, -1, 0)], fbody[(-1, 0, 1,0)], fbody[(0, -1, 0, 1)], fbody[(0, 1, 0, -1)] = 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5



blue = (30,144,255)
red = (255,0,0)
slate_gray = (112,128,144)
saddle = (139,69,19)
black = (0, 0, 0)
white = (255, 255, 255)
tomato = (255,99,71)
aqua = (0,255,255)


delta = [[0, -1], [0, 1], [-1, 0], [1, 0]]
cell = 20

init_snakes = [ [[1, 33], [1, 32], [1, 31]], [[58, 33], [58, 32], [58, 31]]]

Font_name = pygame.font.Font(None, 80)
def prepare_nickname(Name):
    global img_name
    img_name = Font_name.render(Name, True, (255, 255, 255))


def draw_snake(dis, snakes, Body, Head, Tail):
    cell = 20
    global fhead, ftail, fbody
    for i in range(len(snakes)):
        snake = snakes[i]
        if i == 0:
            dx, dy = snake[0] - snakes[1][0], snake[1] - snakes[1][1]
            dis.blit(Tail[ftail[(dx, dy)]], (snake[0] * cell, snake[1] * cell))
        if i == len(snakes) - 1:
            tmp_id = len(snakes) - 2
            dx, dy = snake[0] - snakes[tmp_id][0], snake[1] - snakes[tmp_id][1]
            dis.blit(Head[fhead[(dx, dy)]], (snake[0] * cell, snake[1] * cell))

        if 0 < i < len(snakes) - 1:
            last, nxt = i - 1, i + 1
            d1x, d1y, d2x, d2y = snake[0] - snakes[last][0], snake[1] - snakes[last][1], snake[0] - snakes[nxt][0], snake[1] - snakes[nxt][1]
            dis.blit(Body[fbody[(d1x, d1y, d2x, d2y)]], (snake[0] * cell, snake[1] * cell))
def draw_point(dis):
    display_number.draw_num(dis, (550, 5), point[0] // 10, 15, cube_point)
    display_number.draw_num(dis, (605, 5), point[0] % 10, 15, cube_point)
    pygame.display.update([550, 5, 100, 75])

def reset(snakes, Id):
    minx, maxx, miny, maxy = 1200, 0, 750, 0
    for snake in snakes:
        maxx = max(maxx, snake[0])
        maxy = max(maxy, snake[1])
        minx = min(minx, snake[0])
        miny = min(miny, snake[1])
    snakes[:] = init_snakes[Id]
    
    save.append([minx * cell, miny * cell, (maxx - minx + 1) * cell, (maxy - miny + 1) * cell])
    #save.append([snakes[-1][0] * cell, snakes[-1][1] * cell, 40, 80])

def move_snake(dis, snakes, point, Id):
    save.append([(snakes[0][0] - 1) * cell, (snakes[0][1] - 1) * cell, cell * 3, cell * 3])
    save.append([(snakes[-1][0] - 1) * cell, (snakes[-1][1] - 1) * cell, cell * 3, cell * 3])
    global apple_x, apple_y, direc
    if direc[Id] == -1:
        return
    snakes.append([snakes[-1][0] + delta[direc[Id]][0], snakes[-1][1] + delta[direc[Id]][1]])
    if mark[(snakes[-1][0], snakes[-1][1])] == True or (snakes[-1] in snakes[:-1]):
        radio.touchfence.play()
        reset(snakes, Id)
        direc[Id] = -1
        point[Id] = max(0, point[Id] - 1)
        draw_point(dis)
        return

    if apple_x == snakes[-1][0] and apple_y == snakes[-1][1]:
        point[Id] += 1
        radio.farm[random.randint(0, 4)].play()
        while True:
            apple_x = random.randint(1, 58)
            apple_y = random.randint(6, 33)
            if mark[(apple_x, apple_y)] == False:
                break
        draw_point(dis)
        #print(point, point2)
    else:
        snakes.pop(0)
   

def play(dis, Fence, Name):
    radio.playing.play()
    graphic.load_image()
    DECLINE = 90
    prepare_nickname(Name)
    Head = [graphic.head_up, graphic.head_down, graphic.head_left, graphic.head_right]
    Tail = [graphic.tail_up, graphic.tail_down, graphic.tail_left, graphic.tail_right]
    Body = [graphic.body_topleft, graphic.body_topright, graphic.body_bottomleft, graphic.body_bottomright, graphic.body_horizontal, graphic.body_vertical]

    global cube, cube_time, cube_point
    cube = pygame.transform.scale(graphic.cube, (20, 20))
    cube_point = pygame.transform.scale(graphic.cube, (15, 15))
    cube_time = pygame.transform.scale(graphic.cube, (8, 8))

    clock = pygame.time.Clock()
    clock.tick(60)
    SNAKE_MOVE = pygame.USEREVENT + 1
    DEC_TIME = pygame.USEREVENT + 2
    pygame.time.set_timer(SNAKE_MOVE, 120)
    pygame.time.set_timer(DEC_TIME, 1000)
    
    
    #init data 
    global snakes, snakes2, apple_x, apple_y, delta, direc, cell, save, mark, point
    snakes = init_snakes[0][:]
    snakes2 = init_snakes[1][:]

    save = []
    direc = [-1, -1]
    point = [0, 0]

    mark = defaultdict(bool)
    for [x, y] in Fence:
        mark[(x, y)] = True

    while True:
            apple_x = random.randint(1, 58)
            apple_y = random.randint(6, 33)
            if mark[(apple_x, apple_y)] == False:
                break
   
    runing = True    
    load_map = False
    pygame.event.set_allowed(None) 
    while runing:
        dis.fill(black)
        #Load map
        for pos in Fence:
            #Rect(dis, saddle, [pos[0] * cell, pos[1] * cell, cell, cell])
            dis.blit(cube, (pos[0] * cell, pos[1] * cell))
        for i in range(61):
            line(dis, aqua, (i * cell, 100), (i * cell, 700), 1)
        for i in range(31):
            line(dis, aqua, (0, i * cell + 100), (1200, i * cell + 100), 1)
       
        #line(dis, aqua, (600, 0), (600, 100), 2)
        line(dis, aqua, (0, 1), (1200, 1), 2)
        line(dis, aqua, (0, 1), (0, 100), 2)
        line(dis, aqua, (1200, 1), (1200, 100), 2)
        line(dis, aqua, (0, 700), (0, 800), 2)
        line(dis, aqua, (1200, 650), (1200, 750), 2)
        line(dis, aqua, (0, 750), (1200, 750), 2)
        line(dis, aqua, (400, 700), (500, 750), 2)
        line(dis, aqua, (800, 700), (700, 750), 2)
        line(dis, aqua, (500, 750), (700, 750), 2)
        dis.blit(img_name, (0, 1))
        
        draw_point(dis)
        #for ID in Move:
        #    dis.blit(graphic.tele, (ID[0] * cell, ID[1] * cell))
        
        if load_map == False:
            pygame.display.flip()
            load_map = True
        

        dis.blit(graphic.apple, (apple_x * cell, apple_y * cell))
        save.append([apple_x * cell, apple_y * cell, cell, cell])
        #sleep(0.07)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            if not runing:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and direc[0] != 1:
                    direc[0] = 0
                if event.key == pygame.K_s and direc[0] != 0 and direc[0] != -1:
                    direc[0] = 1
                if event.key == pygame.K_a and direc[0] != 3:
                    direc[0] = 2
                if event.key == pygame.K_d and direc[0] != 2:
                    direc[0] = 3

            if event.type == SNAKE_MOVE:
                    move_snake(dis, snakes, point, 0)
                    draw_snake(dis, snakes, Body, Head, Tail)
            if event.type == DEC_TIME and DECLINE > 0:
                DECLINE -= 1
                display_number.draw_num(dis, (570, 705), DECLINE // 10, 8, cube_time)
                display_number.draw_num(dis, (606, 705), DECLINE % 10, 8, cube_time)
                pygame.display.update([570, 705, 70, 40])
                if DECLINE == 0:
                    runing = False
                #print(DECLINE)
        while len(save):
            pygame.display.update(save[-1])
            save.pop()
    pygame.time.set_timer(SNAKE_MOVE, 0)
    pygame.time.set_timer(DEC_TIME, 0)
    radio.playing.stop()
    return point[0]
    
