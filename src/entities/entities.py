import pygame, random
from root.utilities import update_sprt


from combat.profile import CombatProfile
from combat.actions import SimpleLevelActionSystem
from combat.context import ContextMenu

class Entities:
    def __init__(self, entity):
        self.origin     = entity
        self.codename   = entity.codename
        self.on_screen  = entity.size
        self.randomized = False
        self.index      = 0
        
        self.main_state     = 'fighting'
        self.fighting_state = 'idle'

        self.current_lv    = 1

        self.skills  = entity.basic_skills
        self.passive = entity.passive

        self.CONTEXT        = ContextMenu()
        self.COMBAT_PROFILE = CombatProfile(self)
        self.COMBAT_ACTIONS = SimpleLevelActionSystem(self)
        self.randomize()

    def randomize(self):
        if not self.randomized:
            self.current_lv = random.randint(1, 5)
            for stats in self.COMBAT_PROFILE.BRUTE_STATS:
                if self.origin.basic_stats[stats] != 0:
                    final_value = int((self.origin.basic_stats[stats] * self.current_lv) / 2)
                    self.COMBAT_PROFILE.BRUTE_STATS[stats] += random.randint(1, final_value)
            self.randomized = True

    def update(self):
        if self.COMBAT_PROFILE.CURRENT_HP <= 0:
            self.COMBAT_PROFILE.CURRENT_HP = 0
            self.main_state = 'defeated'
        update_sprt(self)
        
        