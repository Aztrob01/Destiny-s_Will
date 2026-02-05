import pygame
from root.settings import *
from cene.backgrounds import Background

class Combat:
    def __init__(self, background):
        self.display    = pygame.display.get_surface()
        self.background = Background(background)
        self.background = self.background.image

        self.PLAYER_TEAM  = []
        self.ENEMY_TEAM   = []

        self.PLAYER_TURN        = True
        self.MEMBER_TURN        = 0
        self.MEMBER_COLOR_IDLE  = (100, 100, 100)
        self.MEMBER_COLOR_TURN  = (30, 150, 30)
        self.RIGHTSIDE_POSITION = {
            0: (0.8, 0.46), 1: (0.847, 0.551), 2: (0.895, 0.643), 3: (0.766, 0.611),
            4: (0.721, 0.517),
        }

        self.ENTITY_TURN        = 0
        self.ENTITY_COLOR_IDLE  = (150, 40, 40)
        self.ENTITY_COLOR_DEAD  = (30, 30, 30)
        self.LEFTSIDE_POSITION  = {
            0: (0.195, 0.46), 1: (0.106, 0.643), 2: (0.154, 0.551), 3: (0.28, 0.51),
            4: (0.106, 0.643), 5: (0.17, 0.627)
        }
        
        self.TOTAL_TURNS  = 0
        
    def _update(self):
        for nums, members in enumerate(self.PLAYER_TEAM):
                members.update()

                # run over the PT lenght, if the player X isnt in the member allies list AND the player X isnt the member
                # adds ally to the member list
                for x in range(0, len(self.PLAYER_TEAM)):
                    if self.PLAYER_TEAM[x] not in members.CONTEXT.allies and self.PLAYER_TEAM[x] != members:
                        members.CONTEXT.allies.insert(-1, self.PLAYER_TEAM[x])        

                for enemies in self.ENEMY_TEAM:
                     if enemies not in members.COMBAT_ACTIONS.LISTOF_TARGETS:
                          members.COMBAT_ACTIONS.LISTOF_TARGETS.append(enemies)

        for entities in self.ENEMY_TEAM:
                entities.update()

                for x in range(0, len(self.ENEMY_TEAM)):
                    if self.ENEMY_TEAM[x] not in entities.CONTEXT.allies and self.ENEMY_TEAM[x] != entities:
                        entities.CONTEXT.allies.insert(-1, self.ENEMY_TEAM[x])

                for members in self.PLAYER_TEAM:
                     if members not in entities.COMBAT_ACTIONS.LISTOF_TARGETS:
                        entities.COMBAT_ACTIONS.LISTOF_TARGETS.append(members)
        
    def draw(self):
        self.display.blit(self.background, (0, 0))
        self._update()

        def draw_player_team_area(target):
            area_dimension = target.size[1] / 3
            
            area = pygame.draw.ellipse(self.display, (self.MEMBER_COLOR_IDLE if self.MEMBER_TURN != target.index else self.MEMBER_COLOR_TURN), (target.rect[0], target.rect[1] + (target.size[1] - area_dimension / 2), target.size[0], area_dimension))
            area.center = (target.rect[0], target.rect[1])


        def draw_player_team():
            for nums, members in enumerate(self.PLAYER_TEAM):
                members.rect.midbottom = ((WIDTH * self.RIGHTSIDE_POSITION[nums][0]), (HEIGHT * self.RIGHTSIDE_POSITION[nums][1]))
                draw_player_team_area(members)
                self.display.blit(members.sprite, (members.rect[0], members.rect[1]))
        def draw_enemy_team():
            for nums, entities in enumerate(self.ENEMY_TEAM):
                entities.rect.midbottom = ((WIDTH * self.LEFTSIDE_POSITION[nums][0]), (HEIGHT * self.LEFTSIDE_POSITION[nums][1]))
                entities.sprite = pygame.transform.flip(entities.sprite, 1, 0)
                self.display.blit(entities.sprite, (entities.rect[0], entities.rect[1]))

        draw_enemy_team()
        draw_player_team()

    def fight(self):

        if not self.PLAYER_TURN:
            if self.ENEMY_TURN > len(self.ENTITY_TURN):
                self.ENTITY_TURN = 0
                self.PLAYER_TURN = True 
            if self.ENEMY_TEAM[self.ENTITY_TURN].COMBAT_ACTIONS.play():
                self.ENTITY_TURN += 1
                self.TOTAL_TURNS += 1
        if self.PLAYER_TURN:
            if self.MEMBER_TURN > len(self.PLAYER_TEAM):
                self.MEMBER_TURN = 0
                self.PLAYER_TURN = False
            if self.PLAYER_TEAM[self.MEMBER_TURN].COMBAT_ACTIONS.play():
                self.MEMBER_TURN += 1
                self.TOTAL_TURNS += 1

        
        

    def start(self):
        self.draw()
        self.fight()