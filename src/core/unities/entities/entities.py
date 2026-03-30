import pygame, random

from core.combat.profile import CombatProfileData

class Entities:
    def __init__(self, entity):
        self.origin     = entity
        self.codename   = entity.codename
        self.on_screen  = entity.size
        self.image = None
        self.rect  = None

        self.randomized = False
        self.mid        = 0
        self.mlvl       = 1
        self.buffer     = None
        self.main_state     = 'fighting'
        self.fighting_state = 'idle'
   

    def update(self):
        pass
        
        