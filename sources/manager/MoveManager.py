from ursina import *
from sources.constructor.ImageLoader import ImageLoader


class MoveManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.img = ImageLoader()
        self.last_update = time.time()
        self.frame_duration = 0.3

    def movePlayer(self, player, held_keys, walls, moving_objects):
        move = Vec2(0, 0)
        speed = player.speed * time.dt
        direction = None
        collide = False

        if held_keys['a']:
            move.x -= speed
            player.direction = "left"
            direction = "left"

        elif held_keys['d']:
            move.x += speed
            player.direction = "right"
            direction = "right"

        elif held_keys['s']:
            move.y -= speed
            player.direction = "bottom"
            direction = "bottom"

        elif held_keys['w']:
            move.y += speed
            player.direction = "top"
            direction = "top"

        # Mouvement avec collisions
        player.x += move.x
        for wall in walls:
            if player.intersects(wall).hit:
                player.x -= move.x
                collide=True

        player.y += move.y
        for wall in walls:
            if player.intersects(wall).hit:
                player.y -= move.y
                collide=True

        # Animation si on bouge
        if direction and not collide:
            player.direction = direction
            self.update_animation(player)

    def update_animation(self, player):
        now = time.time()
        if now - self.last_update > self.frame_duration:
            self.last_update = now
            direction = player.direction
            player.current_animation = (player.current_animation + 1) % len(self.img.images['player'][direction])
            player.texture = self.img.images['player'][direction][player.current_animation]

    def moveEntity(self, player, held_keys, walls, moving_objects):
        # Mouvement et collisions ennemis
        for obj in moving_objects:
            obj.y += obj.speed * obj.direction * time.dt
            if obj.y < -3 or obj.y > 3:
                obj.direction *= -1

            if player.intersects(obj).hit:
                push = (player.position - obj.position).normalized() * time.dt * 5
                player.position += push