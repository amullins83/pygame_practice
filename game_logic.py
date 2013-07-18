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
        self.pos = PongPos(pos.x, pos.y)
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

        # Randomly choose one of four starting directions
        self.directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        self.speed = 10
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

    def update(self):
        if self.status == Running:
            if self.hitDetector.didHitXBoundary(self.ball):
                print("Boundary X Hit")
                if self.width - self.ball.pos.x <= Ball.defaultSize:
                    self.score[0] += 1
                    if self.score[0] >= self.scoreMax:
                        self.status = Player1Win
                        print("Player 1 Wins")
                else:
                    self.score[1] += 1
                    if self.score[1] >= self.scoreMax:
                        self.status = Player2Win
                        print("Player 2 Wins")
                print("Player 1: " + str(self.score[0]) + ", Player 2: " + str(self.score[1]))
                self.ball.restart(self.ballStart)

            else:
                if self.hitDetector.collision(self.ball, self.pad1) or self.hitDetector.collision(self.ball, self.pad2):
                    self.ball.velocity.x = -self.ball.velocity.x
                    print("Pad Hit")
                elif self.hitDetector.didHitYBoundary(self.ball):
                    self.ball.velocity.y = -self.ball.velocity.y
                    print("Boundary Y Hit")

                self.ball.pos.x += self.ball.velocity.x
                self.ball.pos.y += self.ball.velocity.y
