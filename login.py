import pygame 
import setting

def login(dis, intro, color):    
    #define font 
    font_intro = pygame.font.Font(None, 70) 
    font_name = pygame.font.Font(None, 40)
    Content = ""
    
    text_intro = font_intro.render(intro, True, color)
    intro_size_x, intro_size_y = text_intro.get_size()
    intro_x = (setting.WIDTH - intro_size_x) / 2
    intro_y = (setting.HEIGHT - intro_size_y) / 2

    

    enter_click = False
    running = True
    updated = False
    while running:
        dis.fill((0, 0, 0))
        #pygame.draw.rect(dis, white, [box_x * cell, box_y * cell , cell * 20, cell + 5], 1)
        text_img = font_name.render("Name: " + Content + "|", True, color)
        dis.blit(text_intro, (intro_x, intro_y))
        dis.blit(text_img, (intro_x, intro_y + intro_size_y))
        if not updated:
            pygame.display.flip()
            updated = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            if enter_click:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    enter_click = True 
                elif event.key == pygame.K_BACKSPACE:
                    if len(Content) > 0:
                        Content = Content[:-1]
                elif event.unicode and len(event.unicode) == 1 and len(Content) <= 9:
                    Content += event.unicode
        pygame.display.update([intro_x, intro_y + intro_size_y, 400, text_img.get_height()])
    return Content
     
