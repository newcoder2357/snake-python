import pygame

def Delay(Time):
    start = pygame.time.get_ticks()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
        now = pygame.time.get_ticks()
        if now - start >= Time * 1000:
            break