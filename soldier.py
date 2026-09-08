import consts
import random
import keyboard
import pygame

import game_field

solider = []
def create_solider():
    global solider
    for i in range(4):
        row = []
        for j in range(2):
            row.append("BODY")
        solider.append(row)
    solider[3][0] = "LEGS"
    solider[3][1] = "LEGS"
    return solider


def is_in_board(col, row):
    if game_field.move() == "up":
        return row > 0
    if game_field.move() == "down":
        return row + 3 < consts.BOARD_ROWS
    if game_field.move() == "right":
        return col + 1 > consts.BOARD_COLS
    if game_field.move() == "left":
        return col > 0




def print_soldier(soldier):
    #check
    for row in soldier:
        for col in row:
            print(col, end=" ")
        print()



print_soldier(create_solider())

