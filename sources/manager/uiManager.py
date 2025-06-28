from ursina import *

def afficher(txt) :
    texte = Text(
        text=txt,
        origin=(0, 0),  # point d’ancrage (centre ici)
        scale=2,  # taille du texte
        color=color.white,  # couleur du texte
        position=(-0.5, 0.4)  # position dans la fenêtre
    )