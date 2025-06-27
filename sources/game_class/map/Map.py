from sources.game_class.entity.entity import Entity
from sources.game_class.entity.player import Player
from sources.game_class.entity.collidebox import CollideBox
from sources.game_class.entity.block import Block


class Map:

    """Constructor of class"""
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        self.entityList = []
        self.blockList = []
        self.player = None

    def addEntity(self, entity : Entity):
        self.entityList.append(entity)

    def addBlock(self, block : Block):
        self.blockList.append(block)

    def removeEntity(self, entity: Entity):
        if entity in self.entityList:
            self.entityList.remove(entity)

    def removeBlock(self, block: Block):
        if block in self.blockList:
            self.blockList.remove(block)


