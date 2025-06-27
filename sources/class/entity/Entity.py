import CollideBox


class Entity:
    def __init__(self, x=0, y=0, isVisible=False, isTangible=False, CollideBox : box):
        self.x = x
        self.y = y
        self.isVisible = isVisible
        self.isTangible = isTangible

    def playSound(self):
        pass
