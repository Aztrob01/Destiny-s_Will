import random, pygame
from core.passive_list import passive_list
from core.skill_engines import SkillEngine
from core.skill_list import skill_list
from root.settings import *
from root.utilities import image_load



class Goblin:
    def __init__(self):
        self.main_class = 'Monster'
        self.codename   = 'Goblin'

        self.size = SPRITE_S_S
        self.inner_galery = {
            'exploring': image_load('./assets/image/enemies/goblins/idle.png'),
            'fighting': {
                'idle': image_load('./assets/image/enemies/goblins/idle.png'),
                'hitted': image_load('./assets/image/enemies/goblins/idle.png'),
                'selected': image_load('./assets/image/enemies/goblins/idle.png'),
                'acting': image_load('./assets/image/enemies/goblins/idle.png'),
            },
            'defeated': image_load('./assets/image/enemies/goblins/idle.png')
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
        
        self.basic_skills = [skill_list['Pierce'], skill_list['Encourage']]
        self.passive      = passive_list['Goblin']
        self.attack       = SkillEngine('Basic Attack', self.atk, self.mch)

    
    
    def mch(self, user):
        pass

    def atk(self, user, target):
        RES = target.COMBAT_PROFILE.RESISTANCE
        DMG = ((user.COMBAT_PROFILE.STRENGHT / 2) - RES)

        if DMG > 0:
            target.COMBAT_PROFILE.CURRENT_HP -= DMG
            return True