import random, pygame

# -------------------------------------------
# D

class dmy:
    def __init__(self):
        self.main_class = 'Dummy'
        self.codename   = 'Dummy'

        self.size = (128, 128)
        self.inner_galery = {
            'exploring': ('./assets/image/entities/dmy/idle.png'),
            'fighting': {
                'idle': ('./assets/image/entities/dmy/idle.png'),
                'hitted': ('./assets/image/entities/dmy/idle.png'),
                'selected': ('./assets/image/entities/dmy/idle.png'),
                'acting': ('./assets/image/entities/dmy/idle.png'),
            },
            'defeated': ('./assets/image/entities/dmy/idle.png')
        }
        self.brain = {
            'agr': 0, # aggressivenes
            'dex': 0, # dexterity as teamplay
            'def': 0, # defense as protection
        }
        self.basic_stats  = {
            'hp': 100,
            'str': 0,
            'dex': 0,
            'knw': 0,
            'lky': 0,
            'res': 0,
        }
        
        self.basic_skills = None
        self.passive      = None
        self.attack       = None #! skill engine do ataque basico do dummy

# -------------------------------------------
# G

class gob:
    def __init__(self):
        self.main_class = 'Monster'
        self.codename   = 'Goblin'

        self.size = (128, 128)
        self.inner_galery = {
            'exploring': ('./assets/image/entities/gob/idle.png'),
            'fighting': {
                'idle': ('./assets/image/entities/gob/idle.png'),
                'hitted': ('./assets/image/entities/gob/idle.png'),
                'selected': ('./assets/image/entities/gob/idle.png'),
                'acting': ('./assets/image/entities/gob/idle.png'),
            },
            'defeated': ('./assets/image/entities/gob/idle.png')
        }
        self.brain = {
            'agr': 5, # aggressivenes
            'dex': 8, # dexterity as teamplay
            'def': 3, # defense as protection
        }
        self.basic_stats  = {
            'hp': 100,
            'str': 20,
            'dex': 30,
            'knw': 10,
            'lky': 0,
            'res': 0,
        }
        
        self.basic_skills = None
        self.passive      = None 
        self.attack       = None #! skill engine do ataque basico do goblin