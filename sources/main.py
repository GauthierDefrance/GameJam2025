from ursina import *

app = Ursina()

camera.orthographic = True
camera.fov = 20

# Joueur
player = Entity(
    model='quad',
    color=color.azure,
    scale=(1, 1),
    position=(0, 0),
    collider='box',
)

# Objets mobiles
moving_objects = []
for i in range(5):
    obj = Entity(
        model='quad',
        color=color.red,
        scale=(1, 1),
        position=(i * 2 - 4, 3),
        collider='box'
    )
    obj.speed = 2 + i * 0.5
    obj.direction = -1
    moving_objects.append(obj)

# Murs de la carte (visibles ou non)
walls = [
    Entity(model='quad', color=color.white66, scale=(20, 1), position=(0, -5.5), collider='box'),  # bas
    Entity(model='quad', color=color.white66, scale=(20, 1), position=(0, 5.5), collider='box'),   # haut
    Entity(model='quad', color=color.white66, scale=(1, 12), position=(-9.5, 0), collider='box'),  # gauche
    Entity(model='quad', color=color.white66, scale=(1, 12), position=(9.5, 0), collider='box'),   # droite
]

def update():
    # Déplacement du joueur
    move = Vec2(0, 0)
    speed = 4 * time.dt

    if held_keys['a']:
        move.x -= speed
    if held_keys['d']:
        move.x += speed
    if held_keys['s']:
        move.y -= speed
    if held_keys['w']:
        move.y += speed

    # Tentative de mouvement
    player.x += move.x
    for wall in walls:
        if player.intersects(wall).hit:
            player.x -= move.x  # annule si collision

    player.y += move.y
    for wall in walls:
        if player.intersects(wall).hit:
            player.y -= move.y  # annule si collision

    # Mouvement des objets ennemis
    for obj in moving_objects:
        obj.y += obj.speed * obj.direction * time.dt
        if obj.y < -3 or obj.y > 3:
            obj.direction *= -1

        # Collision ennemis → pousse joueur
        if player.intersects(obj).hit:
            push = (player.position - obj.position).normalized() * time.dt * 5
            player.position += push

app.run()
