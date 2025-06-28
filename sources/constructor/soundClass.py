from sources.manager.uiManager import *

class Son :
    def __init__(self,nom,sound,ids):
        self.nom = nom
        self.sound = sound
        self.ids = ids

    def splay(self):
        self.sound.play()
        #code a ajouter pour check des event box

jacass = None

class Parrot :
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


    def __init__(self):
        if Parrot._initialized:
            return

        self.soundL = [jacass]
        self.last = jacass
        Parrot._initialized = True

    def play_id(self,ids):
        self.soundL[ids].splay()

    def play_last(self):
        self.last.splay()

    def play_what(self):
        uim = UserInterface()
        uim.afficher_menu(self.soundL,self.play_id)

