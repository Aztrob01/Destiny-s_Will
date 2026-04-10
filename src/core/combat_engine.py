import pygame

from core.view.renderizator import Renderization
from core.combat.profile import CombatProfileData



class CombatEngine:
    def __init__(self):
        self.data = {
            # basic
            'cenary': None,
            'entities': [],
            'team': [],
            # match
            'turn': 0,
            'active': 0,
            'turns': [],
            'over': False,
            # entity cache
            'temp': {
                'active': False,
                'entities': None,
                'chars': None,
            }
        }
        

        self.events  = None
        self.display = pygame.display.get_surface()
        self.action_controller       = None
        self.combatevents_controller = None
        self.renderization = Renderization()

    def __prepare(self):
        if self.data['temp']['active'] is False:
            for nums, unities in enumerate(self.data['entities']):
                self.data['temp']['entities'][nums] = CombatProfileData(unities)
            for nums, unities in enumerate(self.data['team']):
                self.data['temp']['chars'][nums] = CombatProfileData(unities)
            
            self.data['temp']['active'] = True

    def prev(self, target=None):
        pass

    def next(self, target=None):
        pass

    def apply_combat_profile(self):
        pass    

    def update(self):
        pass

    def play(self):
        for unities in self.player['team']:
            unity = self.player['team'][unities]
            self.renderization.draw_entity(unity, (300, 300))