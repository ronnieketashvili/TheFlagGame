import MineField
import consts
import screen
import pygame
import soldier
import Database

pygame.init()
dict_keys = {
    pygame.K_1: 0,
    pygame.K_2: 0,
    pygame.K_3: 0,
    pygame.K_4: 0,
    pygame.K_5: 0,
    pygame.K_6: 0,
    pygame.K_7: 0,
    pygame.K_8: 0,
    pygame.K_9: 0
}
def main():
    CLOCK = pygame.time.Clock()
    while not consts.FINISH:
        CLOCK.tick(consts.FPS)
        for event in pygame.event.get():
            screen.player_screen()
            screen.drow_start_message()
            if event.type == pygame.QUIT:
                consts.FINISH = True
            if event.type == pygame.KEYDOWN:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    dict_keys[event.key] = pygame.time.get_ticks()
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
                if event.key == pygame.K_RETURN:
                    count = 0
                    while count != 35:
                        screen.when_enter_pressed()
                        count += 1
            if event.type == pygame.KEYUP:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    time_elapsed = (pygame.time.get_ticks() - dict_keys[event.key]) / 1000.0
                    print(time_elapsed)
                    if time_elapsed <= 1:
                        Database.getting_data_for_press(int(chr(event.key)))
                        print("fast", int(chr(event.key)))
                    else:
                        print("slow", int(chr(event.key)))

    pygame.quit()




if __name__ == '__main__':
    main()
