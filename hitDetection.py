class HitDetector(object):
    """docstring for HitDetector"""
    def __init__(self, xstart, ystart, xend, yend):
        super(HitDetector, self).__init__()
        self.boundary = ((xstart, ystart), (xend, yend))

    def didHitXBoundary(self, thing):
        return (thing.left() <= self.boundary[0][0] and thing.velocity.x < 0) or (thing.right() >= self.boundary[1][0] and thing.velocity.x > 0)

    def didHitYBoundary(self, thing):
        return (thing.top() <= self.boundary[0][1] and thing.velocity.y < 0) or (thing.bottom() >= self.boundary[1][1] and thing.velocity.y > 0)

    def didCollide(self, thing1, thing2):
        return self.didCollideHoriz(thing1, thing2) or self.didCollideVert(thing1, thing2)

    def didCollideVert(self, thing1, thing2):
        return self.didCollideTop(thing1, thing2) or self.didCollideBottom(thing1, thing2)

    def didCollideHoriz(self, thing1, thing2):
        return self.didCollideLeft(thing1, thing2) or self.didCollideRight(thing1, thing2)

    def didCollideTop(self, thing1, thing2):
        return thing1.velocity.y > thing2.velocity.y and \
        thing1.bottom() >= thing2.top() and \
        (thing1.bottom() - thing2.top()) <= (thing1.velocity.y - thing2.velocity.y) and \
        self.inside(thing1, thing2)

    def didCollideBottom(self, thing1, thing2):
        return thing1.velocity.y < thing2.velocity.y and \
        thing1.top() <= thing2.bottom() and \
        (thing2.bottom() - thing1.top()) <= (thing2.velocity.y - thing1.velocity.y) and \
        self.inside(thing1, thing2)

    def didCollideLeft(self, thing1, thing2):
        return thing1.velocity.x > thing2.velocity.x and \
        thing1.right() >= thing2.left() and \
        (thing1.right() - thing2.left()) <= (thing1.velocity.x - thing2.velocity.x) and \
        self.inside(thing1, thing2)

    def didCollideRight(self, thing1, thing2):
        return thing1.velocity.x < thing2.velocity.x and \
        thing1.left() <= thing2.right() and \
        (thing2.right() - thing1.left()) <= (thing2.velocity.x - thing1.velocity.x) and \
        self.inside(thing1, thing2)

    def inside(self, thing1, thing2):
        return self.insideHoriz(thing1, thing2) and self.insideVert(thing1, thing2)

    def insideHoriz(self, thing1, thing2):
        return thing1.right() >= thing2.left() and thing1.left() <= thing2.right()

    def insideVert(self, thing1, thing2):
        return thing1.bottom() >= thing2.top() and thing1.top() <= thing2.bottom()
