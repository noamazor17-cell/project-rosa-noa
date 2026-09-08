import consts
import random
import keyboard
import soldier

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


def put_solider_at_field(first_squrt, solider, field):
    soldier_i = 0
    for i in range(first_squrt[0], first_squrt[0]+4):
        soldier_j = 0
        for j in range(first_squrt[1], first_squrt[1]+2):
            field[i][j] = solider[soldier_i][soldier_j]
            soldier_j += 1
        soldier_i += 1


def move(solider):
    #return the corrct string for move
    row = solider[0]
    col = solider[0][0]
    while True:
        if keyboard.read_key() == 'up':
            return [row+1, col]
        if keyboard.read_key() == 'left':
            return [row, col-1]
        if keyboard.read_key() == 'right':
            return [row, col+1]
        if keyboard.read_key() == 'down':
            return [row-1, col]


def make_a_move(field, solider):
    the_move = move(solider)
    if soldier.is_in_board(the_move[0], the_move[1]):
        put_solider_at_field(the_move, solider, field)
        return True
    else:
        return False







