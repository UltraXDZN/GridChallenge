import pygame
from constants import *


def line_horizontal(x, y, width):
    for w in range(WIDTH):
        screen.set_at((x, y + width), foreground_color)
        y += 1
    y -= WIDTH


def line_vertical(x, y, width):
    for i in range(RES_Y):
        for w in range(width):
            screen.set_at((x, y), foreground_color)
            x += 1
        x -= width
        y += 1


if __name__ == '__main__':
    screen = pygame.display.set_mode((RES_X, RES_Y))
    pygame.display.set_caption(CAPTION)

    screen.fill(background_color)

    running = True
    cur_x, cur_y = DEFAULT_POS_X, DEFAULT_POS_Y
    cur_width = WIDTH

    while running:
        for y in range(0, RES_Y, cur_width * DENSITY):
            if cur_x == RES_X:
                cur_x = 0
            for x in range(RES_X):
                line_horizontal(cur_x, y, cur_width)
                if cur_x < RES_X:
                    cur_x += 1
                else:
                    cur_x = 0

        for x in range(0, RES_X, cur_width * DENSITY):
            line_vertical(x, cur_y, cur_width)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
