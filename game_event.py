import pygame
import global_vars as g


events = [pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP, pygame.MOUSEBUTTONDOWN]


def process(event):
    for e in events:
        if e == event:
            getattr(__name__, e.__name__)()


def QUIT():
    g.done = True


def KEYDOWN():
    pass


def KEYUP():
    pass


def MOUSEBUTTONDOWN():
    pass
