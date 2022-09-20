import consts
import pygame
import screen

minefield = consts.MINEFIELD

guard = pygame.Rect(0,210,consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT)

def guard_matrix():
    #Checking guard location in the matrix
    guard_col = int(guard.x) // consts.VEL
    return guard_col

def guard_location_in_matrix():
    minefield = consts.MINEFIELD
    guard_body_matrix = []
    guard_col = guard_matrix()
    for i in range(3):
        for j in range(2):
            guard_body_matrix.append((10+i,guard_col+j))
    return guard_location_in_matrix()

def check_match():
    soldier_body = consts.soldier_full_location
    guard_body = guard_location_in_matrix()
    match = 0
    for i in range(len(guard_body)):
        for j in range(2):
            if guard_body[i][0+j] == soldier_body[i][0+j]:
                match+= 1
            if match >= 2:
                return True

guard_picture = pygame.image.load('guardpic.png')
guard_picture = pygame.transform.scale(guard_picture,
                                           (consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT))
def guard_moving():
    count = 0
    while count <= 35:
        screen.SCREEN.blit(guard_picture, guard.x, guard.y)
        guard.x += 20
        count+=1
        pygame.display.update()














