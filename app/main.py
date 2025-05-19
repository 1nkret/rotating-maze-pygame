import pygame
import sys

from app.core.config import WIN, clock, WHITE, GREEN, BLACK, MOVE_DELAY, difficulty_settings, records
from app.utils.files import save_records
from app.utils.maze import create_empty_grid, generate_maze, draw_maze, draw_exit, rotate_maze
from app.utils.menu import show_menu, show_end_screen
from app.utils.player import Player
from app.utils.rnd_cell import get_random_cell


def start_new_game(selected_difficulty):
    settings = difficulty_settings[selected_difficulty]
    rotate_interval = settings["rotate_interval"]
    time_limit = settings["time_limit"] * 1000
    grid = create_empty_grid()
    generate_maze(grid)
    start_x, start_y = get_random_cell()
    end_x, end_y = get_random_cell()
    while abs(end_x - start_x) + abs(end_y - start_y) < 6:
        end_x, end_y = get_random_cell()
    player = Player(start_x, start_y)
    return grid, player, end_x, end_y, rotate_interval, time_limit


def game_loop(selected_difficulty):
    grid, player, end_x, end_y, rotate_interval, time_limit = start_new_game(selected_difficulty)
    running = True
    start_time = pygame.time.get_ticks()
    last_move_time = 0
    last_rotate_time = pygame.time.get_ticks()
    font = pygame.font.SysFont(None, 48)

    while running:
        clock.tick(60)
        elapsed_time = pygame.time.get_ticks() - start_time
        WIN.fill(BLACK)
        draw_maze(grid)
        player.draw()
        draw_exit(end_x, end_y)

        if elapsed_time > time_limit:
            result = show_end_screen("Час вийшов!")
            if result == "restart":
                return "restart"
            if result == "change_difficulty":
                return "change_difficulty"

        if player.x == end_x and player.y == end_y:
            elapsed_sec = elapsed_time // 1000
            best_time = records.get(selected_difficulty)
            if best_time is None or elapsed_sec < best_time:
                records[selected_difficulty] = elapsed_sec
                save_records(records)
                message = f"Новий рекорд: {elapsed_sec} сек!"
            else:
                message = f"Пройдено за {elapsed_sec} сек"
            result = show_end_screen(message)
            if result == "restart":
                return "restart"
            if result == "change_difficulty":
                return "change_difficulty"

        remaining_time = max(0, (time_limit - elapsed_time) // 1000)
        WIN.blit(font.render(f"{remaining_time} sec", True, WHITE), (10, 10))
        best = records.get(selected_difficulty)
        if best:
            WIN.blit(font.render(f"Best: {best} sec", True, GREEN), (10, 50))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()

        if current_time - last_move_time > MOVE_DELAY:
            if keys[pygame.K_LEFT]:
                player.move(-1, 0, grid)
                last_move_time = current_time
            elif keys[pygame.K_RIGHT]:
                player.move(1, 0, grid)
                last_move_time = current_time
            elif keys[pygame.K_UP]:
                player.move(0, -1, grid)
                last_move_time = current_time
            elif keys[pygame.K_DOWN]:
                player.move(0, 1, grid)
                last_move_time = current_time

        if current_time - last_rotate_time > rotate_interval:
            grid, player.x, player.y, end_x, end_y = rotate_maze(grid, player.x, player.y, end_x, end_y)
            last_rotate_time = current_time


def main():
    pygame.init()
    pygame.display.set_caption("Maze Game")
    while True:
        selected_difficulty = show_menu()
        while True:
            result = game_loop(selected_difficulty)
            if result == "change_difficulty":
                break


if __name__ == "__main__":
    main()
