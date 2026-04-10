import pygame, random

from core.combat_engine import CombatEngine
from core.builder_level import LevelBuilder
from core.builder_player import PlayerBuilder

class FlowManager:
    def __init__(self, player, level):
        self.__display = pygame.display.get_surface()
        self.__player  = PlayerBuilder(player)
        self.__level   = LevelBuilder(level)
        
        self.__explore = None 
        self.__combat  = None
        self.__state   = [0, 'fight']
        
        self.events  = None

    def load(self):
        if self.__state[1] == 'explore':
            self.__explore = None
            print('Loading exploration...')
        elif self.__state[1] == 'fight':
            battleground = self.__level.generate_battleground()
            mobs         = self.__level.generate_enemies()
            team         = self.__player.generate_team()
            self.__combat = CombatEngine()

            self.__combat.level['data']['image'] = battleground

            for nums, members in enumerate(self.__combat.player['team']):
                self.__combat.player['team'][nums] = team[nums]
            for nums, entities in enumerate(self.__combat.level['entities']):
                self.__combat.level['entities'][nums] = entities

    def play(self):
        if self.__state[0] == 0:
            self.load()
            self.__state[0] = 1
        self.__combat.play()
