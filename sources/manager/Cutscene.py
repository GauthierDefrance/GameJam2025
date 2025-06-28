from ursina import *
from sources.constructor.ImageLoader import ImageLoader
from sources.manager.MenuManager import MenuManager


class Cutscene:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, map_constructor):
        if Cutscene._initialized:
            return
        self.map = map_constructor
        self.guard = None
        self.guard_animating = False  # ✅ Flag d’animation
        Cutscene._initialized = True

    def animate_guard(self):
        self.guard_animating = True

        def update_frame():
            if not self.guard or not self.guard_animating:
                return
            self.guard.current_animation = (self.guard.current_animation + 1) % len(self.guard.frames)
            self.guard.texture = self.guard.frames[self.guard.current_animation]
            invoke(update_frame, delay=0.25)

        update_frame()

    def stop_guard_animation(self, static_frame_index=1):
        self.guard_animating = False
        if self.guard and hasattr(self.guard, "frames"):
            self.guard.texture = self.guard.frames[static_frame_index]

    def guard_enter(self):
        print("Guard enter cutscene")
        MenuManager().game_started = False

        start_pos = (11, -2, 0)
        target_pos = (7, -2, 0)
        duration = 3

        img = ImageLoader()
        self.guard = Entity(
            model='quad',
            scale=(1, 2),
            position=start_pos,
            texture=img.images["pnj"]["gardien"]["left"][0],
            name="cutscene_guard"
        )
        self.guard.frames = img.images["pnj"]["gardien"]["left"]
        self.guard.current_animation = 0

        self.animate_guard()
        self.guard.animate_position(target_pos, duration=duration, curve=curve.linear)

        def on_arrival():
            print("Le garde est arrivé.")
            self.stop_guard_animation()

        invoke(on_arrival, delay=duration)
        MenuManager().game_started = True

    def guard_escape(self):
        print("Guard escape cutscene")
        MenuManager().game_started = False

        start_pos = (7, -2, 0)
        target_pos = (40, -2, 0)
        duration = 2

        if not self.guard:
            return

        self.guard.position = start_pos
        self.animate_guard()
        self.guard.animate_position(target_pos, duration=duration, curve=curve.linear)

        def on_escape():
            print("Le garde s'est enfui.")
            self.stop_guard_animation()
            destroy(self.guard)
            self.guard = None

        invoke(on_escape, delay=duration)
        MenuManager().game_started = True
