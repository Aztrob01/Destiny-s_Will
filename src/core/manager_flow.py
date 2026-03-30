import pygame, random

from core.combat_engine import CombatEngine
from core.manager_save  import SaveManager
from core.manager_level import LevelBuilder

class PlayerTeamBuilder:
    def __init__(self, data_player):
        self.data_player = data_player

    def generate_team(self):
        from core.unities.classes.characters import Characters
        from core.unities.classes.classes    import alc, cvl, dpl

        pass
        

class FlowManager:
    def __init__(self, player, level):
        self.__display = pygame.display.get_surface()
        self.__player  = SaveManager()
        self.__level   = LevelBuilder(level)
        
        self.__explore = None 
        self.__combat  = CombatEngine()
        self.__state   = [0, 'fight']
        
        self.events  = None

    def load(self):
        pass

    def play(self):
        pass

    def tick(self):
        print(f'Active: {self.__state[0]} in {self.__state[1]} | events: {self.events}')