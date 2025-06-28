class Son :
    def __init__(self,nom,sound,ids):
        self.nom = nom
        self.sound = sound
        self.ids = ids

    def splay(self):
        self.sound.play()
        #code a ajouter pour check des event box

jacass = None

class parrot :
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


    def __init__(self):
        self.soundL = [jacass]
        self.last = jacass

    def play_last(self):
        self.last.splay()

    def play_what(self):
        
