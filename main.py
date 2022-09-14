import MineField
import consts
import screen
import pygame
import soldier




def main(): #פה ירוץ המשחק
    clock = pygame.time.Clock()
    MINEFIELD = MineField.creating_minefield()
    finish = False
    while not finish:
        clock.tick(consts.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
        soldier.soldier_in_matrix()
        screen.opening_screen()
    pygame.quit()
if __name__ == '__main__':
    main()
