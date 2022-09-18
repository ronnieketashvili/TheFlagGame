import MineField
import consts
import screen
import pygame
import soldier

pygame.init()

def main(): #פה ירוץ המשחק
    CLOCK = pygame.time.Clock()
    while not consts.FINISH:
        CLOCK.tick(consts.FPS)
        for event in pygame.event.get():
            screen.player_screen()
            if event.type == pygame.QUIT:
                consts.FINISH = True
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
                if event.key == pygame.K_KP_ENTER:
                    count = 0
                    while count != 35:
                        screen.when_enter_pressed()
                        count += 1
    pygame.quit()



if __name__ == '__main__':
    main()
