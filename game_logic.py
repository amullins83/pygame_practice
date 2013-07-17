from colors import *
from hitDetection import HitDetector
from random import randint

Running, Player1Win, Player2Win = range(3)


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
        self.pos = pos
        self.history = []
        self.size = size
        self.color = color

    def left(self):
        return self.pos.x

    def right(self):
        return self.pos.x + self.size.width

    def top(self):
        return self.pos.y

    def bottom(self):
        return self.pos.y + self.size.height

    def didCollide(self, otherObject, hitDetector):
        return hitDetector.collision(self, otherObject)


class Pad(PongObject):
    """docstring for Pad"""
    defaultHeight = 100
    defaultWidth = 10

    def __init__(self, name, pos=PongPos()):
        super(Pad, self).__init__(name, pos, PongSize(Pad.defaultWidth, Pad.defaultHeight), red)


class Ball(PongObject):
    """docstring for Ball"""
    defaultSize = 20

    def __init__(self, pos=PongPos()):
        super(Ball, self).__init__("ball", pos, PongSize(Ball.defaultSize, Ball.defaultSize), green)

        # Random initial velocity, don't allow 0, 0
        self.velocity = PongPos()
        while self.velocity == PongPos():
            self.velocity = PongPos(randint(-1, 1), randint(-1, 1))


class PongLogic(object):
    """docstring for PongLogic"""
    def __init__(self, width, height):
        super(PongLogic, self).__init__()

        self.status = Running

        self.width = width
        self.height = height

        self.ballSize = 20
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

    def update(self):
        if self.status == Running:
            if self.ball.didCollide(self.pad1, self.hitDetector) or self.ball.didCollide(self.pad2, self.hitDetector):
                self.ball.velocity.x = -self.ball.velocity.x

            if self.hitDetector.didHitYBoundary(self.ball):
                self.ball.velocity.y = -self.ball.velocity.y

            if self.hitDetector.didHitXBoundary(self.ball):
                if self.ball.pos.x < 20:
                    self.score[0] += 1
                    if self.score[0] >= self.scoreMax:
                        self.status = Player1Win
                else:
                    self.score[1] += 1
                    if self.score[1] >= self.scoreMax:
                        self.status = Player2Win

                self.ball = Ball(self.ballStart)

            self.ball.pos.x += self.ball.velocity.x
            self.ball.pos.y += self.ball.velocity.y
