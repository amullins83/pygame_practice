import pygame
import global_vars as g


events = {
    "QUIT": pygame.QUIT,
    "KEYDOWN": pygame.KEYDOWN,
    "KEYUP": pygame.KEYUP,
    "MOUSEBUTTONDOWN": pygame.MOUSEBUTTONDOWN
}


def process(event):
    for e in events:
        if events[e] == event.type:
            globals()[e](event)


def QUIT(event):
    g.done = True


def KEYDOWN(event):
    QUIT(event)


def KEYUP(event):
    pass


def MOUSEBUTTONDOWN(event):
    pass
