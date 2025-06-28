from ursina import Audio


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
        if held_keys['space'] and not self.audio_crawk.playing:
            self.audio_crawk.play()
