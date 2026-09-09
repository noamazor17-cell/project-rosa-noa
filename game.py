import consts
import random
import game_field as gf
import keyboard
import soldier
from game_field import create_field

is_winner = False
while not is_winner:
    field = gf.spred_bombs()
    gf.print_field()
    print("----------------------------------------------------------------------------------------------------------")
    print("creating soldier")
    s = soldier.create_solider()
    made_move = soldier.make_a_move()
    if made_move:
        print("soldier moved")
    else:
        print("soldier not moved")
    is_winner = gf.is_soldier_touch_flag(s)
    if is_winner:
        print("soldier wins")
    if gf.is_soldier_touch_bomb(s):
        print("soldier lost")




