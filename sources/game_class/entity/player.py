from entity import Entity


class Player(Entity):
    def __init__(self, x: int = 0, y: int = 0, isVisible: bool = False, isTangible: bool = False, width: int = 0, height: int = 0, texture = None):
        super().__init__(x, y, isVisible, isTangible, width, height, texture)