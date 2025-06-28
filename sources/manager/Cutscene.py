from ursina import *

from sources.manager.MenuManager import MenuManager


class Cutscene:
    _instance = None
    _initialized = False  # flag d'initialisation

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


    def __init__(self, map_constructor):
        if Cutscene._initialized:
            return  # ignore les appels suivants à __init__
        self.map = map_constructor

    def guard_enter(self):
        print("Guard enter cutscene")
        MenuManager().game_started = False
        # Position de départ : juste derrière la porte
        start_pos = (11, -2, 0.5)
        target_pos = (7, -2, 0.5)

        # Créer le garde
        self.guard = Entity(
            model='cube',
            scale=(1, 2),
            color=color.azure,
            position=start_pos,
            texture='white_cube',
            name="cutscene_guard"
        )

        # Animation d'entrée
        duration = 3
        self.guard.animate_position(target_pos, duration=duration, curve=curve.linear)

        # Optionnel : afficher un message quand le garde s'arrête
        def on_arrival():
            print("Le garde est arrivé.")
            # Ici, tu peux déclencher la suite de la cutscene
            print(self.guard)

        invoke(on_arrival, delay=duration)
        MenuManager().game_started = True

    def guard_escape(self):
        print("Guard escape cutscene")
        MenuManager().game_started = False

        # Position de départ : dans la pièce
        start_pos = (7, -2, 0.5)
        target_pos = (11, -2, 0.5)  # Vers l'extérieur

        # Créer ou réutiliser le garde
        self.guard.position = start_pos

        # Animation de fuite
        duration = 0.5
        self.guard.animate_position(target_pos, duration=duration, curve=curve.linear)

        def on_escape():
            print("Le garde s'est enfui.")
            destroy(self.guard)  # Optionnel : supprimer le garde après sa fuite
            self.guard = None  # Réinitialiser

        invoke(on_escape, delay=duration)
        MenuManager().game_started = True
