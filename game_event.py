import pygame


events = {
    "QUIT": pygame.QUIT,
    "KEYDOWN": pygame.KEYDOWN,
    "KEYUP": pygame.KEYUP,
    "MOUSEBUTTONDOWN": pygame.MOUSEBUTTONDOWN
}


class PongEvent(object):
    """PongEvent: processes events for the pong game"""
    def __init__(self, game):
        super(PongEvent, self).__init__()
        self.game = game

    def process(self, event):
        for e in events:
            if events[e] == event.type:
                getattr(self, e)(event)

    def QUIT(self, event):
        self.game.done = True

    def KEYDOWN(self, event):
        self.QUIT(event)

    def KEYUP(self, event):
        pass

    def MOUSEBUTTONDOWN(self, event):
        pass
