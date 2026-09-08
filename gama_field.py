import consts
import random

field = []
EMPTY = "EMPTY"
BOOM = "BOOM"

def create_field():
    global field
    for i in range(consts.BOARD_ROWS):
        row = []
        for j in range(consts.BOARD_COLS):
            row.append((EMPTY))
        field.append(row)
    return field


def print_field(field):
    for row in field:
        for col in row:
            print(col, end=" ")
        print()


def spred_booms(field):
    for i in range (20):
        col = random.randint(0, consts.BOARD_COLS-1)
        row = random.randint(0, consts.BOARD_ROWS-1)
        while field[row][col] != EMPTY:
            col = random.randint(0, consts.BOARD_COLS)
            row = random.randint(0, consts.BOARD_ROWS)
        if (col == consts.BOARD_COLS-1):
            field[row][col] = BOOM
            field[row][col-1] = BOOM
            field[row][col-2] = BOOM
        elif (col+1 == consts.BOARD_COLS-1):
            field[row][col] = BOOM
            field[row][col-1] = BOOM
            field[row][col+1] = BOOM
        else:
            field[row][col] = BOOM
            field[row][col+1] = BOOM
            field[row][col+2] = BOOM

def square_colide_with_flag(field, flag):
    for i in range(consts.BOARD_ROWS, consts.BOARD_ROWS):






spred_booms(create_field())
print_field()