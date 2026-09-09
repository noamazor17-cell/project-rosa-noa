from pygame.display import update

import Screen
import consts
import pygame
import keyboard

import soldier

# screen = pygame.display.set_mode(
#         (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

# Screen.screen_draw()

# Screen.screen_draw()
#
# Screen.draw():
#
# window = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
# text_font = pygame.font.SysFont(consts.FONT_NAME, consts.FONT_SIZE)

# window = Screen.window

player = pygame.Vector2(100,100)

# def normal_mode():
#     img = pygame.image.load("soldier.png")
#     Screen.normal()
#     while True: #game loop
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT: #user clicks the X button in window
#                 pygame.quit()
#                 exit()
#         mouse_x, mouse_y = pygame.mouse.get_pos()
#         img_rect = img.get_rect(center=(mouse_x ,mouse_y))
#         Screen.window.blit(img, img_rect)
#         pygame.display.update()
#         pygame.display.flip()


def normal_mode():
    img = pygame.image.load("soldier.png")
    x = 0
    y = 0

    width = 20
    height = 20

    vel = 1

    Screen.window.fill((0,0,0))
    Screen.normal()
    while True: #game loop
        Screen.normal()
        pygame.time.delay(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #user clicks the X button in window
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            Screen.night()

        if keys[pygame.K_LEFT] and x > 0:
            x -= vel*consts.CELL_SIZE

        if keys[pygame.K_RIGHT] and x < consts.WINDOW_WIDTH - consts.CELL_SIZE*2:
            x += vel*consts.CELL_SIZE

        if keys[pygame.K_UP] and y > 0:
            y -= vel*consts.CELL_SIZE

        if keys[pygame.K_DOWN] and y < consts.WINDOW_HEIGHT - consts.CELL_SIZE*2:
            y += vel*consts.CELL_SIZE
        Screen.draw_player(x,y,img)

        pygame.display.update()
        pygame.display.flip()


normal_mode()

# def night_mode():
#     Screen.night()
#     while True: #game loop
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT: #user clicks the X button in window
#                 pygame.quit()
#                 exit()
#         pygame.display.update()
#         pygame.display.flip()


# night_mode()
# Screen.run_night_mode()