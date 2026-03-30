import pygame

from core.view.renderizator import Renderization
from core.combat.profile import CombatProfileData

#? we dont need to know that, so you need to convert save -> data -> CombatEngine
from core.unities.classes.characters  import Characters
from core.unities.entities.entities import Entities
from core.unities.classes.classes import alc, cvl, dpl
from core.unities.entities.enemy import dmy 



class CombatEngine:
    def __init__(self):
        self.level  = {
            'data': {
                'battleground_name': 'Training Ground',
                'battleground_path': None,
            },
            'entities': {
                0: Entities(dmy()),
                1: Entities(dmy()),
                2: Entities(dmy())
            }
        }
        self.player = {
            'team': {
                0: Characters(alc()),
                1: Characters(cvl()),
                2: Characters(dpl())
            }
        }
        self.events = None
        self.info   = {
            'cache': { 'is_active': False, },
            'match': { 'rounds_played': 0, 'is_game_over': False }
        }

        self.display = pygame.display.get_surface()
        self.action_controller       = None
        self.combatevents_controller = None
        self.renderization = Renderization()

    def __start_combat_profile(self):
        for nums, ent in enumerate(self.level['entities']):
            self.info['cache']['entities'][nums] = CombatProfileData(ent)
        for nums, char in enumerate(self.player['team']):
            self.info['cache']['characters'][nums] = CombatEngine(char)
        self.info['cache']['is_active'] = True
    
    def __clear_combat_profile(self):
        self.info['cache'] = { 'is_active': False, }

    def apply_combat_profile(self):
        pass    

    def update(self):
        pass