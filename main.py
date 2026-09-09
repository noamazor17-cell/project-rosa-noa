import Screen
import consts
import pygame
import keyboard


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

def normal_mode():
    Screen.normal()
    while True: #game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #user clicks the X button in window
                pygame.quit()
                exit()
        pygame.display.update()
        pygame.display.flip()


normal_mode()

def night_mode():
    Screen.night()
    while True: #game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #user clicks the X button in window
                pygame.quit()
                exit()
        pygame.display.update()
        pygame.display.flip()


# night_mode()
# Screen.run_night_mode()