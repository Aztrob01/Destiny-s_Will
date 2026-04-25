import pygame, random, operator
from core.damage import *

class Model:
    def __init__(self, name, requirements, description, data):
        self.name = name
        self.requirements = requirements
        self.description  = description
        self.data = data

class Passive(Model):
    def __init__(self, name, requirements, description):
        data = { 'name': name, 'type': 'passive', 'times_activated': 0 }
        super().__init__(name, requirements, description, data)

class Active(Model):
    def __init__(self, name, requirements, description):
        data = { 'name': name, 'type': 'sk_common', 'consuption': 0 }
        super().__init__(name, requirements, description, data)

class Ultimate(Model):
    def __init__(self, name, requirements, description):
        data = { 'name': name, 'type': 'sk_ult', 'consuption': 0 }
        super().__init__(name, requirements, description, data)


class Pact(Model):
    def __init__(self, name, requirements, description):
        data = { 'name': name, 'type': 'pact', 'times_activated': 0 }
        super().__init__(name, requirements, description, data)


