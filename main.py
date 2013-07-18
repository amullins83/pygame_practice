import pygame
from game_logic import PongLogic
from game_ui import PongUI
from game_event import PongEvent


class Pong(object):
    """Pong game"""
    def __init__(self, width, height):
        super(Pong, self).__init__()
        self.width = width
        self.height = height
        self.size = (self.width, self.height)

        self.initializeScreen()

        pygame.init()

        self.restart()
        self.main()

        pygame.quit()

    def initializeScreen(self):
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Pong")

    def main(self):
        self.done = False
        while not self.done:
            for event in pygame.event.get():
                self.eventRunner.process(event)

            self.logic.update()

            self.ui.update()

            self.clock.tick(60)
            if not __name__ == "__main__":
                self.done = True

    def pressKey(self, key):
        self.logic.pressKey(key)

    def releaseKey(self, key):
        self.logic.releaseKey(key)

    def running(self):
        return self.logic.running()

    def restart(self):
        self.clock = pygame.time.Clock()
        self.eventRunner = PongEvent(self)
        self.logic = PongLogic(self.width, self.height)
        self.ui = PongUI(self.screen, self.logic)

if __name__ == "__main__":
    Pong(600, 400)
