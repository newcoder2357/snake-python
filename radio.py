import pygame

pygame.mixer.init()

background = pygame.mixer.Sound("sound/background.wav")

dec5s = pygame.mixer.Sound("sound/dec5s.wav")

pause10s = pygame.mixer.Sound("sound/pause10s.wav")

playing = pygame.mixer.Sound("sound/playing.wav")

winer = pygame.mixer.Sound("sound/winer.wav")

showratio1 = pygame.mixer.Sound("sound/showratio1.wav")

showratio2 = pygame.mixer.Sound("sound/showratio2.wav")

touchfence = pygame.mixer.Sound("sound/touchfence.wav")

farm1 = pygame.mixer.Sound("sound/farm1.wav")

farm2 = pygame.mixer.Sound("sound/farm2.wav")

farm3 = pygame.mixer.Sound("sound/farm3.wav")

farm4 = pygame.mixer.Sound("sound/farm4.wav")

farm5 = pygame.mixer.Sound("sound/farm5.wav")

chaimpion = pygame.mixer.Sound("sound/champion.wav")

competitive = pygame.mixer.Sound("sound/competitive.wav")

farm = [farm1, farm2, farm3, farm4, farm5]
showratio = [showratio1, showratio2]
