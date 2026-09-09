import random

import pygame
from sys import exit #terminate the program

import consts
import game_field

pygame.font.init()

#game variables
GAME_WIDTH = consts.WINDOW_WIDTH
GAME_HEIGHT = consts.WINDOW_HEIGHT

text_font = pygame.font.SysFont(consts.FONT_NAME, consts.FONT_SIZE)
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

img = pygame.image.load("grass.png")
img = pygame.transform.scale(img, (60, 60))


def draw_screen():
    pygame.init() #always needed to initialize pygame
    pygame.display.set_caption("The Flag Game") #title of the window

def draw_player(x,y, img):
    player = pygame.transform.scale(img, (consts.CELL_SIZE * 2, consts.CELL_SIZE * 4))
    window.blit(player, (x,y))


def draw_bushes():
        x = random.randint(0,(consts.BOARD_COLS*20))
        y = random.randint(0,(consts.BOARD_ROWS*20))
        window.blit(img, (x, y))

def draw_bombs(x,y):
    bombs = pygame.image.load("mine.png")
    window.blit(bombs, (x, y))

def draw_flag():
    flag = pygame.image.load("flag.png")
    flag = pygame.transform.scale(flag, (consts.CELL_SIZE*3,consts.CELL_SIZE*4))
    window.blit(flag, (GAME_WIDTH-3*consts.CELL_SIZE, GAME_HEIGHT - 4*consts.CELL_SIZE))


def draw_text(text, font, text_color, x, y):
    text_hello = font.render(text, True, text_color)
    window.blit(text_hello, (x, y))

def put_bombs():
    field = game_field.spred_bombs()
    for i in range(len(field)):
        for j in range(len(field[i])):
            if j == "BOMB":
                draw_bombs(i,j)

def night_mode_lines(screen):
    for x in range(0, GAME_WIDTH, 20):
        pygame.draw.line(screen, consts.LINE_COLOR, (1, x), (GAME_WIDTH, x), 2)
    for y in range(0, GAME_WIDTH, 20):
        pygame.draw.line(screen, consts.LINE_COLOR, (y, 1), (y, GAME_WIDTH), 2)


def run():
    window.fill(consts.COLOR_SCREEN)
    for i in range(20):
        draw_bushes()
    sol_img = pygame.image.load("soldier.png")
    draw_player(0, 0, sol_img)
    draw_text("Welcome To The Flag Game!\n HAVE FUN!", text_font, (255,255,255), 30,0)
    draw_flag()
    while True: #game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #user clicks the X button in window
                pygame.quit()
                exit()
        pygame.display.update()
        # window.blit(img, (950, 0))
        # draw_bushes()
        pygame.display.flip()



def run_night_mode():
    window.fill(consts.COLOR_SCREEN)
    night_img = pygame.image.load("soldier_night.png")
    # draw_player(0, 0,night_img)
    draw_flag()
    put_bombs() #DOESNT SHOW BOMBS
    screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    while True: #game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #user clicks the X button in window
                pygame.quit()
                exit()
            night_mode_lines(screen)
            draw_flag()
            draw_player(0, 0, night_img)
        pygame.display.update()
        pygame.display.flip()