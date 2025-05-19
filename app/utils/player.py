import pygame
from app.core.config import CELL_SIZE, WIN, BLUE, COLS, ROWS


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy, grid):
        nx, ny = self.x + dx, self.y + dy
        if not (0 <= nx < COLS and 0 <= ny < ROWS):
            return

        walls = grid[self.y][self.x]['walls']
        if dx == -1 and not walls[3]:
            self.x -= 1
        elif dx == 1 and not walls[1]:
            self.x += 1
        elif dy == -1 and not walls[0]:
            self.y -= 1
        elif dy == 1 and not walls[2]:
            self.y += 1

    def draw(self):
        pygame.draw.rect(WIN, BLUE, (self.x * CELL_SIZE + 5, self.y * CELL_SIZE + 5, CELL_SIZE - 10, CELL_SIZE - 10))
