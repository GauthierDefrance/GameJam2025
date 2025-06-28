class Son :
    def __init__(self,nom,sound,ids):
        self.nom = nom
        self.sound = sound
        self.ids = ids

    def play(self):
        self.sound.play()
        #code a ajouter pour check des event box
