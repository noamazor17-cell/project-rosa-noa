import random

import pygame
from sys import exit #terminate the program

import consts
import game_field
from consts import flag_row, flag_col

pygame.font.init()

#game variables
GAME_WIDTH = consts.WINDOW_WIDTH
GAME_HEIGHT = consts.WINDOW_HEIGHT

text_font = pygame.font.SysFont(consts.FONT_NAME, consts.FONT_SIZE)
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

img = pygame.image.load("grass.png")
img = pygame.transform.scale(img, (consts.CELL_SIZE*3, consts.CELL_SIZE*3))


def draw_screen():
    pygame.init() #always needed to initialize pygame
    pygame.display.set_caption("The Flag Game") #title of the window

def draw_player(x,y, img):
    player = pygame.transform.scale(img, (consts.CELL_SIZE * 2, consts.CELL_SIZE * 4))
    window.blit(player, (x,y))

lst_bushes = []
for i in range(20):
    x = random.randint(0, (consts.BOARD_COLS * 20))
    y = random.randint(0, (consts.BOARD_ROWS * 20))
    lst_bushes.append((x,y))


def draw_bushes():
        for bush in lst_bushes:
            window.blit(img, bush)

def draw_bombs(x,y):
    bombs = pygame.image.load("mine.png")
    bombs = pygame.transform.scale(bombs, (consts.CELL_SIZE*3, consts.CELL_SIZE))
    window.blit(bombs, (y,x))


def draw_flag():
    flag = pygame.image.load("flag.png")
    flag = pygame.transform.scale(flag, (consts.CELL_SIZE*3,consts.CELL_SIZE*4))
    window.blit(flag, (flag_col, flag_row))


def draw_text(text, font, text_color, x, y):
    text_hello = font.render(text, True, text_color)
    window.blit(text_hello, (x, y))

where_bomb = []
field = game_field.spred_bombs()
for i in range(len(field)):
    for j in range(len(field[i])):
        if field[i][j] == "BOMB":
                where_bomb.append((i, j))

def put_bombs():
    for bomb in where_bomb:
        draw_bombs(bomb[0]*consts.CELL_SIZE,bomb[1]*consts.CELL_SIZE)


def night_mode_lines(screen):
    for x in range(0, GAME_WIDTH, 20):
        pygame.draw.line(screen, consts.LINE_COLOR, (1, x), (GAME_WIDTH, x), 2)
    for y in range(0, GAME_WIDTH, 20):
        pygame.draw.line(screen, consts.LINE_COLOR, (y, 1), (y, GAME_WIDTH), 2)


# def run():
#     window.fill(consts.COLOR_SCREEN)
#     for i in range(20):
#         draw_bushes()
#     sol_img = pygame.image.load("soldier.png")
#     draw_player(0, 0, sol_img)
#     draw_text("Welcome To The Flag Game!\n HAVE FUN!", text_font, (255,255,255), 30,0)
#     draw_flag()
#     while True: #game loop
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT: #user clicks the X button in window
#                 pygame.quit()
#                 exit()
#         pygame.display.update()
#         pygame.display.flip()



# def run_night_mode():
#     window.fill(consts.COLOR_SCREEN)
#     night_img = pygame.image.load("soldier_night.png")
#     # draw_player(0, 0,night_img)
#     draw_flag()
#     put_bombs() #DOESNT SHOW BOMBS
#     screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
#     while True: #game loop
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT: #user clicks the X button in window
#                 pygame.quit()
#                 exit()
#             night_mode_lines(screen)
#             draw_flag()
#             draw_player(0, 0, night_img)
#         pygame.display.update()
#         pygame.display.flip()

# def d():
#     for i in range(20):
#         draw_bushes()

def normal():
    window.fill(consts.COLOR_SCREEN)
    draw_bushes()
    sol_img = pygame.image.load("soldier.png")
    # draw_player(0, 0, sol_img)
    draw_text("Welcome To The Flag Game!\n HAVE FUN!", text_font,
              (255, 255, 255), 30, 0)
    draw_flag()


def night():
    night_img = pygame.image.load("soldier_night.png")
    window.fill((0,0,0))
    # draw_player(0, 0,img_night)
    draw_flag()
    put_bombs()
    night_mode_lines(window)
    draw_flag()
    draw_player(0, 0, night_img)
    # draw_player(0,100, night_img)
    # draw_player(GAME_WIDTH, 0, night_img)
    # DOESNT SHOW BOMBS

# def __init__(self, image, height, speed):
#         self.speed = speed
#         self.image = image
#         self.pos = image.get_rect().move(0, height)
#
# def move(self):

#         self.pos = self.pos.move(self.speed, 0)
#         if self.pos.right > 600:
#             self.pos.left = 0