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
        img = ImageLoader()
        self.walls = [
            self.constructor.createWall((0, -5.5), (19, 1), img.images["wall"]["birdcage_wall_bottom"][0]),  # bas
            self.constructor.createWall((0, 5.5), (19, 1), img.images["wall"]["birdcage_wall_top"][0]),  # haut



            self.constructor.createWall((-4.75, 2.25, 2), (0.25, 0.5), "brick"),


            # Mur droit en deux parties pour laisser une ouverture au milieu
            self.constructor.createWall((-10.29, 0), (0.42, 10), img.images["wall"]["birdcage_wall_side"][0]),  # gauche
            self.constructor.createWall((10, 2), (0.42, 7), img.images["wall"]["birdcage_wall_side"][0]),
            self.constructor.createWall((10, -4.25), (0.42, 1.75), img.images["wall"]["birdcage_wall_side"][0]),  # partie basse


            # Coins
            self.constructor.createWall((-10, 5.5), (1, 1), img.images["wall"]["birdcage_wall_top_left_corner"][0]),
            # coin haut gauche
            self.constructor.createWall((9.7, 5.5), (1, 1), img.images["wall"]["birdcage_wall_top_right_corner"][0]),
            # coin haut droit
            self.constructor.createWall((-10, -5.5), (1, 1), img.images["wall"]["birdcage_wall_bottom_left_corner"][0]),
            # coin bas gauche
            self.constructor.createWall((9.7, -5.5), (1, 1), img.images["wall"]["birdcage_wall_bottom_right_corner"][0])
            # coin bas droit
        ]

    def createDoors(self):
        img = ImageLoader()
        self.doors = {
            'east_door': self.constructor.createDoor((10.35, -2, -1), (1.25, 3), color.gray, False, "east_door", img.images["doors"]["first"]["closed"][0]),
            'real_east_door': self.constructor.createDoor((10.35, -2, 0.2), (1.25, 3), color.gray, False, "east_door", img.images["doors"]["first"]["door"][0])
        }
        self.doors['real_east_door'].visible = False

    def createProps(self):
        img = ImageLoader()
        self.props = {
            "avocatier" : self.constructor.createProps(position=(-5, 5, -1), scale=(6,6), texture=img.images["props"]["avocatier"][0]),
        }



    def createEvent(self):
        constructor = EntityConstructor()
        self.event_zones = {

            "lion" : constructor.createEventZone(position=(0, 4.5, 0.5),
                                        scale=(4, 1.5),
                                        callback=LionEvent,  # EventManager().event(),
                                        name="secret_zone",
                                        color_value=color.yellow,
                                        sound="lion_grr",
                                        soundp="lion_grr"),

            "baby" : constructor.createEventZone(position=(-3, -4.5, 0.5),
                                        scale=(4, 1.5),
                                        callback=KidEvent,  # EventManager().event(),
                                        name="secret_zone",
                                        color_value=color.yellow,
                                        sound="baby_cry",
                                        soundp="baby_cry_loop"),

            "guard" : constructor.createEventZone(position=(7, -2.5, 0.5),
                                        scale=(5, 5),
                                        callback=GuardEvent,  # EventManager().event(),
                                        name="secret_zone",
                                        color_value=color.orange,
                                        ),

            "tuto": constructor.createEventZone(position=(-8, 0, 0.5),
                                                 scale=(4, 3), # EventManager().event(),
                                                 name="secret_zone",
                                                 color_value=color.blue,
                                                sound="tutos",
                                                soundp="tutos"
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
        img = ImageLoader()
        self.grounds = [ Entity(
            model='quad',
            scale=(20.3, 12),
            position=(0, 0, 1),
            texture='grass',
            color=color.green,
        ),
            self.constructor.createGrass(position=(0, -7, 0.6),scale=(22, 2),texture=img.images["ground"]["road"]["sidewalk"][0],),
            self.constructor.createGrass(position=(0, 0, 5),scale=(30, 30),texture=img.images["ground"]["road"]["basic"][0],texture_scale=(30,30)),
            self.constructor.createGrass(position=(10.75, -3, 0.3),scale=(1.5, 2),texture=img.images["ground"]["sidewalk"]["door"][0],),
            self.constructor.createGrass(position=(10.75, -4, 0.5),scale=(1.5, 2),texture=img.images["ground"]["sidewalk"]["right"][0],),
            self.constructor.createGrass(position=(10.75, -5, 0.51),scale=(1.5, 2),texture=img.images["ground"]["sidewalk"]["right"][0],),

            self.constructor.createGrass(position=(10.5, -7, 0.5),scale=(2, 2),texture=img.images["ground"]["sidewalk"]["bottom-right"][0],),
            self.constructor.createGrass(position=(10.5, -7, 0.51),scale=(2, 2),texture=img.images["ground"]["sidewalk"]["bottom"][0],),


            self.constructor.createGrass(position=(10.75, -1, 0.5), scale=(1.5, 2),texture=img.images["ground"]["sidewalk"]["right"][0], ),
            self.constructor.createGrass(position=(10.75, 1, 0.5), scale=(1.5, 2),texture=img.images["ground"]["sidewalk"]["right"][0], ),
            self.constructor.createGrass(position=(10.75, 3, 0.5), scale=(1.5, 2),texture=img.images["ground"]["sidewalk"]["right"][0], ),
            self.constructor.createGrass(position=(10.75, 5, 0.5), scale=(1.5, 2),texture=img.images["ground"]["sidewalk"]["right"][0], ),
            self.constructor.createGrass(position=(10.75, 5.5, 0.4), scale=(1.5, 1),texture=img.images["ground"]["little-sidewalk"]["top-right"][0], ),



            ]

        for k in range(21):
            self.grounds.append(
                self.constructor.createGrass(position=(9.5-k, -7.44, 0.51), scale=(1, 1.1),
                                             texture=img.images["ground"]["sidewalk"]["bottom"][0], )
            )