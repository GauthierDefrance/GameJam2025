import collidebox

class Block:
    def __init__(self, x: int = 0, y: int = 0, z : int = 0, width: int = 32, height: int = 32, texture = None):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.isVisible = True
        self.isTangible = True
        self.box = collidebox.CollideBox(x, y, width, height)
        self.texture = texture