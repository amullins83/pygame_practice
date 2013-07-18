import pygame
from colors import *


class PongUI(object):
    """The UI for Pong"""
    def __init__(self, screen, logic):
        super(PongUI, self).__init__()
        self.screen = screen
        self.logic = logic

    def update(self):
        self.screen.fill(white)
        self.draw()
        pygame.display.flip()

    def draw(self):
        self.drawField()
        self.drawScore()
        self.drawPads()
        self.drawBall()

    def drawField(self):
        pygame.draw.line(self.screen, blue, [self.screen.get_width() / 2, 0], [self.screen.get_width() / 2, self.screen.get_height()], 5)

    def drawScore(self):
        font = pygame.font.Font("fonts/Romulus.ttf", 72)
        score = []
        for points in self.logic.score:
            score.append(font.render(str(points), 0, blue))

        scoreOffsetX = 50
        scoreOffsetY = 50

        self.screen.blit(score[0], (self.screen.get_width() / 2 - scoreOffsetX - score[0].get_width() / 2, scoreOffsetY))
        self.screen.blit(score[1], (self.screen.get_width() / 2 + scoreOffsetX - score[1].get_width() / 2, scoreOffsetY))

    def drawPads(self):
        for pad in self.logic.pads:
            pygame.draw.rect(self.screen, pad.color, [pad.pos.x, pad.pos.y, pad.size.width, pad.size.height])

    def drawBall(self):
        ball = self.logic.ball
        pygame.draw.ellipse(self.screen, ball.color, [ball.pos.x, ball.pos.y, ball.size.width, ball.size.height])
