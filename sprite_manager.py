import pygame


class SpriteManager:
    def __init__(self, user):
        self.image = None
        self.rect  = None
        self.size  = None

        self.static = {
            'explore': {
                'idle': None,
                'walk_up': None,
                'walk_down': None,
                'walk_side': None,
                'dead': None,
            },
            'fight': {
                'idle': None,
                'running': None,
                'acting': None,

                'stuned': None,
                'hitted': None,
                'low': None,
                'dead': None,
            }
        }
