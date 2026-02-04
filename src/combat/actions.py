import pygame, random
            
class ActionSystem:
    def __init__(self, user):
       self.user = user
       
       self.action_pool = user.COMBAT_PROFILE.action_pool

       self.LISTOF_TARGETS  = []

       self.SELECTED_ACTION       = None
       self.SELECTED_ACTION_INDEX = 0
       self.SELECTED_TARGET       = None
       self.SELECTED_TARGET_INDEX = 0
       self.SELECTION_STAGE       = 'selecting'

       self.LAST_TARGET = None
       self.LAST_ACTION = None

    def update(self):
        self.user.COMBAT_PROFILE.pool_update()
        if self.SELECTED_ACTION != None:
            self.SELECTED_ACTION.set(self.user)

    def action(self):
        keys = pygame.key.get_pressed()
        self.update()
        
        if keys[pygame.K_a]:
            if self.SELECTED_ACTION_INDEX <= 0:
                self.SELECTED_ACTION_INDEX = len(self.action_pool)
            else:
                self.SELECTED_ACTION_INDEX -= 1

        if keys[pygame.K_d]:
            if self.SELECTED_ACTION_INDEX >= len(self.action_pool):
                self.SELECTED_ACTION_INDEX = 0
            else:
                self.SELECTED_ACTION_INDEX += 1
                
        if keys[pygame.K_SPACE]:
            self.SELECTION_STAGE = 'targeting'
            self.SELECTED_ACTION = self.action_pool[self.SELECTED_ACTION_INDEX]
            self.update()
    
    def targeting(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if self.SELECTED_TARGET_INDEX <= 0:
                self.SELECTED_TARGET_INDEX = len(self.LISTOF_TARGETS)
            else:
                self.SELECTED_TARGET_INDEX -= 1
        if keys[pygame.K_s]:
            if self.SELECTED_TARGET_INDEX >= len(self.LISTOF_TARGETS):
                self.SELECTED_TARGET_INDEX = 0
            else:
                self.SELECTED_TARGET_INDEX += 1
        if keys[pygame.K_SPACE]:
            self.SELECTED_TARGET = self.LISTOF_TARGETS[self.SELECTED_TARGET_INDEX]
            return True

    def play(self):
        if self.SELECTION_STAGE == 'selecting':
            self.action()
            
        elif self.SELECTION_STAGE == 'targeting':
            
            if self.targeting():
                self.action_pool[self.SELECTED_ACTION_INDEX].use(self.user, self.SELECTED_TARGET)
                self.SELECTION_STAGE = 'selecting'
                self.LAST_ACTION     = self.SELECTED_ACTION
                self.SELECTED_ACTION = None
                self.LAST_TARGET     = self.SELECTED_TARGET
                self.SELECTED_TARGET = None
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