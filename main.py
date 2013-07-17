import pygame
import colors
import game_event
import game_logic
import game_ui
import global_vars as g


def main(width, height):
    pygame.init()
    colors.init()

    size = (width, height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Test Game")
    clock = pygame.time.Clock()

    g.done = False
    while not g.done:
        for event in pygame.event.get():
            game_event.process(event)

        game_logic.update()

        game_ui.update(screen)

        clock.tick(60)

if __name__ == "__main__":
    main()
