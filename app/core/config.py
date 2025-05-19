import pygame
from app.utils.files import load_records

WIDTH, HEIGHT = 600, 600
CELL_SIZE = 40
COLS = WIDTH // CELL_SIZE
ROWS = HEIGHT // CELL_SIZE

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

MOVE_DELAY = 100

difficulty_settings = {
    "Новачок": {"rotate_interval": 10000, "time_limit": 60},
    "Середня": {"rotate_interval": 7000, "time_limit": 45},
    "Тяжко": {"rotate_interval": 5000, "time_limit": 30},
    "Неможливо": {"rotate_interval": 3000, "time_limit": 15},
}

records = load_records()
