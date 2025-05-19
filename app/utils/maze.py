import random
import pygame
from app.core.config import CELL_SIZE, COLS, ROWS, WIN, WHITE, GREEN


def create_empty_grid():
    return [[{'visited': False, 'walls': [True, True, True, True]} for _ in range(COLS)] for _ in range(ROWS)]


def remove_wall(grid, cx, cy, nx, ny):
    dx = nx - cx
    dy = ny - cy
    if dx == 1:
        grid[cy][cx]['walls'][1] = False
        grid[ny][nx]['walls'][3] = False
    elif dx == -1:
        grid[cy][cx]['walls'][3] = False
        grid[ny][nx]['walls'][1] = False
    elif dy == 1:
        grid[cy][cx]['walls'][2] = False
        grid[ny][nx]['walls'][0] = False
    elif dy == -1:
        grid[cy][cx]['walls'][0] = False
        grid[ny][nx]['walls'][2] = False


def generate_maze(grid):
    stack = [(0, 0)]
    grid[0][0]['visited'] = True
    while stack:
        cx, cy = stack[-1]
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < COLS and 0 <= ny < ROWS and not grid[ny][nx]['visited']:
                neighbors.append((nx, ny))
        if neighbors:
            nx, ny = random.choice(neighbors)
            remove_wall(grid, cx, cy, nx, ny)
            grid[ny][nx]['visited'] = True
            stack.append((nx, ny))
        else:
            stack.pop()
    return grid


def draw_maze(grid):
    for y in range(ROWS):
        for x in range(COLS):
            walls = grid[y][x]['walls']
            px, py = x * CELL_SIZE, y * CELL_SIZE
            if walls[0]:
                pygame.draw.line(WIN, WHITE, (px, py), (px + CELL_SIZE, py), 2)
            if walls[1]:
                pygame.draw.line(WIN, WHITE, (px + CELL_SIZE, py), (px + CELL_SIZE, py + CELL_SIZE), 2)
            if walls[2]:
                pygame.draw.line(WIN, WHITE, (px + CELL_SIZE, py + CELL_SIZE), (px, py + CELL_SIZE), 2)
            if walls[3]:
                pygame.draw.line(WIN, WHITE, (px, py + CELL_SIZE), (px, py), 2)


def draw_exit(x, y):
    pygame.draw.rect(WIN, GREEN, (x * CELL_SIZE + 10, y * CELL_SIZE + 10, CELL_SIZE - 20, CELL_SIZE - 20))


def rotate_maze(grid, player_x, player_y, end_x, end_y):
    size = len(grid)
    new_grid = [[{'visited': True, 'walls': [False, False, False, False]} for _ in range(size)] for _ in range(size)]

    for y in range(size):
        for x in range(size):
            cell = grid[y][x]
            new_x = size - 1 - y
            new_y = x

            old_walls = cell['walls']
            rotated_walls = [
                old_walls[3],
                old_walls[0],
                old_walls[1],
                old_walls[2],
            ]

            new_grid[new_y][new_x]['walls'] = rotated_walls

    new_player_x = size - 1 - player_y
    new_player_y = player_x

    new_end_x = size - 1 - end_y
    new_end_y = end_x

    return new_grid, new_player_x, new_player_y, new_end_x, new_end_y
