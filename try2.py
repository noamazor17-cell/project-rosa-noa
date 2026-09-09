import keyboard

# keyboard.write("GEEKS FOR GEEKS\n")
#
# keyboard.press_and_release('shift + r, shift + k, \n')
# keyboard.press_and_release('R, K')
#
# keyboard.wait('Ctrl')GEEKS FOR GEEKS
# RK
# rk

# Source - https://stackoverflow.com/q/74326247
# Posted by Saif Bashar, modified by community. See post 'Timeline' for change history
# Retrieved 2026-09-09, License - CC BY-SA 4.0

import keyboard
print("Hello World")
print("enter arrow")
if keyboard.read_key() == 'left':
    print("left")
elif keyboard.read_key() == 'right':
    print("right")
elif keyboard.read_key() == 'down':
    print("down")
elif keyboard.read_key() == 'up':

