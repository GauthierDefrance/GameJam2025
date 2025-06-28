from ursina import Audio
from sources.manager.MenuManager import MenuManager


class EventManager:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if EventManager._initialized:
            return
        self.audio_crawk = Audio('musics/sounds/squawk.ogg', autoplay=False)
        print(self.audio_crawk)
        EventManager._initialized = True

    def check(self, player, held_keys, gameMap):
        from sources.constructor.MapConstructor import MapConstructor
        if held_keys['escape']:
            self.audio_crawk.stop()
            #Arréter toutes musiques
            MenuManager().showMainMenu()

        if held_keys['space'] and not self.audio_crawk.playing:
            self.audio_crawk.play()
            #Vérifier si on est dans une zone d'interactions et faire le son associé

        if held_keys['e'] and not self.e_key_locked:
            self.e_key_locked = True
            for zone in gameMap.event_zones.values():
                if intersects_2d_xy(player, zone):
                    print(f"Player is in zone: {zone.name}")
                    if hasattr(zone, 'callback') and callable(zone.callback):
                        zone.callback()
                        break
        elif not held_keys['e']:
            self.e_key_locked = False

            # ----- C -----
        if held_keys['c'] and not self.c_key_locked:
            self.c_key_locked = True
            for zone in gameMap.event_zones.values():
                if intersects_2d_xy(player, zone):
                    print(f"Player is in zone: {zone.name}")
                    if hasattr(zone, 'callback') and callable(zone.callback):
                        zone.callback()
                        break
        elif not held_keys['c']:
            self.c_key_locked = False



def LionEvent():
    print("Lion Event triggered!")

def KidEvent():
    print("Kid Event triggered!")

def GuardEvent():
    print("Guard Event triggered!")

def intersects_2d_xy(entity_a, entity_b):
    # Calcule les bords pour chaque entité en X et Y
    a_min_x = entity_a.x - entity_a.scale_x / 2
    a_max_x = entity_a.x + entity_a.scale_x / 2
    a_min_y = entity_a.y - entity_a.scale_y / 2
    a_max_y = entity_a.y + entity_a.scale_y / 2

    b_min_x = entity_b.x - entity_b.scale_x / 2
    b_max_x = entity_b.x + entity_b.scale_x / 2
    b_min_y = entity_b.y - entity_b.scale_y / 2
    b_max_y = entity_b.y + entity_b.scale_y / 2

    # Vérifie si les rectangles se croisent
    return (
        a_min_x < b_max_x and a_max_x > b_min_x and
        a_min_y < b_max_y and a_max_y > b_min_y
    )