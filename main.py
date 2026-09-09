from pygame.display import update

import Screen
import consts
import pygame
import keyboard

import game_field
import soldier



dark = pygame.image.load("soldier_night.png")
dead = pygame.image.load("injury.png")


#run game
def normal_mode():
    img = pygame.image.load("soldier.png")
    #cordinantes
    x = 0
    y = 0

    #if lost or won
    flag = False

    Screen.window.fill((0,0,0))
    Screen.normal()
    while True: #game loop
        Screen.normal()
        pygame.time.delay(20)
        pygame.time.delay(20)
        if game_field.is_soldier_touch_bomb([y // consts.CELL_SIZE,x // consts.CELL_SIZE]):
            Screen.draw_text("LOSE", Screen.text_font,
                             (255, 255, 255), (consts.BOARD_COLS // 2) * 20,
                             (consts.BOARD_ROWS // 2) * 20)
            flag = True

        if (game_field.is_soldier_touch_flag
                ([y // consts.CELL_SIZE,x // consts.CELL_SIZE])):
            Screen.draw_text("WIN", Screen.text_font,
                             (255, 255, 255), (consts.BOARD_COLS // 2) * 20,
                             (consts.BOARD_ROWS // 2) * 20)
            flag = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #user clicks the X button in window
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            Screen.night()
            Screen.draw_player(x, y, dark)
        elif flag == False:
            if keys[pygame.K_LEFT] and x > 0:
                x -= consts.CELL_SIZE

            if keys[pygame.K_RIGHT] and x < consts.WINDOW_WIDTH - consts.CELL_SIZE*2:
                x += consts.CELL_SIZE

            if keys[pygame.K_UP] and y > 0:
                y -= consts.CELL_SIZE

            if keys[pygame.K_DOWN] and y < consts.WINDOW_HEIGHT - consts.CELL_SIZE*4:
                y += consts.CELL_SIZE
            Screen.draw_player(x,y,img)

        pygame.display.update()
        pygame.display.flip()


normal_mode()
