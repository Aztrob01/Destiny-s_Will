import pygame, random


from root.settings       import *
from entities.classes    import * #! removable
from entities.enemy      import * #! removable
from entities.characters import Characters
from entities.entities   import Entities
from core.combat         import Combat

# Control any combat screen


class World:
    def __init__(self):
        pass


class LevelCreator:
    def __init__(self):
        self.display = pygame.display.get_surface()
        
        self.WORLD   = World()
        self.COMBAT  = Combat('./assets/image/battlegrounds/sideviewerII.png')
        
        self.WORLD_STAGE = None

    def play(self):
        if self.COMBAT.PLAYER_TEAM == []:
            for x in range(0, 3):
                target = random.choice(LIST)
                self.COMBAT.PLAYER_TEAM.append(Characters(LIST[x]()))
                self.COMBAT.PLAYER_TEAM[x].index = x
        if self.COMBAT.ENEMY_TEAM == []:
            for x in range(0, 3):
                self.COMBAT.ENEMY_TEAM.append(Entities(Goblin()))
                self.COMBAT.ENEMY_TEAM[x].index = x
        self.COMBAT.start()
