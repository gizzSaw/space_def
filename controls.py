import pygame, sys
from bullet import Bullet
from ino import Ino

def events(screen, gun, bullets):
    """обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #вправо
            if event.key == pygame.K_d:
                gun.mright = True
            #влево
            elif event.key == pygame.K_a:
                gun.mleft = True
            #стрелять
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            #вправо
            if event.key == pygame.K_d:
                gun.mright = False
            #влево
            elif event.key == pygame.K_a:
                gun.mleft = False
def update(bg_color, screen, gun, inos, bullets):
    """обновление экрана"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()

def update_bullets(bullets): 
    """обновление позиции пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            print('пуля внатуре удалена')
            print('осталось пуль ' + str(len(bullets)))
def update_inos(inos):
    """обновляет позицию пришельца"""
    inos.update()

def create_army(screen, inos):
    """создание армии пришельцев"""
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((600 - 2 * ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((700 - 100 - 2 * ino_height) / ino_height)

    for row_number in range(number_ino_y - 1):

        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + ino_width * ino_number
            ino.y = ino_height + ino_height * row_number
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * row_number
            inos.add(ino)