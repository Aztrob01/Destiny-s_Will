import pygame
import random

# -------------------------------------------
# C

class cvl:
    def __init__(self):
        self.data = {
            'class': { 'main': 'DUELIST', 'secondary': 'HIBRID' }, 
            'info':  { 'name': 'Claire Lemoine', 'codename': 'Cavaliere' },
            'stats': { 'hp': 100, 'str': 20, 'dex': 40, 'knw': 10, 'lky': 20, 'res': 10 }
        }
        
        self.sprites = {
            'explore': {
                'idle': None,
                'walk_up': None,
                'walk_down': None,
                'walk_side': None,
                'dead': None,
            },
            'fight':   {
                'idle': None,
                'running': None,
                'acting': None,

                'stuned': None,
                'hitted': None,
                'low': None,
                'dead': None,
            },
            'size':    {
                'default': (128, 128),
                'others': None,
            }
        }

class dpl:
    def __init__(self):
        self.data = {
            'class': { 'main': 'TANK', 'secondary': 'DAMAGE' }, 
            'info':  { 'name': 'Friedrich Knikovw', 'codename': 'Doppelsoldier' },
            'stats': { 'hp': 130, 'str': 40, 'dex': 10, 'knw': 10, 'lky': 5, 'res': 35 }
        }
        
        self.sprites = {
            'explore': {
                'idle': None,
                'walk_up': None,
                'walk_down': None,
                'walk_side': None,
                'dead': None,
            },
            'fight':   {
                'idle': None,
                'running': None,
                'acting': None,

                'stuned': None,
                'hitted': None,
                'low': None,
                'dead': None,
            },
            'size':    {
                'default': (128, 128),
                'others': None,
            }
        }


class alc:
    def __init__(self):
        self.data = {
            'class': { 'main': 'MAGE', 'secondary': 'DAMAGE' }, 
            'info':  { 'name': 'Lizze Osborn', 'codename': 'Alchemist' },
            'stats': { 'hp': 80, 'str': 10, 'dex': 30, 'knw': 40, 'lky': 10, 'res': 10 }
        }
        
        self.sprites = {
            'explore': {
                'idle': None,
                'walk_up': None,
                'walk_down': None,
                'walk_side': None,
                'dead': None,
            },
            'fight':   {
                'idle': None,
                'running': None,
                'acting': None,

                'stuned': None,
                'hitted': None,
                'low': None,
                'dead': None,
            },
            'size':    {
                'default': (128, 128),
                'others': None,
            }
        }

    


list = {
    0: alc,
    1: cvl,
    2: dpl,
}