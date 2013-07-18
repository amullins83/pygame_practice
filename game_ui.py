import pygame
from colors import *


class PongUI(object):
    """The UI for Pong"""
    def __init__(self, screen, logic):
        super(PongUI, self).__init__()
        self.screen = screen
        self.logic = logic
        self.font = pygame.font.Font("fonts/Romulus.ttf", 72)

    def update(self):
        self.screen.fill(white)
        self.draw()
        pygame.display.flip()

    def draw(self):
        self.drawField()
        self.drawScore()
        self.drawPads()
        self.drawBall()
        self.drawMessage()

    def drawField(self):
        pygame.draw.line(self.screen, blue, [self.screen.get_width() / 2, 0], [self.screen.get_width() / 2, self.screen.get_height()], 5)

    def drawScore(self):
        scoreOffsetX = 50
        scoreOffsetY = 50
        sign = [-1, 1]
        i = 0
        for points in self.logic.score:
            score = self.font.render(str(points), 0, blue)
            self.screen.blit(score, (self.screen.get_width() / 2 + sign[i]*scoreOffsetX - score.get_width() / 2, scoreOffsetY))
            i += 1

    def drawPads(self):
        for pad in self.logic.pads:
            pygame.draw.rect(self.screen, pad.color, [pad.pos.x, pad.pos.y, pad.size.width, pad.size.height])

    def drawBall(self):
        ball = self.logic.ball
        pygame.draw.ellipse(self.screen, ball.color, [ball.pos.x, ball.pos.y, ball.size.width, ball.size.height])

    def drawMessage(self):
        message = self.font.render(self.logic.message, 0, blue)
        self.screen.blit(message, (self.screen.get_width() / 2 - message.get_width() / 2, self.screen.get_height() / 2 - message.get_height() / 2))
