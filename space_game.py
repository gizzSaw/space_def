import pygame
import sys
from gun import Gun

def run():

    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Space Defenders")
    bg_color = (110, 10, 10)
    gun = Gun(screen)

    print(gun)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        gun.output()
        pygame.display.flip()

run()