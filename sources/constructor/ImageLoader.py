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
                    "grawl": self.load_texture_frames("characters/lion/grawl", 0),
                    "sit": self.load_texture_frames("characters/lion/sit", 0),
                },
            },
            "ground": {},
            "wall": {
                "brick" : self.load_texture_frames("textures/wall/brick", 1),
            },
            "props": {},
            "doors": {
                "first" : {
                    "open" : self.load_texture_frames("textures/doors/open", 1),
                    "closed" : self.load_texture_frames("textures/doors/closed", 1),
                }
            }
        }