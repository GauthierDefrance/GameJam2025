from ursina import *
from sources.constructor.ImageLoader import ImageLoader


class MoveManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def movePlayer(self, player, held_keys, walls, moving_objects):
        move = Vec2(0, 0)
        speed = player.speed * time.dt

        if held_keys['a']:
            move.x -= speed
            player.texture = ImageLoader().images['player']['left'][0]
            player.direction = "left"

        if held_keys['d']:
            move.x += speed
            player.texture = ImageLoader().images['player']['right'][0]
            player.direction = "right"

        if held_keys['s']:
            move.y -= speed
            player.texture = ImageLoader().images['player']['bottom'][0]
            player.direction = "bottom"

        if held_keys['w']:
            move.y += speed
            player.texture = ImageLoader().images['player']['top'][0]
            player.direction = "top"

        # Mouvement avec collisions
        player.x += move.x
        for wall in walls:
            if player.intersects(wall).hit:
                player.x -= move.x

        player.y += move.y
        for wall in walls:
            if player.intersects(wall).hit:
                player.y -= move.y

    def moveEntity(self, player, held_keys, walls, moving_objects):
        # Mouvement et collisions ennemis
        for obj in moving_objects:
            obj.y += obj.speed * obj.direction * time.dt
            if obj.y < -3 or obj.y > 3:
                obj.direction *= -1

            if player.intersects(obj).hit:
                push = (player.position - obj.position).normalized() * time.dt * 5
                player.position += push