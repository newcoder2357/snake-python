import pygame

def load_image():
    global apple, body_bottomleft, body_bottomright, body_horizontal, body_topleft, body_topright, body_vertical, head_down;
    global tail_up, tail_right, tail_left, tail_down, head_up, head_right, head_left;
    global body_bottomleft2, body_bottomright2, body_horizontal2, body_topleft2, body_topright2, body_vertical2, head_down2;
    global tail_up2, tail_right2, tail_left2, tail_down2, head_up2, head_right2, head_left2, tele, cube, menu 
  
    size = (20, 20)
    apple = pygame.image.load("snake_graphics/apple.png").convert_alpha()
    apple = pygame.transform.scale(apple, size)

    body_bottomleft = pygame.image.load("snake_graphics/body_bottomleft.png").convert_alpha()
    body_bottomleft = pygame.transform.scale(body_bottomleft, size)

    body_bottomright = pygame.image.load("snake_graphics/body_bottomright.png").convert_alpha()
    body_bottomright = pygame.transform.scale(body_bottomright, size)

    body_horizontal = pygame.image.load("snake_graphics/body_horizontal.png").convert_alpha()
    body_horizontal = pygame.transform.scale(body_horizontal, size)

    body_topleft = pygame.image.load("snake_graphics/body_topleft.png").convert_alpha()
    body_topleft = pygame.transform.scale(body_topleft, size)

    body_topright = pygame.image.load("snake_graphics/body_topright.png").convert_alpha()
    body_topright = pygame.transform.scale(body_topright, size)

    body_vertical = pygame.image.load("snake_graphics/body_vertical.png").convert_alpha()
    body_vertical = pygame.transform.scale(body_vertical, size)

    head_down = pygame.image.load("snake_graphics/head_down.png").convert_alpha()
    head_down = pygame.transform.scale(head_down, size)

    head_left = pygame.image.load("snake_graphics/head_left.png").convert_alpha()
    head_left = pygame.transform.scale(head_left, size)

    head_right = pygame.image.load("snake_graphics/head_right.png").convert_alpha()
    head_right = pygame.transform.scale(head_right, size)

    head_up = pygame.image.load("snake_graphics/head_up.png").convert_alpha()
    head_up = pygame.transform.scale(head_up, size)

    tail_down = pygame.image.load("snake_graphics/tail_down.png").convert_alpha()
    tail_down = pygame.transform.scale(tail_down, size)

    tail_left = pygame.image.load("snake_graphics/tail_left.png").convert_alpha()
    tail_left = pygame.transform.scale(tail_left, size)

    tail_right = pygame.image.load("snake_graphics/tail_right.png").convert_alpha()
    tail_right = pygame.transform.scale(tail_right, size)

    tail_up = pygame.image.load("snake_graphics/tail_up.png").convert_alpha()
    tail_up = pygame.transform.scale(tail_up, size)

    body_bottomleft2 = pygame.image.load("snake_graphics/body_bottomleft2.png").convert_alpha()
    body_bottomleft2 = pygame.transform.scale(body_bottomleft2, size)

    body_bottomright2 = pygame.image.load("snake_graphics/body_bottomright2.png").convert_alpha()
    body_bottomright2 = pygame.transform.scale(body_bottomright2, size)

    body_horizontal2 = pygame.image.load("snake_graphics/body_horizontal2.png").convert_alpha()
    body_horizontal2 = pygame.transform.scale(body_horizontal2, size)

    body_topleft2 = pygame.image.load("snake_graphics/body_topleft2.png").convert_alpha()
    body_topleft2 = pygame.transform.scale(body_topleft2, size)

    body_topright2 = pygame.image.load("snake_graphics/body_topright2.png").convert_alpha()
    body_topright2 = pygame.transform.scale(body_topright2, size)

    body_vertical2 = pygame.image.load("snake_graphics/body_vertical2.png").convert_alpha()
    body_vertical2 = pygame.transform.scale(body_vertical2, size)

    head_down2 = pygame.image.load("snake_graphics/head_down2.png").convert_alpha()
    head_down2 = pygame.transform.scale(head_down2, size)

    head_left2 = pygame.image.load("snake_graphics/head_left2.png").convert_alpha()
    head_left2 = pygame.transform.scale(head_left2, size)

    head_right2 = pygame.image.load("snake_graphics/head_right2.png").convert_alpha()
    head_right2 = pygame.transform.scale(head_right2, size)

    head_up2 = pygame.image.load("snake_graphics/head_up2.png").convert_alpha()
    head_up2 = pygame.transform.scale(head_up2, size)

    tail_down2 = pygame.image.load("snake_graphics/tail_down2.png").convert_alpha()
    tail_down2 = pygame.transform.scale(tail_down2, size)

    tail_left2 = pygame.image.load("snake_graphics/tail_left2.png").convert_alpha()
    tail_left2 = pygame.transform.scale(tail_left2, size)

    tail_right2 = pygame.image.load("snake_graphics/tail_right2.png").convert_alpha()
    tail_right2 = pygame.transform.scale(tail_right2, size)

    tail_up2 = pygame.image.load("snake_graphics/tail_up2.png").convert_alpha()
    tail_up2 = pygame.transform.scale(tail_up2, size)


    cube = pygame.image.load("snake_graphics/cube.png").convert_alpha()
    
    menu = pygame.image.load("snake_graphics/menu.png").convert_alpha()
    

    selec_map_relax_mode = pygame.image.load("snake_graphics/select_map_relax_mode.png")

