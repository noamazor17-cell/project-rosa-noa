import consts
import random
import keyboard
import pygame

solider = []
is_soldier = "SOLDIER"
def create_solider():
    global solider
    for i in range(4):
        row = []
        for j in range(2):
            row.append((is_soldier))
        solider.append(row)
    return solider


def legs(solider):
    for row in solider:



def print_soldier(soldier):
    #check
    for row in soldier:
        for col in row:
            print(col, end=" ")
        print()

print_soldier(create_solider())

