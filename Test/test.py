# additions chahiye
# aur dalna

import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAY = pygame.display.set_mode((400, 400))
pygame.display.set_caption('GAME!')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
