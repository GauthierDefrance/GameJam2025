from ursina import Audio

from sources.manager.Cutscene import Cutscene
from sources.manager.MenuManager import MenuManager
from sources.manager.uiManager import *


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

        self.event_guard_inside = False
        self.event_guard_RunAway = False



        self.audio_crawk = Audio('musics/sounds/squawk.ogg', autoplay=False)
        self.audio_baby_loop = Audio('musics/sounds/baby.ogg',loop = True, autoplay=False)
        self.audio_baby = Audio('musics/sounds/baby.ogg', autoplay=False)
        self.audio_lion = Audio('musics/sounds/lion.ogg', autoplay=False)

        self.audio_dict = {
            "baby_cry_loop" : self.audio_baby_loop,
            "baby_cry" : self.audio_baby,
            "lion_grr" : self.audio_lion,
        }

        print(self.audio_crawk)
        EventManager._initialized = True

    def check(self, player, held_keys, gameMap):
        from sources.constructor.MapConstructor import MapConstructor
        game_started=False
        volume = clamp(1  - (1*game_started) - ((player.position - (-3,-6)).length() / 6), 0, 1)
        self.audio_baby_loop.volume = volume

        if held_keys['escape']:
            self.audio_crawk.stop()
            #Arréter toutes musiques
            MenuManager().showMainMenu()

        if held_keys['space'] and not self.audio_crawk.playing:
            self.audio_crawk.play()
            zone = gameMap.event_zones["lion"]
            if intersects_2d_xy(player, zone):
                if hasattr(zone, 'sound') and zone.sound:
                    if zone.sound in self.audio_dict:
                        audio = self.audio_dict[zone.sound]
                        if not audio.playing:
                            Sequence(
                                Wait(1),
                                Func(audio.play)
                            ).start()


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
                            if zone.soundp in self.audio_dict:
                                audio = self.audio_dict[zone.soundp]
                                if audio.playing:
                                    print("Copied sound:", zone.sound)
                                    player.current_sound = zone.sound
                                    afficher_message_temporaire("Son copié !")

                        break  # On sort après la première zone détectée
        else:
            self.c_key_locked = False

        if held_keys['t']:
            if not self.t_key_locked:
                self.t_key_locked = True
                txt_tuto = "Commandes :\n\n\nflèches directionnelles : déplacements \n\nespace : jacasser\n\nc : copier un son\n\ne : répéter le dernier son copié\n\n\n (cliquez pour fermer)"
                afficher_panneau(txt_tuto)
        else:
            self.t_key_locked = False

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
    cutscene = Cutscene(MapConstructor())


    if player.current_sound=="baby_cry" and not EventManager().event_guard_inside:
        mc = MapConstructor()
        mc.doors['real_east_door'].visible = True
        cutscene.guard_enter()
        EventManager().event_guard_inside = True

    elif player.current_sound=="lion_grr" and not EventManager().event_guard_RunAway and EventManager().event_guard_inside :
        cutscene.guard_escape()
        EventManager().event_guard_RunAway = True
        mc = MapConstructor()
        mc.doors['east_door'].is_open = True
        mc.doors['real_east_door'].is_open = True

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