import pygame

from root.utilities import update_sprt

from combat.actions import ActionSystem
from combat.context import ContextMenu
from combat.profile import CombatProfile

# Create the real entity thats read in game

class Characters:
    def __init__(self, member):
        self.origin    = member
        self.codename  = member.codename
        self.on_screen = member.size 
        self.chid      = 0
        
        self.main_state     = 'fighting'
        self.fighting_state = 'idle'
        
        self.items          = member.basic_items
        self.skills         = member.basic_skills
        self.passive        = member.passive
        
        self.CONTEXT        = ContextMenu()
        self.COMBAT_PROFILE = CombatProfile(self)
        self.COMBAT_ACTIONS = ActionSystem(self)
        
        self.current_lv    = 1
        self.current_xp    = 0
        self.total_xp      = self.current_xp

    def update(self):
        if self.COMBAT_PROFILE.CURRENT_HP <= 0:
            self.COMBAT_PROFILE.CURRENT_HP = 0
            self.main_state = 'defeated'
        update_sprt(self)
    
