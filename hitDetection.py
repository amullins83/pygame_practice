class HitDetector(object):
    """docstring for HitDetector"""
    def __init__(self, xstart, ystart, xend, yend):
        super(HitDetector, self).__init__()
        self.boundary = ((xstart, ystart), (xend, yend))

    def didHitXBoundary(self, thing):
        return (thing.pos.x <= self.boundary[0][0]) or ((thing.pos.x + thing.size.width) >= self.boundary[1][0])

    def didHitYBoundary(self, thing):
        return (thing.pos.y <= self.boundary[0][1]) or ((thing.pos.y + thing.size.height) >= self.boundary[1][1])

    def collision(self, thing1, thing2):
        collided = collidedVert = collidedHoriz = False
        if thing1.left() <= thing2.left():
            collidedHoriz = thing1.right() >= thing2.left()
        else:
            collidedHoriz = thing1.left() <= thing2.right()

        if thing1.top() <= thing2.top():
            collidedVert = thing1.bottom() >= thing2.top()
        else:
            collidedVert = thing1.top() <= thing2.bottom()

        collided = collidedVert and collidedHoriz

        if collided:
            print(thing1.name + "(" + str(thing1.left()) + ", " + str(thing1.top()) + ") collided with " + thing2.name + "(" + str(thing2.left()) + ", " + str(thing2.top()) + ")")

        return collided
