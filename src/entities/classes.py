import pygame
import random
from entities.passives import *
from combat.profile import *
from root.settings import *

# Creates start and playable Classes/jobs, determining their basic stats
# and sprites

class d01:
    def __init__(self):
        self.mc       = 'DUELIST'
        self.codename = 'Cavaliere'
        self.name     = 'Claire Lemoine'

        self.size = SPRITE_S_N
        self.inner_image_explore  = pygame.image.load('./assets/image/classes/cavaliere/idle.png')
        self.inner_image_idle     = pygame.image.load('./assets/image/classes/cavaliere/idle.png')
        self.inner_image_hitted   = pygame.image.load('./assets/image/classes/cavaliere/idle.png')
        self.inner_image_selected = pygame.image.load('./assets/image/classes/cavaliere/idle.png')
        self.inner_image_acting   = pygame.image.load('./assets/image/classes/cavaliere/idle.png')
        self.inner_image_defeated = pygame.image.load('./assets/image/classes/cavaliere/idle.png')
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

        self.basic_stats   = {
            'hp': 100,
            'str': 20, 
            'dex': 40,
            'knw': 10,
            'lky': 20,
            'res': 10,
        }
        self.basic_items   = {
            'armor': None,
            'weapon': None,
            'Trinket': None,
            'Boots': None,
        }
        self.basic_skills  = [None, None, None, None]
        self.attack        = SkillEngine(self.ba_mech, self.ba_set)
        self.passive       = PassiveEngine('Angarde', self.psv)

    def ba_mech(self, user, target):
        # ataque basico que se beneficia de Destreza para causar dano
        # chance de desvio baseado na destreza do alvo?
    
        critchance = user.COMBAT_PROFILE.CRITICAL_CH
        crit_threshold = random.uniform(0.01, 1)

        avoidchance = target.COMBAT_PROFILE.DEXTERITY / 100
        avoid_threshold = random.uniform(0.01, 1)

        if avoidchance > avoid_threshold:
            if crit_threshold <= critchance:
                damage = int((user.COMBAT_PROFILE.DEXTERITY / 2) * user.COMBAT_PROFILE.CRITICAL_DMG)
                print('Causou critico!')
            else:
                damage = int(user.COMBAT_PROFILE.DEXTERITY * user.COMBAT_PROFILE.DEXTERITY)

            target.COMBAT_PROFILE.CURRENT_HP -= damage
            return True
        
        else:
            print(f'{user.codename} errou o ataque contra {target.codename}')
        
    def ba_set(self, user):
        pass

    def psv(self, user):
        pass
            
        
class w01:
    def __init__(self):
        self.mc = 'WARRIOR'
        self.codename = 'Soldier'
        self.name     = 'Zander Khrustt'

        self.size = SPRITE_S_N
        self.inner_image_explore  = pygame.image.load('./assets/image/classes/dwarf/idle.png')
        self.inner_image_idle     = pygame.image.load('./assets/image/classes/dwarf/idle.png')
        self.inner_image_hitted   = pygame.image.load('./assets/image/classes/dwarf/idle.png')
        self.inner_image_selected = pygame.image.load('./assets/image/classes/dwarf/idle.png')
        self.inner_image_acting   = pygame.image.load('./assets/image/classes/dwarf/idle.png')
        self.inner_image_defeated = pygame.image.load('./assets/image/classes/dwarf/idle.png')
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
            'hp': 125,
            'str': 40, 
            'dex': 10,
            'knw': 0,
            'lky': 0,
            'res': 30,
        }
        self.basic_items   = {
            'armor': None,
            'weapon': None,
            'Trinket': None,
            'Boots': None,
        }
        self.basic_skills  = [None, None, None, None]
        
        self.attack  = SkillEngine(self.mech, self.set)
        self.passive = PassiveEngine('For the Twice', self.psv)

    def mech(self, user, target):
        DAMAGE = (user.COMBAT_PROFILE.STRENGHT * user.COMBAT_PROFILE.INPUT_DAMAGE_MULTIPLIER) - target.COMBAT_PROFILE.RESISTANCE

        target.COMBAT_PROFILE.CURRENT_HP -= DAMAGE

    def set(self, user):
        pass


    def psv(self, user):
        pass

class m01:
    def __init__(self):
        self.mc = 'MAGE'
        self.codename = 'Wizard'

        self.size = SPRITE_S_N
        self.inner_image_explore  = pygame.image.load('./assets/image/classes/wizard/idle.png')
        self.inner_image_idle     = pygame.image.load('./assets/image/classes/wizard/idle.png')
        self.inner_image_hitted   = pygame.image.load('./assets/image/classes/wizard/idle.png')
        self.inner_image_selected = pygame.image.load('./assets/image/classes/wizard/idle.png')
        self.inner_image_acting   = pygame.image.load('./assets/image/classes/wizard/idle.png')
        self.inner_image_defeated = pygame.image.load('./assets/image/classes/wizard/idle.png')
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

        self.basic_stats   = {
            'hp': 70,
            'str': 20, 
            'dex': 30,
            'knw': 30,
            'lky': 10,
            'res': 10,
        }
        self.basic_items   = {
            'armor': None,
            'weapon': None,
            'Trinket': None,
            'Boots': None,
        }
        self.basic_skills  = [None, None, None, None]
        self.attack        = SkillEngine(self.mech, self.set)
        self.passive       = PassiveEngine('Contracts', self.psv)

    def mech(self, user, target):
        damage = (user.COMBAT_PROFILE.STRENGHT * user.COMBAT_PROFILE.OUTPUT_DAMAGE_MULTIPLIER) - target.COMBAT_PROFILE.RESISTANCE
        if target in user.CONTEXT.ALLIES:
            target.COMBAT_PROFILE.CURRENT_HP += damage
            print(f'{user.codename} [{user.index}] curou {target.codename} [{target.index}]')
            for allies in user.CONTEXT.ALLIES:
                user.COMBAT_PROFILE.LISTOF_TARGETS.remove(allies)
        else:
            target.COMBAT_PROFILE.CURRENT_HP -= damage
        
        return True

        

    def set(self, user):
        for allies in user.CONTEXT.ALLIES:
            if allies not in user.COMBAT_ACTIONS.LISTOF_TARGETS:
                user.COMBAT_ACTIONS.LISTOF_TARGETS.insert(-1, allies)

    def psv(self, user):
        #TODO uma passiva pra armazenar aliados na lista de alvos de actions
        #TODO e curar eles com o ataque, caso eles sejam atacados
        pass

LIST = {
    0: d01,
    1: w01,
    2: m01,
}