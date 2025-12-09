import pygame



def selec_map(dis):
    img_mode = pygame.image.load("snake_graphics/select_map_relax_mode.png").convert_alpha()
    updated = False
    key = 0
    run = True 
    while run:
        dis.blit(img_mode, (0, 0))
        if not updated:
            pygame.display.flip()
            updated = True 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and key == 0:
                    key = 1
                    run = False 
                if event.key == pygame.K_2 and key == 0:
                    key = 2
                    run = False 
                if event.key == pygame.K_3 and key == 0:
                    key = 3
                    run = False 
                if event.key == pygame.K_4 and key == 0:
                    key = 4
                    run = False 
                if event.key == pygame.K_5 and key == 0:
                    key = 5
                    run = False 
                if event.key == pygame.K_6 and key == 0:
                    key = 6
                    run = False 
                if event.key == pygame.K_7 and key == 0:
                    key = 7
                    run = False 
    return key                
