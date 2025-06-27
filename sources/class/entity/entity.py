import collidebox


class Entity:
    def __init__(self, x: int = 0, y: int = 0, isVisible: bool = False, isTangible: bool = False, width: int = 0, height: int = 0):
        self.x = x
        self.y = y
        self.isVisible = isVisible
        self.isTangible = isTangible
        self.box = collidebox.CollideBox(x, y, width, height)

    def playSound(self):
        pass
