import MineField
import consts
import screen
import pygame
import soldier
import Database


time_press_keys = {
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

pygame.init()
def main():
    Database.initialize_database()
    clock = pygame.time.Clock()
    while not consts.FINISH:
        clock.tick(consts.FPS)
        for event in pygame.event.get():
            screen.player_screen()
            screen.draw_start_message()
            if event.type == pygame.QUIT:
                consts.FINISH = True
            if event.type == pygame.KEYDOWN:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    time_press_keys[event.key] = pygame.time.get_ticks()
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
                if event.key == pygame.K_RETURN: # TODO: change it to normal time handling
                    count = 0
                    while count != 35:
                        screen.when_enter_pressed()
                        count += 1
            if event.type == pygame.KEYUP:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    time_elapsed = (pygame.time.get_ticks() - time_press_keys[event.key]) / 1000.0
                    if time_elapsed <= 1:
                        Database.get_data_for_press(chr(event.key))
                    else:
                        if Database.check_exist_memory(chr(event.key)):
                            screen.BUSHES_LIST = Database.get_property_coordinates(chr(event.key), consts.BUSH_COORD)
                            consts.MINES_LIST = Database.get_property_coordinates(chr(event.key), consts.MINES_COORD)
                            soldier.soldier.x, soldier.soldier.y = Database.get_property_coordinates(chr(event.key),consts.SOLDIER_COORD)

    pygame.quit()


if __name__ == '__main__':
    main()
