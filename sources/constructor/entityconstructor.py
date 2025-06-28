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
        player.current_sound = None
        return player

    def createWall(self, position=(0,0,0), scale=(1,1), texture=None,color_value=color.gray):
        wall = Entity(
            model='quad',
            color=color_value,
            scale=scale,
            position=position,
            collider='box',
            texture=texture,
            texture_scale = scale,
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

    def createEventZone(self, position=(0, 0, 0), scale=(1, 1), callback=lambda: None, name="zone", color_value=color.white, sound:str=None, soundp:str=None):
        zone = Entity(
            name=name,
            model='quad',
            position=position,
            scale=scale,
            collider='box',
            visible=True,
            color=color_value,
        )

        # Attributs supplémentaires
        zone.sound = sound #String indiquant le nom du son associé
        zone.soundp = soundp
        zone.callback = callback  # fonction à exécuter à l'entrée
        zone.triggered = False  # empêche plusieurs déclenchements

        return zone

    def createDoor(self, position=(0, 0), scale=(1, 2), color_=color.brown, is_open=False, name="door", texture = None):
        door = Entity(
            name=name,
            model='quad',
            position=position,
            scale=scale,
            color=color_,
            collider='box',
            texture=texture
        )
        door.is_open = is_open  # Ajout du flag d'état
        return door

    def createNPC(self, position=(0, 0), scale=(1, 2), color_=color.red, texture = None, name = "bob", callback=lambda: None, radius:int=0):
        npc = Entity(
            name=name,
            model='quad',
            position=position,
            scale=scale,
            collider='box',
            texture=texture
        )
        npc.callback = callback
        npc.contact_radius = radius
        return npc