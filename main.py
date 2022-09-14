import MineField
import consts
import screen
import pygame
import soldier





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
        screen.opening_screen()
    pygame.quit()
if __name__ == '__main__':
    maim()
