from ursina import *

from sources.constructor.MapConstructor import MapConstructor
from sources.manager.EventManager import EventManager
from sources.manager.MenuManager import MenuManager
from sources.manager.MoveManager import MoveManager


class UpdateManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.current_menu = "Home"
        self.not_launched = True

    def tick(self):
        if MenuManager().game_started:
            if self.not_launched :
                EventManager().audio_baby_loop.play()
                self.not_launched = False
            self.update_game()
        else:
            self.update_menu()

    def update_game(self):
        MoveManager().movePlayer(MapConstructor().player, held_keys, MapConstructor().walls, MapConstructor().moving_objects)
        MoveManager().moveEntity(MapConstructor().player, held_keys, MapConstructor().walls, MapConstructor().moving_objects)
        EventManager().check(MapConstructor().player, held_keys, MapConstructor())
        camera.position = (MapConstructor().player.x, MapConstructor().player.y, camera.z)

    def update_menu(self):
        # Ici tu peux gérer les interactions du menu si besoin
        pass
