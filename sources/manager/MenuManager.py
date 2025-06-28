from ursina import *

class MenuManager:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if MenuManager._initialized:
            return
        # création UI ici
        self.menu = "Home"
        self.title_text = Text('Parrot Escape !', origin=(0, 0), scale=2, position=Vec2(0, 0.3))
        self.start_button = Button(text='Démarrer', color=color.azure, scale=(0.3, 0.1), position=Vec2(0, 0))
        self.start_button.on_click = self.showGame
        self.quit_button = Button(text='Quitter', color=color.red, scale=(0.3, 0.1), position=Vec2(0, -0.2))
        self.quit_button.on_click = application.quit

        self.game_started = False
        MenuManager._initialized = True

    def showMainMenu(self):
        self.menu = "Home"
        self._set_ui_enabled(True)
        self.game_started = False
        print("Home menu !")

    def showGame(self):
        self.menu = "Game"
        self._set_ui_enabled(False)
        self.game_started = True
        print("Game menu !")

    def _set_ui_enabled(self, enabled: bool):
        self.start_button.enabled = enabled
        self.quit_button.enabled = enabled
        self.title_text.enabled = enabled
