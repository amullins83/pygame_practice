import pygame
from colors import *
import game_ui
from game_logic import PongLogic


class Test_ui():
    def setUp(self):
        pygame.init()
        self.width = 600
        self.height = 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.logic = PongLogic(self.width, self.height)
        game_ui.update(self.screen, self.logic)

    def test_size(self):
        assert self.screen.get_width() == self.width
        assert self.screen.get_height() == self.height

    def test_rectangle(self):
        assert self.screen.get_at((80, 100)) == red

    def test_ellipse(self):
        assert self.screen.get_at((300, 300)) == green

    def test_fillwhite(self):
        assert self.screen.get_at((0, 0)) == white

    def tearDown(self):
        self.screen = 0
        pygame.quit()
