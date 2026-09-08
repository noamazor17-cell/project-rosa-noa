import consts
import random

field = []
EMPTY = "EMPTY"
BOMB = "BOMB"

def create_field():
    #creat the field
    global field
    for i in range(consts.BOARD_ROWS):
        row = []
        for j in range(consts.BOARD_COLS):
            row.append((EMPTY))
        field.append(row)
    return field


def print_field(field):
    #print field
    for row in field:
        for col in row:
            print(col, end=" ")
        print()



def spred_bombs():
    field = create_field()
    #get the field, and randomly spred bombs at the field
    for i in range (20):
        col = random.randint(0, consts.BOARD_COLS-1)
        row = random.randint(0, consts.BOARD_ROWS-1)
        while field[row][col] != EMPTY:
            col = random.randint(0, consts.BOARD_COLS)
            row = random.randint(0, consts.BOARD_ROWS)
        if (col == consts.BOARD_COLS-1):
            field[row][col] = BOMB
            field[row][col-1] = BOMB
            field[row][col-2] = BOMB
        elif (col+1 == consts.BOARD_COLS-1):
            field[row][col] = BOMB
            field[row][col-1] = BOMB
            field[row][col+1] = BOMB
        else:
            field[row][col] = BOMB
            field[row][col+1] = BOMB
            field[row][col+2] = BOMB
    return field

def square_collide_with_flag():
    #make a list of squares that collide with flag
    collide_with_flag = []
    for i in range(consts.BOARD_ROWS, consts.BOARD_ROWS-3, -1):
        for j in range(consts.BOARD_COLS, consts.BOARD_COLS-4, -1):
            collide_with_flag.append((i, j))
    return collide_with_flag

def square_collide_with_bomb(field):
    collide_with_bomb = []
    for i in range(consts.BOARD_ROWS):
        for j in range(consts.BOARD_COLS):
            if field[i][j] == BOMB:
                collide_with_bomb.append((i, j))
    return collide_with_bomb

def is_solider_touch_flag(collide_with_flag, soldier):
    solider_touch_flag = False

