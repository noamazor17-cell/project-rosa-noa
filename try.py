import consts
import random
import game_field as gf
import keyboard
import soldier

# field = gf.create_field()
# list_of_bombs = gf.spred_bombs(field)
# flag = gf.square_collide_with_flag()
# collide_bomb = gf.square_collide_with_bomb(field)
# #gf.print_field(field)
# print(flag)
# print(collide_bomb)
# Source - https://stackoverflow.com/q/78044134
# Posted by Jack
# Retrieved 2026-09-08, License - CC BY-SA 4.0

# Source - https://stackoverflow.com/q/74326247
# Posted by Saif Bashar, modified by community. See post 'Timeline' for change history
# Retrieved 2026-09-08, License - CC BY-SA 4.0

import keyboard
field = gf.spred_bombs()
soldier = soldier.create_solider()
print("----------------------------------------------------------------------")
gf.print_field(field)
print("----------------------------------------------------------------------")
print("----------------------------------------------------------------------")
print(gf.make_a_move(field,soldier))
print("----------------------------------------------------------------------")
gf.print_field(field)
print("----------------------------------------------------------------------")



#fix creat field\ make a move doesen't get the place of the soldier\ doesn't get e direction