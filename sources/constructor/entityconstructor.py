from ursina import *

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
        player.speed = 4                  # vitesse de déplacement
        player.direction = "right"        # direction du regard
        player.current_animation = 0      # frame de l'animation
        player.score = 0                  # score ou autre variable de progression
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
