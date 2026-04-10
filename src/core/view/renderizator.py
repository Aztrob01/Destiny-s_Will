import pygame
from core.manager_data import DataLoader

class Renderization:
    def __init__(self):
        self.__display = pygame.display.get_surface()
        self.__loader  = DataLoader()

        self.__world      = None
        self.__background = None
        self.__entity     = None

    def draw_world(self, level, offset):
        pass

    def draw_background(self, path, pos):
        pass

    def draw_entity(self, entity, pos):
        entity.sprite.update(entity.state)

        res = self.__loader.data_settings['video']['actual_res']
        if pos[0] >= 0 and pos[0] <= res[0]:
            if pos[1] >= 0 and pos[1] <= res[1]:
                if entity.rect is None:
                    entity.sprite.rect = entity.sprite.image.get_rect()
                entity.sprite.rect.midbottom = pos
                self.__display.blit(entity.sprite.image, entity.sprite.rect)

            



