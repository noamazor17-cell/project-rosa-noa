import Screen
import consts
import random
import keyboard
import pygame

import game_field

solider = [0,0]

#creates soldier body and legs
# def create_solider():
#     solider.append(0)
#     solider.append(0)
#     return solider

def update_solider_location(x,y):
    # create_solider()
    solider[0] = x
    solider[1] = y
    return solider

    # global solider
    # for i in range(4):
    #     row = []
    #     for j in range(2):
    #         row.append("BODY")
    #     solider.append(row)
    # solider[3][0] = "LEGS"
    # solider[3][1] = "LEGS"
    # return solider


# def is_in_board(col, row):
#     if game_field.move() == "up":
#         return row > 0
#     if game_field.move() == "down":
#         return row + 3 < consts.BOARD_ROWS
#     if game_field.move() == "right":
#         return col + 1 > consts.BOARD_COLS
#     if game_field.move() == "left":
#         return col > 0


#checks if player is in range of board
def is_in_board(col, row):
    return row >= 0 and row + 3 <= consts.BOARD_ROWS and col + 1 <= consts.BOARD_COLS and col >= 0


# def print_soldier(soldier):
#     #check
#     for row in soldier:
#         for col in row:
#             print(col, end=" ")
#         print()



def move():
    #return the corrct string for move
    row = solider[0]
    col = solider[1]
    print("enter arrow")
    if keyboard.read_key() == 'up':
        print("Up")
        return [row+1, col]
    elif keyboard.read_key() == 'left':
        print("Left")
        return [row, col-1]
    elif keyboard.read_key() == 'right':
        print("Right")
        return [row, col+1]
    elif keyboard.read_key() == 'down':
        print("Down")
        return [row-1, col]


def make_a_move():
    the_move = move()
    if is_in_board(the_move[1], the_move[0]):
        update_solider_location(the_move[0], the_move[1])
        return True
    else:
        return False


# def move_sol():
#     x = 200
#     y = 200
#
#     width = 20
#     height = 20
#
#     vel = 10
#
#     keys = pygame.key.get_pressed()
#
#     if keys[pygame.K_LEFT] and x > 0:
#         x -= vel
#
#     if keys[pygame.K_RIGHT] and x < consts.WINDOW_WIDTH - width:
#         x += vel
#
#     if keys[pygame.K_UP] and y > 0:
#         y -= vel
#
#     if keys[pygame.K_DOWN] and y < consts.WINDOW_HEIGHT - width:
#         y += vel
#
#     Screen.normal()
#     pygame.draw.rect(Screen.window, (255, 0, 0), (x, y, width, height))


