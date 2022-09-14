import MineField
import consts
import screen
import pygame

import soldier


def draw_screen():
    SCREEN_COLOR = (61, 145, 64)
    screen.SCREEN.fill(SCREEN_COLOR)
    screen.SCREEN.blit(soldier.soldier_image, (soldier.soldier.x, soldier.soldier.y))
    pygame.display.update()


def maim(): #פה ירוץ המשחק
    clock = pygame.time.Clock()
    MINEFIELD = MineField.creating_minefield()
    finish = False
    while not finish:
        clock.tick(consts.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
        soldier.soldier_moving()
        draw_screen()
    pygame.quit()
if __name__ == '__main__':
    maim()
