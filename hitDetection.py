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
        return False
