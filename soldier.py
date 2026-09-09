import Screen
import consts
import random
import keyboard
import pygame

import game_field

solider = [0,0]


# create_solider()
def update_solider_location(x,y):
    solider[0] = x
    solider[1] = y
    return solider



#checks if player is in range of board
def is_in_board(col, row):
    return row >= 0 and row + 3 <= consts.BOARD_ROWS and col + 1 <= consts.BOARD_COLS and col >= 0

#return the corrct string for move
def move():
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

#make a move, and move the soldier only if move is valid
def make_a_move():
    the_move = move()
    if is_in_board(the_move[1], the_move[0]):
        update_solider_location(the_move[0], the_move[1])
        return True
    else:
        return False


