import pygame
from colors import *
from hitDetection import HitDetector
from random import randint

Running, Player1Win, Player2Win = range(3)
Keys = [pygame.K_s, pygame.K_w, pygame.K_DOWN, pygame.K_UP]


class PongPos(object):
    """docstring for PongPos"""
    def __init__(self, x=0, y=0):
        super(PongPos, self).__init__()
        self.x = x
        self.y = y


class PongSize(object):
    """docstring for PongSize"""
    def __init__(self, width=0, height=0):
        super(PongSize, self).__init__()
        self.width = width
        self.height = height


class PongObject(object):
    """docstring for PongObject"""
    def __init__(self, name, pos=PongPos(), size=PongSize(), color=black):
        super(PongObject, self).__init__()
        self.name = name
        self.pos = PongPos(pos.x, pos.y)
        self.history = []
        self.size = size
        self.color = color
        self.velocity = PongPos()

    def left(self):
        return self.pos.x

    def right(self):
        return self.pos.x + self.size.width

    def top(self):
        return self.pos.y

    def bottom(self):
        return self.pos.y + self.size.height


class Pad(PongObject):
    """docstring for Pad"""
    defaultHeight = 100
    defaultWidth = 10

    def __init__(self, name, pos=PongPos()):
        super(Pad, self).__init__(name, pos, PongSize(Pad.defaultWidth, Pad.defaultHeight), red)
        self.speed = 3

    def startMove(self, directionDown):
        if directionDown:
            self.velocity.y = -self.speed
        else:
            self.velocity.y = self.speed

    def endMove(self, directionDown):
        if (self.velocity.y < 0 and directionDown) or (self.velocity.y > 0 and not directionDown):
            self.velocity.y = 0


class Ball(PongObject):
    """docstring for Ball"""
    defaultSize = 20

    def __init__(self, pos=PongPos()):
        super(Ball, self).__init__("ball", pos, PongSize(Ball.defaultSize, Ball.defaultSize), green)

        # Randomly choose one of four starting directions
        self.directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        self.speed = 5
        self.restart(pos)

    def restart(self, pos=PongPos()):
        i = randint(0, 3)
        self.velocity = PongPos(self.speed*self.directions[i][0], self.speed*self.directions[i][1])
        self.pos = PongPos(pos.x, pos.y)


class PongLogic(object):
    """docstring for PongLogic"""
    def __init__(self, width, height):
        super(PongLogic, self).__init__()

        self.status = Running

        self.width = width
        self.height = height

        self.ballSize = Ball.defaultSize
        self.ballStart = PongPos((self.width - self.ballSize) / 2,
                                 (self.height - self.ballSize) / 2)

        self.padStartOffsets = PongPos(50, 10)

        self.pad1Start = self.padStartOffsets
        self.pad2Start = PongPos(self.width - self.padStartOffsets.x - Pad.defaultWidth,
                                 self.height - self.padStartOffsets.y - Pad.defaultHeight)

        self.ball = Ball(self.ballStart)
        self.pad1 = Pad("1", self.pad1Start)
        self.pad2 = Pad("2", self.pad2Start)

        self.score = [0, 0]
        self.scoreMax = 10

        self.hitDetector = HitDetector(0, 0, 600, 400)
        self.pads = [self.pad1, self.pad2]

        self.message = ""

    def keyResponse(self, key, func):
        if self.status == Running:
            for i in range(len(Keys)):
                if key == Keys[i]:
                    if i < 2:
                        getattr(self.pad1, func)(i)
                    else:
                        getattr(self.pad2, func)(i - 2)
                    break

    def pressKey(self, key):
        self.keyResponse(key, "startMove")

    def releaseKey(self, key):
        self.keyResponse(key, "endMove")

    def update(self):
        if self.status == Running:
            self.updateBall()
            for pad in self.pads:
                self.updatePad(pad)

    def updateBall(self):
        if self.hitDetector.didHitXBoundary(self.ball):
            self.updateScore()
        else:
            self.checkPadHit()
            self.checkBoundary()
            self.incrementBallPosition()

    def updateScore(self):
        if self.width - self.ball.pos.x <= Ball.defaultSize:
            self.score[0] += 1
            if self.score[0] >= self.scoreMax:
                self.status = Player1Win
                self.message = "Player 1 Wins"
        else:
            self.score[1] += 1
            if self.score[1] >= self.scoreMax:
                self.status = Player2Win
                self.message = "Player 2 Wins"
        self.ball.restart(self.ballStart)

    def checkPadHit(self):
        if self.hitDetector.didCollide(self.ball, self.pad1) or self.hitDetector.didCollide(self.ball, self.pad2):
            if self.hitDetector.didCollideRight(self.ball, self.pad1) or self.hitDetector.didCollideLeft(self.ball, self.pad2):
                self.ball.velocity.x = -self.ball.velocity.x

            if self.hitDetector.didCollideVert(self.ball, self.pad1) or self.hitDetector.didCollideVert(self.ball, self.pad2):
                self.ball.velocity.y = -self.ball.velocity.y

    def checkBoundary(self):
        if self.hitDetector.didHitYBoundary(self.ball):
                self.ball.velocity.y = -self.ball.velocity.y

    def incrementBallPosition(self):
        self.ball.pos.x += self.ball.velocity.x
        self.ball.pos.y += self.ball.velocity.y

    def updatePad(self, pad):
        if self.hitDetector.didHitYBoundary(pad):
            if pad.bottom() > self.height/2:
                pad.pos.y = self.height - pad.size.height
            else:
                pad.pos.y = 0
        else:
            pad.pos.y += pad.velocity.y

    def running(self):
        return self.status == Running
