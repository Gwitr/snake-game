# NOTE: This was written very quickly, don't use this as an example on how to code a game please

import time
import pygame
import numpy as np
from random import randint as rand

font = {
    "S": np.array(
        [
            [1, 1, 1],
            [1, 0, 0],
            [1, 1, 1],
            [0, 0, 1],
            [1, 1, 1],
        ]
    ),
    "C": np.array(
        [
            [1, 1, 1],
            [1, 0, 0],
            [1, 0, 0],
            [1, 0, 0],
            [1, 1, 1],
        ]
    ),
    "O": np.array(
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1],
            [1, 1, 1],
        ]
    ),
    "R": np.array(
        [
            [1, 1, 0],
            [1, 0, 1],
            [1, 1, 0],
            [1, 1, 0],
            [1, 0, 1],
        ]
    ),
    "E": np.array(
        [
            [1, 1, 1],
            [1, 0, 0],
            [1, 1, 1],
            [1, 0, 0],
            [1, 1, 1],
        ]
    ),
    "8": np.array(
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
        ]
    ),
    "0": np.array(
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1],
            [1, 1, 1],
        ]
    ),
    "1": np.array(
        [
            [0, 0, 1],
            [0, 0, 1],
            [0, 0, 1],
            [0, 0, 1],
            [0, 0, 1],
        ]
    ),
    "2": np.array(
        [
            [1, 1, 1],
            [0, 0, 1],
            [1, 1, 1],
            [1, 0, 0],
            [1, 1, 1],
        ]
    ),
    "3": np.array(
        [
            [1, 1, 1],
            [0, 0, 1],
            [1, 1, 1],
            [0, 0, 1],
            [1, 1, 1],
        ]
    ),
    "4": np.array(
        [
            [1, 0, 1],
            [1, 0, 1],
            [1, 1, 1],
            [0, 0, 1],
            [0, 0, 1],
        ]
    ),
    "5": np.array(
        [
            [1, 1, 1],
            [1, 0, 0],
            [1, 1, 1],
            [0, 0, 1],
            [1, 1, 1],
        ]
    ),
    "8": np.array(
        [
            [1, 1, 1],
            [1, 0, 0],
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
        ]
    ),
    "7": np.array(
        [
            [1, 1, 1],
            [0, 0, 1],
            [0, 0, 1],
            [0, 0, 1],
            [0, 0, 1],
        ]
    ),
    "9": np.array(
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
            [0, 0, 1],
            [1, 1, 1],
        ]
    ),
    ":": np.array(
        [
            [0, 0, 0],
            [1, 0, 0],
            [0, 0, 0],
            [1, 0, 0],
            [0, 0, 0],
        ]
    ),
    " ": np.array(
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
    ),
}

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

RESOLUTION  = (320, 240)
SNAKE_SPEED = 0.1

def move_snake(fruit, snake, dir):
    global score
    
    last = snake[-1][:]
    if dir == UP:
        snake[-1][1] -= 1
    elif dir == DOWN:
        snake[-1][1] += 1
    elif dir == LEFT:
        snake[-1][0] -= 1
    elif dir == RIGHT:
        snake[-1][0] += 1

    if snake[-1] == fruit:
        fruit[0] = rand(0, RESOLUTION[0]) // 8
        fruit[1] = rand(0, RESOLUTION[1]) // 8
        snake.insert(-2, last)
        boop.play()
        score += 1

    if snake[-1][0] < 0:
        snake[-1][0] += RESOLUTION[0] // 8
    if snake[-1][1] < 0:
        snake[-1][1] += RESOLUTION[1] // 8
    if snake[-1][0] > (RESOLUTION[0] / 8):
        snake[-1][0] -= RESOLUTION[0] // 8 + 1
    if snake[-1][1] > (RESOLUTION[1] / 8):
        snake[-1][1] -= RESOLUTION[1] // 8 + 1

    if snake[-1] in snake[:-1]:
        return False

    for i in range(len(snake) - 2):
        snake[i] = snake[i+1]
    snake[len(snake) - 2] = last

    return True

