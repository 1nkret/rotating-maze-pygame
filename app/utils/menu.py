import sys
import pygame

from app.core.config import WIN, WHITE, GREEN, BLACK, RED, difficulty_settings, WIDTH, records


def show_menu():
    menu_font = pygame.font.SysFont(None, 48)
    small_font = pygame.font.SysFont(None, 32)
    options = ["Новачок", "Середня", "Тяжко", "Неможливо"]
    selected = 0

    while True:
        WIN.fill(BLACK)
        title = menu_font.render("Оберіть складність", True, WHITE)
        WIN.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))

        for i, option in enumerate(options):
            color = GREEN if i == selected else WHITE
            text = small_font.render(option, True, color)
            WIN.blit(text, (WIDTH // 2 - text.get_width() // 2, 150 + i * 50))

        record_y = 400
        for diff in difficulty_settings:
            best = records.get(diff)
            record_text = f"{diff}: {best} сек" if best else f"{diff}: -"
            rec_surf = small_font.render(record_text, True, WHITE)
            WIN.blit(rec_surf, (WIDTH // 2 - rec_surf.get_width() // 2, record_y))
            record_y += 30

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    return options[selected]


def show_end_screen(message):
    menu_font = pygame.font.SysFont(None, 48)
    small_font = pygame.font.SysFont(None, 32)
    options = ["Рестарт", "Змінити складність", "Вийти"]
    selected = 0

    while True:
        WIN.fill(BLACK)
        title = menu_font.render(message, True, RED)
        WIN.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))

        for i, option in enumerate(options):
            color = GREEN if i == selected else WHITE
            text = small_font.render(option, True, color)
            WIN.blit(text, (WIDTH // 2 - text.get_width() // 2, 200 + i * 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    command = options[selected]
                    if command == "Вийти":
                        pygame.quit()
                        sys.exit()
                    elif command == "Рестарт":
                        return "restart"
                    elif command == "Змінити складність":
                        return "change_difficulty"
