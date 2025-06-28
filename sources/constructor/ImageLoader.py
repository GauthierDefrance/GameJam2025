from ursina import load_texture

from config import ASSETS_DIR


class ImageLoader:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def load_texture_frames(self, base_path: str, count: int) -> list:
        """
        base_path doit être du style "characters/parrots/right"
        et count le nombre d'images (ici 4 pour right0.png → right2.png).
        """
        frames = []
        for i in range(count):
            rel_path = f"{base_path}{i}.png"   # ex: "characters/parrots/right0.png"
            tex = load_texture(rel_path)
            if(tex==None):
                print(f"Error when trying to load : {rel_path}")
            else:
                frames.append(tex)
        return frames


    def __init__(self):
        if hasattr(self, 'initialized'):
            return
        self.images = {
            'player': {
                "right": self.load_texture_frames("characters/parrots/Pdroite", 3),
                "left": self.load_texture_frames("characters/parrots/Pgauche", 3),
                "top": self.load_texture_frames("characters/parrots/Pdos", 3),
                "bottom": self.load_texture_frames("characters/parrots/Pface", 3),
            },
            "pnj": {
                "lion": {
                    "grawl": self.load_texture_frames("characters/lion/grawl", 1),
                    "sit": self.load_texture_frames("characters/lion/stand", 1),
                },
                "gardien" : {
                    "left" : self.load_texture_frames("characters/gardien/Gardiengauche", 3),
                },
                "poussette" : {
                    "still" : self.load_texture_frames("characters/poussette/still", 1),
                }


            },
            "ground": {
                "sidewalk" : {
                    "bottom" : self.load_texture_frames("textures/road/little_sidewalk_bottom", 1),
                    "right" : self.load_texture_frames("textures/road/little_sidewalk_right", 1),
                    "bottom-right": self.load_texture_frames("textures/road/little_sidewalk_bottom_right_corner", 1),
                    "door": self.load_texture_frames("textures/road/sidewalk_birdcage_door", 1),
                },
                "little-sidewalk": {
                    "bottom": self.load_texture_frames("textures/road/sidewalk_bottom", 1),
                    "right": self.load_texture_frames("textures/road/sidewalk_right", 1),
                    "left": self.load_texture_frames("textures/road/sidewalk_left", 1),
                    "bottom-right": self.load_texture_frames("textures/road/sidewalk_bottom_right_corner", 1),
                    "bottom-left": self.load_texture_frames("textures/road/sidewalk_bottom_left_corner", 1),
                    "top-right": self.load_texture_frames("textures/road/sidewalk_top_right_corner", 1),
                },
                "road": {
                    "basic" : self.load_texture_frames("textures/road/road", 1),
                    "sidewalk" : self.load_texture_frames("textures/road/sidewalk", 1),
                },
            },
            "wall": {
                "brick" : self.load_texture_frames("textures/wall/brick", 1),
                "birdcage_wall_bottom" : self.load_texture_frames("textures/wall/birdcage_wall_bottom", 1),
                "birdcage_wall_bottom_left_corner" : self.load_texture_frames("textures/wall/birdcage_wall_bottom_left_corner", 1),
                "birdcage_wall_bottom_right_corner" : self.load_texture_frames("textures/wall/birdcage_wall_bottom_right_corner", 1),
                "birdcage_wall_top" : self.load_texture_frames("textures/wall/birdcage_wall_top", 1),
                "birdcage_wall_side" : self.load_texture_frames("textures/wall/birdcage_wall_side", 1),
                "birdcage_wall_top_left_corner" : self.load_texture_frames("textures/wall/birdcage_wall_top_left_corner", 1),
                "birdcage_wall_top_right_corner" : self.load_texture_frames("textures/wall/birdcage_wall_top_right_corner", 1),
                "lion_cage_bars" : self.load_texture_frames("textures/wall/lion_cage_bars", 1),
                "lion_cage_wall_bottom" : self.load_texture_frames("textures/wall/lion_cage_wall_bottom", 1),
                "lion_cage_wall_bottom_right_corner" : self.load_texture_frames("textures/wall/lion_cage_wall_bottom_right_corner", 1),
                "lion_cage_wall_side" : self.load_texture_frames("textures/wall/lion_cage_wall_side", 1),


            },
            "props": {
                "avocatier" : self.load_texture_frames("avocatier", 1),
            },
            "doors": {
                "first" : {
                    "open" : self.load_texture_frames("textures/doors/open", 1),
                    "closed" : self.load_texture_frames("textures/doors/closed", 1),
                    "door" : self.load_texture_frames("textures/doors/actual_door", 1),
                }
            }
        }