def disp_char(xy, arr, char):
    chardata = font[char]
    for y, row in enumerate(chardata):
        for x, cell in enumerate(row):
            sx, ex = (x + xy[0]) * 8, (x + xy[0]) * 8 + 8
            sy, ey = (y + xy[1]) * 8, (y + xy[1]) * 8 + 8
            arr[sx:ex, sy:ey] = [cell * 255, cell * 255, cell * 255]

def disp_str(xy, arr, s):
    xy = [int(xy[0]), int(xy[1])]
    for i in s:
        disp_char(xy, arr, i)
        xy[0] += 4

pygame.mixer.init(22100, -16, 2, 64)
pygame.init()
display = pygame.display.set_mode(RESOLUTION, pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption("game")

score = None
boop = pygame.mixer.Sound("beep.wav")
beep = pygame.mixer.Sound("boop.wav")

beep.set_volume(0.4)
boop.set_volume(0.4)

clock = pygame.time.Clock()
def main():
    global display, clock, score

    score = 0
    run = True
    left = False
    right = False
    up = False
    down = False
    snake_segments = [[0, 0], [1, 0], [2, 0]]
    last_move = time.perf_counter()
    fruit = [rand(0, RESOLUTION[0]) // 8, rand(0, RESOLUTION[1]) // 8]
    while run:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    A = [snake_segments[-1][0], snake_segments[-1][1] - 1]
                    if snake_segments[-2] == A:
                        continue
                    up = True
                    down = False
                    left = False
                    right = False
                elif event.key == pygame.K_DOWN:
                    A = [snake_segments[-1][0], snake_segments[-1][1] + 1]
                    if snake_segments[-2] == A:
                        continue
                    up = False
                    down = True
                    left = False
                    right = False
                elif event.key == pygame.K_LEFT:
                    A = [snake_segments[-1][0] - 1, snake_segments[-1][1]]
                    if snake_segments[-2] == A:
                        continue
                    up = False
                    down = False
                    left = True
                    right = False
                elif event.key == pygame.K_RIGHT:
                    A = [snake_segments[-1][0] + 1, snake_segments[-1][1]]
                    if snake_segments[-2] == A:
                        continue
                    up = False
                    down = False
                    left = False
                    right = True


        alive = True
        if left:
            if time.perf_counter() - last_move > SNAKE_SPEED:
                alive = move_snake(fruit, snake_segments, LEFT)
                last_move = time.perf_counter()
        if right:
            if time.perf_counter() - last_move > SNAKE_SPEED:
                alive = move_snake(fruit, snake_segments, RIGHT)
                last_move = time.perf_counter()
        if up:
            if time.perf_counter() - last_move > SNAKE_SPEED:
                alive = move_snake(fruit, snake_segments, UP)
                last_move = time.perf_counter()
        if down:
            if time.perf_counter() - last_move > SNAKE_SPEED:
                alive = move_snake(fruit, snake_segments, DOWN)
                last_move = time.perf_counter()

        array = np.zeros((RESOLUTION[0], RESOLUTION[1], 3))
            
        if not alive:
            # Dead
            beep.play()
            print("You died!")
            for _ in range(60*4):
                clock.tick(60)
                x = (RESOLUTION[0] / 2) // 8 - 20
                y = (RESOLUTION[1] / 2) // 8 - 3
                disp_str((x, y), array, "SCORE: %03d" % (score))
                pygame.surfarray.blit_array(display, array)
                pygame.display.flip()
            return True

        for i in snake_segments:
            pygame.event.get()
            sx, ex = i[0]*8, i[0]*8+8
            sy, ey = i[1]*8, i[1]*8+8
            array[sx:ex, sy:ey] = [255, 255, 255]

        sx, ex = fruit[0]*8, fruit[0]*8+8
        sy, ey = fruit[1]*8, fruit[1]*8+8
        array[sx:ex, sy:ey] = [128, 128, 128]

        pygame.surfarray.blit_array(display, array)

        pygame.display.flip()

    pygame.quit()
    return False

while main():
    pass
