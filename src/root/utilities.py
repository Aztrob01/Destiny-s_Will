from root.settings import *
import pygame

def update_sprt(target):
    for states in target.origin.inner_galery:
        if target.main_state != 'fighting':
            target.sprite = target.origin.inner_galery[target.main_state]
        else:
            target.sprite = target.origin.inner_galery[target.main_state][target.fighting_state]

    target.sprite = pygame.transform.scale(target.sprite, (target.on_screen))
    target.rect = target.sprite.get_rect()
    target.size = target.sprite.get_size()

class Timer:
    def __init__(self, delay):
        self.delay = delay
        self.ltime = 0

    def wait(self):
        ctime = pygame.time.get_ticks()
        if ctime - self.ltime > self.delay:
            self.ltime = ctime
            return True
        return False
        
