import pygame
from colors import *


def update(screen, logic):
    screen.fill(white)
    draw(screen, logic)
    pygame.display.flip()


def draw(screen, logic):
    pygame.draw.line(screen, blue, [screen.get_width() / 2, 0], [screen.get_width() / 2, screen.get_height()], 5)

    for pad in logic.pads:
        pygame.draw.rect(screen, pad.color, [pad.pos.x, pad.pos.y, pad.size.width, pad.size.height])

    pygame.draw.ellipse(screen, logic.ball.color, [logic.ball.pos.x, logic.ball.pos.y, logic.ball.size.width, logic.ball.size.height])
