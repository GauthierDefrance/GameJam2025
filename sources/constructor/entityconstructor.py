from ursina import *
from config import *
from sources.constructor.ImageLoader import ImageLoader


class EntityConstructor:
    def createPlayer(self):
        player = Entity(
            model='quad',
            scale=(1, 1),
            position=(0, 0, 0),
            collider='box',
            texture= ImageLoader().images['player']['top'][0],
        )

        # Attributs utiles en top-down 2D
        player.speed = PLAYER_SPEED
        player.direction = DEFAULT_PLAYER_DIRECTION
        player.current_animation = 0
        player.score = 0
        return player

    def createWall(self, position=(0,0,0), scale=(1,1), color_value=color.gray, texture=None):
        wall = Entity(
            model='quad',
            color=color_value,
            scale=scale,
            position=position,
            collider='box',
            texture=texture
        )

        # Optionnel : attributs supplémentaires
        wall.isSolid = True
        return wall

    def createEntity(self, position=(0,0,0), scale=(1,1), color_value=color.white, texture=None):
        entity = Entity(
            model='quad',
            color=color_value,
            scale=scale,
            position=position,
            collider='box',
            texture=texture
        )

        entity.speed = 2
        entity.direction = "down"
        entity.current_animation = 0
        entity.path = []
        return entity

    def createEventZone(self, position=(0, 0, 0), scale=(1, 1), callback=lambda: None, name="zone"):
        zone = Entity(
            name=name,
            model='quad',
            position=position,
            scale=scale,
            collider='box',
            visible=True
        )

        # Attributs supplémentaires
        zone.callback = callback  # fonction à exécuter à l'entrée
        zone.triggered = False  # empêche plusieurs déclenchements

        return zone