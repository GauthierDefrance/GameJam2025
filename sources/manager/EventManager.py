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
        self.audio_baby = Audio('musics/sounds/baby.ogg', autoplay=False)
        self.audio_lion = Audio('musics/sounds/lion.ogg', autoplay=False)

        self.audio_dict = {
            "baby_cry" : self.audio_baby,
            "lion_grr" : self.audio_lion,
        }

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

        # Initialisation des verrous une seule fois
        if not hasattr(self, 'e_key_locked'):
            self.e_key_locked = False
        if not hasattr(self, 'c_key_locked'):
            self.c_key_locked = False

        # --- Touche E : jouer le son actuel du joueur, et exécuter un éventuel callback ---
        if held_keys['e']:
            if not self.e_key_locked:
                self.e_key_locked = True

                # Jouer le son actuel du joueur s'il existe
                if hasattr(player, 'current_sound') and player.current_sound:
                    if player.current_sound in self.audio_dict:
                        audio = self.audio_dict[player.current_sound]
                        if not audio.playing:
                            audio.play()

                # Vérifie si le joueur est dans une zone avec un callback
                for zone in gameMap.event_zones.values():
                    if intersects_2d_xy(player, zone):
                        if hasattr(zone, 'callback') and callable(zone.callback):
                            zone.callback()
                        break  # Une seule zone suffit
        else:
            self.e_key_locked = False

        # --- Touche C : uniquement si dans une zone avec un son ---
        if held_keys['c']:
            if not self.c_key_locked:
                self.c_key_locked = True

                for zone in gameMap.event_zones.values():
                    if intersects_2d_xy(player, zone):
                        if hasattr(zone, 'sound') and zone.sound:
                            if zone.sound in self.audio_dict:
                                audio = self.audio_dict[zone.sound]
                                if not audio.playing:
                                    audio.play()
                                player.current_sound = zone.sound
                                print("Copied sound:", zone.sound)
                        break  # On sort après la première zone détectée
        else:
            self.c_key_locked = False


def LionEvent():
    from sources.constructor.MapConstructor import MapConstructor
    player = MapConstructor().player

    print("Lion Event triggered!")

def KidEvent():
    from sources.constructor.MapConstructor import MapConstructor
    player = MapConstructor().player

    print("Kid Event triggered!")

def GuardEvent():
    from sources.constructor.MapConstructor import MapConstructor
    player = MapConstructor().player

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