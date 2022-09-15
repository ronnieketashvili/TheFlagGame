import MineField
import consts
import screen
import pygame
import soldier


pygame.init()

def main(): #פה ירוץ המשחק
    clock = pygame.time.Clock()
    finish = False
    while not finish:
        #clock.tick(consts.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    soldier.right_key()
                    soldier.checking_minefield()
                if event.key == pygame.K_LEFT:
                    soldier.left_key()
                    soldier.checking_minefield()
                if event.key == pygame.K_UP:
                    soldier.up_key()
                    soldier.checking_minefield()
                if event.key == pygame.K_DOWN:
                    soldier.down_key()
                    soldier.checking_minefield()
        screen.opening_screen()
    pygame.quit()



if __name__ == '__main__':
    main()
