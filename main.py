from ursina import *

from config import ASSETS_DIR
from sources.constructor.ImageLoader import ImageLoader
from sources.constructor.entityconstructor import EntityConstructor
from sources.manager.MoveManager import MoveManager

app = Ursina()
img = ImageLoader()



camera.orthographic = True
camera.fov = 20

constructor = EntityConstructor()
player = constructor.createPlayer()

# Objets mobiles ennemis
moving_objects = []
for i in range(5):
    enemy = constructor.createEntity(
        position=(i * 2 - 4, 3),
        scale=(1, 1),
        color_value=color.red
    )
    enemy.speed = 2 + i * 0.5
    enemy.direction = -1
    moving_objects.append(enemy)

# Murs
walls = [
    constructor.createWall(position=(0, -5.5), scale=(20, 1)),   # bas
    constructor.createWall(position=(0, 5.5), scale=(20, 1)),    # haut
    constructor.createWall(position=(-9.5, 0), scale=(1, 12)),   # gauche
    constructor.createWall(position=(9.5, 0), scale=(1, 12)),    # droite
]

mvm = MoveManager()

def update():
    mvm.movePlayer(player, held_keys, walls, moving_objects)
    mvm.moveEntity(player, held_keys, walls, moving_objects)


app.run()
