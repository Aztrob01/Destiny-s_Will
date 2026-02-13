import random, pygame
from entities.passives import PassiveEngine, SkillEngine
from root.settings import *

class Goblin:
    def __init__(self):
        self.mc       = 'Monster'
        self.codename = 'Goblin'

        self.size = SPRITE_S_S
        self.inner_image_explore  = pygame.image.load('./assets/image/enemies/goblins/idle.png')
        self.inner_image_idle     = pygame.image.load('./assets/image/enemies/goblins/idle.png')
        self.inner_image_hitted   = pygame.image.load('./assets/image/enemies/goblins/idle.png')
        self.inner_image_selected = pygame.image.load('./assets/image/enemies/goblins/idle.png')
        self.inner_image_acting   = pygame.image.load('./assets/image/enemies/goblins/idle.png')
        self.inner_image_defeated = pygame.image.load('./assets/image/enemies/goblins/idle.png')
        self.inner_galery         = {
            'exploring':  self.inner_image_explore,
            'fighting': {
                'idle': self.inner_image_idle,
                'hitted':  self.inner_image_hitted,
                'selected': self.inner_image_selected,
                'acting':   self.inner_image_acting,
            },
            'defeated':  self.inner_image_defeated,
        }
        
        
        self.basic_stats  = {
            'hp': 100,
            'str': 20,
            'dex': 30,
            'knw': 10,
            'lky': 0,
            'res': 0,
        }
        self.randomizable = [['str', (20, 40)], ['knw', (10, 20)]]
        self.basic_skills  = [None, None, None, None]
        self.attack       = SkillEngine("Ataque Básico", self.mech, self.set)
        self.passive      = PassiveEngine('Minor Attack', self.psv)

    def set(self, user):
        pass

    def mech(self, user, target):
        RESISTANCE  = target.COMBAT_PROFILE.RESISTANCE
        AVOIDCHANCE = RESISTANCE / 100
        AVOIDLIMIT  = random.uniform(0.01, 1)
        DAMAGE      = ((user.COMBAT_PROFILE.STRENGHT / 2) - RESISTANCE)
        if  AVOIDLIMIT <= AVOIDCHANCE:
            target.COMBAT_PROFILE.CURRENT_HP -= DAMAGE
            print(f'O ataque Básico de {user.codename}[{user.index}] atingiu {target.codename} [{target.index}]')  
            return True
        else:
            print(f'O Ataque Básico de {user.codename}[{user.index}] errou o alvo!')
        

    def psv(self, user):
        if user.CONTEXT.GET_HITTED_NOW:
            user.origin.mech(user, user.CONTEXT.GET_HITTED_BY)



        