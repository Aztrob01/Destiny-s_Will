import pygame, random
from root.utilities import Timer
            
class ActionSystem:
    def __init__(self, user):
        self.user = user
        self.Time = Timer(250)
        
        self.action_pool = user.COMBAT_PROFILE.action_pool

        self.LISTOF_ENEMIES  = []
        self.LISTOF_ALLIES   = []
        self.LISTOF_TARGETS  = []
         

        self.SELECTED_ACTION       = None
        self.SELECTED_ACTION_INDEX = 0
        self.SELECTED_TARGET       = 0
        self.SELECTED_TARGET_INDEX = 0
        self.SELECTION_STAGE       = 'Selecting'

        self.LAST_TARGET = None
        self.LAST_ACTION = None

    def update(self):
        self.user.COMBAT_PROFILE.pool_update()
        
        for allies in self.LISTOF_ALLIES: #!
            if allies == self.user:
                self.LISTOF_ALLIES.remove(allies)

        for enemies in self.LISTOF_ENEMIES:
            if enemies.main_state != 'dead' and enemies not in self.LISTOF_TARGETS:
                self.LISTOF_TARGETS.append(enemies)
        if self.SELECTED_ACTION != None:
            self.SELECTED_ACTION.set(self.user)

    def action(self):
        keys = pygame.key.get_pressed()
        start_value = self.SELECTED_ACTION_INDEX
        self.update()

        if keys[pygame.K_a]:
            if self.Time.wait():
                if self.SELECTED_ACTION_INDEX <= 0:
                    self.SELECTED_ACTION_INDEX = len(self.action_pool)
                else:
                    self.SELECTED_ACTION_INDEX -= 1
        elif keys[pygame.K_d]:
            if self.Time.wait():
                if self.SELECTED_ACTION_INDEX >= len(self.action_pool):
                    self.SELECTED_ACTION_INDEX = 0
                else:
                    self.SELECTED_ACTION_INDEX += 1

        
        if start_value != self.SELECTED_ACTION_INDEX:
            print(f'Mudando de ação para {self.action_pool[self.SELECTED_TARGET_INDEX].name}')

        if keys[pygame.K_SPACE]:
            if self.Time.wait():
                self.SELECTED_ACTION = self.action_pool[self.SELECTED_ACTION_INDEX]
                self.SELECTION_STAGE = 'Targeting'
                self.update()

    def targeting(self):
        start_value = self.SELECTED_TARGET_INDEX
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            if self.Time.wait():
                if self.SELECTED_TARGET_INDEX <= 0:
                    self.SELECTED_TARGET_INDEX = len(self.LISTOF_TARGETS) - 1
                else:
                    self.SELECTED_TARGET_INDEX -= 1
        elif keys[pygame.K_s]:
            if self.Time.wait():
                if self.SELECTED_TARGET_INDEX >= (len(self.LISTOF_TARGETS) - 1):
                    self.SELECTED_TARGET_INDEX = 0
                else:
                    self.SELECTED_TARGET_INDEX += 1
        
        if start_value != self.SELECTED_TARGET_INDEX:
            for targets in self.LISTOF_TARGETS:
                print(f'Alvos: {targets.codename}')
            print(f'Mudando de alvo para alvo {self.LISTOF_TARGETS[self.SELECTED_TARGET_INDEX].codename} [{self.LISTOF_TARGETS[self.SELECTED_TARGET_INDEX].index}]')

        if keys[pygame.K_SPACE]:
            if self.Time.wait():
                self.SELECTED_TARGET = self.LISTOF_TARGETS[self.SELECTED_TARGET_INDEX]
                print(f'Alvo selecionado: {self.SELECTED_TARGET.codename} [{self.SELECTED_TARGET_INDEX}]')
                return True

    def play(self):
        if self.SELECTION_STAGE == 'Selecting':
            self.action()
        else:
            if self.targeting():
                self.SELECTION_STAGE = 'Selecting'
                self.SELECTED_ACTION.use(self.user, self.SELECTED_TARGET)
                self.LAST_ACTION = self.SELECTED_ACTION
                self.LAST_TARGET = self.SELECTED_TARGET
                self.SELECTED_ACTION = None
                self.SELECTED_TARGET = None
                self.SELECTED_ACTION_INDEX, self.SELECTED_TARGET_INDEX = (0, 0)
                return True
                
        

class SimpleLevelActionSystem:
    def __init__(self, user):
        self.user = user

        self.action_pool = user.COMBAT_PROFILE.action_pool

        self.LISTOF_TARGETS  = []

        self.LAST_TARGET = None
        self.LAST_ACTION = None

    def update(self):
        self.user.COMBAT_PROFILE.pool_update()
        if self.SELECTED_ACTION != None:
            self.SELECTED_ACTION.set(self.user)

    def play(self):
        RANDOMACT    = random.choice(self.action_pool)
        RANDOMTARGET = random.choice(self.LISTOF_TARGETS)

        RANDOMACT.use(self.user, RANDOMTARGET)
        self.LAST_ACTION = RANDOMACT
        self.LAST_TARGET = RANDOMTARGET
        return True