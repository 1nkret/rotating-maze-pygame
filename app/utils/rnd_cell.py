import random

from app.core.config import COLS, ROWS


def get_random_cell():
    return random.randint(0, COLS - 1), random.randint(0, ROWS - 1)
