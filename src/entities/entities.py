import pygame, random

from combat.combat_buffer import CombatBuffer
from root.utilities import update_sprt

class Entities:
    def __init__(self, entity):
        self.origin     = entity
        self.codename   = entity.codename
        self.on_screen  = entity.size
        self.randomized = False
        self.mid        = 0
        self.mlvl       = 1
        self.buffer     = CombatBuffer()
        self.main_state     = 'fighting'
        self.fighting_state = 'idle'
   

    def update(self):
        update_sprt(self)
        
        