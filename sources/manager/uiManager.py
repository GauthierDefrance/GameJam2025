from ursina import *
from sources.constructor.soundClass import *

class UserInterface :
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


    def __init__(self):
        if UserInterface._initialized:
            return
        self.menu_buttons = []
        UserInterface._initialized = True

    def afficher(self,txt):
        texte = Text(
            text=txt,
            origin=(0, 0),  # point d’ancrage (centre ici)
            scale=2,  # taille du texte
            color=color.white,  # couleur du texte
            position=(-0.5, 0.4)  # position dans la fenêtre
        )

    def afficher_menu(self, options, callback):
        # Nettoyer anciens boutons
        for b in self.menu_buttons:
            destroy(b)
        self.menu_buttons.clear()

        # Créer un bouton par option
        for i, option in enumerate(options):
            button = Button(
                text=option,
                scale=(0.4, 0.1),
                position=(0, 0.4 - i * 0.15),
                color=color.azure,
                on_click=lambda o=option: self.choix_fait(o, callback, options)
            )
            self.menu_buttons.append(button)

    # Quand une option est choisie, on détruit les boutons et on appelle le callback
    def choix_fait(self,option, callback, options):
        for b in self.menu_buttons:
            destroy(b)
        self.menu_buttons.clear()
        for i in range(len(options)):
            if options(i)==o :
                callback(i)
        callback(0)


def afficher_panneau(message):
    # Créer un fond pour le panneau (semi-transparent)
    fond = Entity(
        parent=camera.ui,
        model='quad',
        scale=(1.2, 0.6),
        color=color.rgba(0, 0, 0, 180),
        position=(0, 0),
        collider = 'box'
    )

    # Créer le texte par-dessus
    texte = Text(
        text=message,
        parent=fond,
        origin=(0, 0),
        scale=2,
        position=(0, 0),
        color=color.white
    )

    # Quand on clique sur le fond, on supprime le fond et le texte
    def supprimer_panneau():
        destroy(fond)

    fond.on_click = supprimer_panneau

def afficher_message_temporaire(texte, duree=1, fondu=1):
    """
    Affiche un message à l'écran, qui disparaît automatiquement en fondu.
    :param texte: Le texte à afficher.
    :param duree: Temps avant le début du fondu (en secondes).
    :param fondu: Durée du fondu (en secondes).
    """
    message = Text(
        text=texte,
        origin=(0, 0),
        scale=2,
        position=(0, 0.3),
        background=True
    )

    # On attend `duree` secondes, puis on lance le fondu, puis on détruit
    Sequence(
        Wait(duree),
        Func(message.fade_out, duration=fondu),
        Wait(fondu),
        Func(destroy, message)
    ).start()