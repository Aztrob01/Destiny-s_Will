import pygame


class SpriteManager:
    def __init__(self, user, data):
        self.image = None
        self.rect  = None
        self.size  = None

        self.static = {
            'explore': {
                'idle': data['explore']['idle'],
                'walk_up': data['explore']['walk_up'],
                'walk_down': data['explore']['walk_down'],
                'walk_side': data['explore']['walk_side'],
                'dead': data['explore']['dead'],
            },
            'fight': {
                'idle': data['fight']['idle'],
                'running': data['fight']['running'],
                'acting': data['fight']['acting'],

                'stuned': data['fight']['stuned'],
                'hitted': data['fight']['hitted'],
                'low': data['fight']['low'],
                'dead': data['fight']['dead'],
            },
        }

    def image_update(self, ref):
        self.image = pygame.image.load(ref)
        self.image = pygame.transform.scale(self.image, (64, 64)) #! change this values later, this thing will go bad if ignored

    
    def static_update(self, key_state):
        for nums, keys in enumerate(self.static):
            if key_state[0] == self.static[nums]:
                for num, key in enumerate(self.static[nums]):
                    if key_state[1] == self.static[nums][num]:
                        self.image_updade(self.static[nums][num])
                    
