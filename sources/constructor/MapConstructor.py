from PIL.ImageOps import scale
from ursina import *

from sources import constructor
from sources.constructor.ImageLoader import ImageLoader
from sources.constructor.entityconstructor import EntityConstructor
from sources.manager.EventManager import LionEvent, KidEvent, GuardEvent


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
            self.constructor.createWall((-9.5, 0), (1, 12), "brick"),  # gauche

            # Mur droit en deux parties pour laisser une ouverture au milieu
            self.constructor.createWall((9.5, 2.25), (1, 7.25), "brick"),  # partie haute
            self.constructor.createWall((9.5, -4.5), (1, 3), "brick"),  # partie basse
        ]

    def createDoors(self):
        img = ImageLoader()
        self.doors = {
            'east_door': self.constructor.createDoor((9.5, -2, -1), (1, 2), color.gray, False, "east_door", img.images["doors"]["first"]["closed"][0]),
            'real_east_door': self.constructor.createDoor((9.5, -2, 0.5), (1, 2), color.gray, False, "east_door", img.images["doors"]["first"]["door"][0])
        }
        self.doors['real_east_door'].visible = False

    def createProps(self):
        pass

    def createEvent(self):
        constructor = EntityConstructor()
        self.event_zones = {

            "lion" : constructor.createEventZone(position=(0, 4.5, 0.5),
                                        scale=(4, 1.5),
                                        callback=LionEvent,  # EventManager().event(),
                                        name="secret_zone",
                                        color_value=color.yellow,
                                        sound="lion_grr"),

            "baby" : constructor.createEventZone(position=(-3, -4.5, 0.5),
                                        scale=(4, 1.5),
                                        callback=KidEvent,  # EventManager().event(),
                                        name="secret_zone",
                                        color_value=color.yellow,
                                        sound="baby_cry"),

            "guard" : constructor.createEventZone(position=(7, -2.5, 0.5),
                                        scale=(2, 3),
                                        callback=GuardEvent,  # EventManager().event(),
                                        name="secret_zone",
                                        color_value=color.orange,
                                        ),
        }

    def createNpc(self):
        img = ImageLoader()
        constructor = EntityConstructor()
        self.npcs = {
            "poussette" : constructor.createNPC(position=(-4, -8, 0.5),
                                                scale=(2, 2),
                                                texture=img.images["pnj"]["poussette"]["still"][0],
                                                ),
            "lion": constructor.createNPC(position=(0, 8, 0.5),
                                               scale=(3, 2),
                                               texture=img.images["pnj"]["lion"]["sit"][0],
                                               ),
        }



    def createGrass(self):
        ground = Entity(
            model='quad',
            scale=(20, 12),
            position=(0, 0, 1),
            texture='grass',
            color=color.green,
        )