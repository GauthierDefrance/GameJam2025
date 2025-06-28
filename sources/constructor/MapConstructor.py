from ursina import *

from sources.constructor.ImageLoader import ImageLoader
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
        self.doors = []
        self.constructor = EntityConstructor()
        self.player = None

        MapConstructor._initialized = True

    def createMap(self):
        self.createWalls()
        self.createMovingObject()
        self.createProps()
        self.createEvent()
        self.createNpc()
        self.createDoors()
        self.createGrass()
        self.player = self.constructor.createPlayer()

    def createMovingObject(self):
        self.moving_objects = []

    def createWalls(self):
        self.walls = [
            self.constructor.createWall((0, -5.5), (20, 1), "brick"),  # bas
            self.constructor.createWall((0, 5.5), (20, 1), "brick"),  # haut
            self.constructor.createWall(position=(-9.5, 0), scale=(1, 12)),  # gauche

            # Mur droit en deux parties pour laisser une ouverture au milieu
            self.constructor.createWall(position=(9.5, 2.5), scale=(1, 7)),  # partie haute
            self.constructor.createWall(position=(9.5, -4.5), scale=(1, 3)),  # partie basse
        ]

    def createDoors(self):
        img = ImageLoader()
        self.doors = {
            'east_door': self.constructor.createDoor((9.5, -2), (1, 2), color.gray, True, "east_door", img.images["doors"]["first"]["open"][0])
        }

    def createProps(self):
        pass

    def createEvent(self):
        constructor = EntityConstructor()
        self.event_zones = [
            constructor.createEventZone(position=(3, 0),
                                        scale=(1, 1),
                                        callback=None, #EventManager().event(),
                                        name="secret_zone"),
        ]

    def createNpc(self):
        pass



    def createGrass(self):
        ground = Entity(
            model='quad',
            scale=(20, 12),
            position=(0, 0, 1),
            texture='grass',
            color=color.green,
        )