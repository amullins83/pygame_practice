import pygame
from game_logic import PongLogic
import game_ui
from game_event import PongEvent


class Pong(object):
    """Pong game"""
    def __init__(self, width, height):
        super(Pong, self).__init__()

        pygame.init()

        self.initializeScreen(width, height)

        self.clock = pygame.time.Clock()
        self.eventRunner = PongEvent(self)
        self.logic = PongLogic(width, height)

        self.main()

        pygame.quit()

    def initializeScreen(self, width, height):
        self.size = (width, height)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Pong")

    def main(self):
        self.done = False
        while not self.done:
            for event in pygame.event.get():
                self.eventRunner.process(event)

            self.logic.update()

            game_ui.update(self.screen, self.logic)

            self.clock.tick(20)
            if not __name__ == "__main__":
                self.done = True

    def pressKey(self, key):
        self.logic.pressKey(key)

    def releaseKey(self, key):
        self.logic.releaseKey(key)


if __name__ == "__main__":
    Pong(600, 400)
