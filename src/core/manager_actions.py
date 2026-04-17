import pygame

from core.manager_inputs import inputManager

class ActionManager:
    def __init__(self, events):
        self.__input = inputManager(events)
        
        self.__user_id = 0
        self.__targets = [] 
        self.__target  = 0
        self.__skills  = []
        self.__skill   = 0
        self.state     = 0

    def save(self, user_data):
        pass

    def undone(self, user_save):
        pass

    def update(self, user_skills):
        pass

    def check(self, user_id):
        pass

    def select_sk(self):
        output = self.__input.key_mult_up(pygame.K_s, pygame.K_w)
        if output is False:
            self.__skill = (self.__skill - 1) if self.__skill > 0 else (len(self.__skills) - 1)
        elif output is True:
            self.__skill = (self.__skill + 1) if self.__skill < (len(self.__skills) - 1) else 0

        if self.__input.key_up(pygame.K_SPACE):
            self.update(self.__skills)
            self.state += 1

    def select_tg(self):
        output = self.__input.key_mult_up(pygame.K_a, pygame.K_d)
        if output is False:
            self.__target = (self.__target - 1) if self.__target > 0 else (len(self.__targets) - 1)
        if output is True:
            self.__target = (self.__target + 1) if self.__target < (len(self.__targets) - 1) else 0
        
        if self.__input.key_up(pygame.K_SPACE):
            self.state += 1

    def play(self, user):
        match self.state:
            case 0:
                self.select_sk()
            case 1:
                self.select_tg()
            case 2:
                return [self.__skills[self.__skill], self.__targets[self.__target]]
            case _:
                return None
        
        
    
                