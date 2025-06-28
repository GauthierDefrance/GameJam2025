from ursina import time, Vec2

from sources.constructor.ImageLoader import ImageLoader
from sources.constructor.MapConstructor import MapConstructor
from sources.manager.EventManager import intersects_2d_xy


class MoveManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, 'initialized'):
            return  # évite d'écraser les valeurs existantes
        self.img = ImageLoader()
        self.frame_timer = 0.0
        self.frame_duration = 0.15
        self.last_direction = None
        self.initialized = True  # empêche réinit

    def movePlayer(self, player, held_keys, walls, moving_objects):
        # 1) calcul du vecteur de déplacement
        move = Vec2(0,0)
        speed = player.speed * time.dt
        direction = None

        if held_keys['left arrow']:
            move.x, direction = -speed, "left"
        if held_keys['right arrow']:
            move.x, direction =  speed, "right"
        if held_keys['down arrow']:
            move.y, direction = -speed, "bottom"
        if held_keys['up arrow']:
            move.y, direction =  speed, "top"

        # 2) mise à jour de la direction et reset de l’anim si besoin
        if direction:
            if direction != self.last_direction:
                # on tourne → reset frame et timer
                player.current_animation = 0
                self.frame_timer         = 0.0
                player.direction         = direction
            self.last_direction = direction

        closed_doors = [door for door in MapConstructor().doors.values() if not getattr(door, 'is_open', False)]

        colliders = walls + closed_doors

        collided = False
        player.x += move.x
        for wall in colliders:
            if intersects_2d_xy(player,wall):
                player.x    -= move.x
                collided      = True
                break

        player.y += move.y
        for wall in colliders:
            if intersects_2d_xy(player,wall):
                player.y    -= move.y
                collided      = True
                break

        if direction:
            if collided:
                # bloqué → on reste sur la frame statique dans la bonne direction
                player.current_animation = 0
                player.texture = self.img.images['player'][player.direction][1]
            else:
                # déplacement libre → animation
                self.update_animation(player)

    def update_animation(self, player):
        self.frame_timer += time.dt
        if self.frame_timer > self.frame_duration:
            self.frame_timer = 0
            direction = player.direction
            frames = self.img.images['player'][direction]
            player.current_animation = (player.current_animation + 1) % len(frames)
            player.texture = frames[player.current_animation]


    def moveEntity(self, player, held_keys, walls, moving_objects):
        # (reste inchangé)
        for obj in moving_objects:
            obj.y += obj.speed * obj.direction * time.dt
            if obj.y < -3 or obj.y > 3:
                obj.direction *= -1
            if player.intersects(obj).hit:
                push = (player.position - obj.position).normalized() * time.dt * 5
                player.position += push
