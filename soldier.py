import consts
import random
import keyboard
import pygame

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


def is_in_board(col, row, direction):
    if direction == "BODY":




def print_soldier(soldier):
    #check
    for row in soldier:
        for col in row:
            print(col, end=" ")
        print()



print_soldier(create_solider())

