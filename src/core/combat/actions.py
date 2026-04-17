import pygame, random

test = { 
    'user': 
            { 
              'stats': None, 
              'other': None
            },
    'fight': 
            { 
              'general': None,
              'team': None,
              'enemy': None
            },
    'usage': 
            { 
                'times': 0,
            }
}

class MainAction:
    def __init__(self, name, type, conditions, requirements):
        self.name = name
        self.type = type
        self.conditions   = conditions
        self.requirements = requirements

class Vote:
    def __init__(self):
        pass

class Passive:
    def __init__(self):
        pass

class Active:
    def __init__(self):
        pass

class Teste(MainAction):
    def __init__(self):
        super().__init__("Nome de Teste", Vote(), None, None)
    
teste = Teste()
teste.tries(0)




skills = {
    'passive':{},
    'pacts': {},
    'skills': {},
    'ultimate': {}     
}
