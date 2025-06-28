from ursina import *

class UiManager:
    _instance = None
    _initialized = False  # flag d'initialisation

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if UiManager._initialized:
            return
        print("UiManager initialized")
        UiManager._initialized = True
        self.addButons()

    def addButons(self):
        # Taille et marge
        box_width = 0.25
        box_height = 0.15
        margin = 0.02

        # Position verticale : en bas (y = -0.9 environ)
        y_pos = -2

        # 3 boîtes
        boxes = []
        for i in range(3):
            box = Entity(
                parent=camera.ui,  # UI space = écran 2D fixe
                model='quad',
                color=color.azure,
                scale=(box_width, box_height),
                x=-0.35 + i * (box_width + margin),
                y=y_pos,
                z=0
            )
            boxes.append(box)