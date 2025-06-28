from ursina import *
from sources.constructor.ImageLoader import ImageLoader
from sources.constructor.MapConstructor import MapConstructor
from sources.manager.MenuManager import MenuManager
from sources.manager.MoveManager import MoveManager
from sources.manager.EventManager import EventManager
from sources.manager.UpdateManager import UpdateManager

#Init de Ursina
app = Ursina()

#Init des menus
game_started = False
menu = MenuManager()
menu.showMainMenu()

#Init des images
img = ImageLoader()

#Init de la caméra
camera.orthographic = True
camera.fov = 10

#Create map
GameMap = MapConstructor()
GameMap.createMap()



#The managers
mover = MoveManager()
events = EventManager()
updater = UpdateManager()

def update():
    updater.tick()

app.run()
