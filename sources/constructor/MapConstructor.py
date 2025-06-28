from ursina import *

from sources.constructor.entityconstructor import EntityConstructor
from sources.manager.EventManager import EventManager


class MapConstructor:
    _instance = None
    _initialized = False  # flag d'initialisation

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if MapConstructor._initialized:
            return  # ignore les appels suivants à __init__

        self.moving_objects = []
        self.walls = []
        self.props = []
        self.event_zones = []
        self.npc = []
        self.constructor = EntityConstructor()
        self.player = None

        MapConstructor._initialized = True

    def createMap(self):
        self.createWalls()
        self.createMovingObject()
        self.createProps()
        self.createEvent()
        self.createNpc()
        self.player = self.constructor.createPlayer()

    def createMovingObject(self):
        self.moving_objects = []

    def createWalls(self):
        self.walls = [
            self.constructor.createWall(position=(0, -5.5), scale=(20, 1)),  # bas
            self.constructor.createWall(position=(0, 5.5), scale=(20, 1)),  # haut
            self.constructor.createWall(position=(-9.5, 0), scale=(1, 12)),  # gauche
            self.constructor.createWall(position=(9.5, 0), scale=(1, 12)),  # droite
        ]

    def createProps(self):
        pass

    def createEvent(self):
        constructor = EntityConstructor()
        self.event_zones = [
            constructor.createEventZone(position=(3, 0),
                                        scale=(2, 2),
                                        callback=None, #EventManager().event(),
                                        name="secret_zone"),
        ]

    def createNpc(self):
        pass
