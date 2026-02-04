import pygame
from root.settings import *
from cene.backgrounds import Background

class Combat:
    def __init__(self, background):
        self.display = pygame.display.get_surface()
        
        self.ACTIVE_TURN = 'player'
        self.PLAYER_TEAM = []
        self.PLAYER_TURN = 0
        self.ENEMY_TEAM  = []
        self.ENEMY_TURN  = 0
        self.zero = 0
        
        self.TOTAL_TURNS  = 0
        self.TOTAL_ROUNDS = 0
        
        self.LEFTSIDE_POSITION  = {
            0: (0.195, 0.46), 1: (0.106, 0.643), 2: (0.154, 0.551), 3: (0.28, 0.51),
            4: (0.106, 0.643), 5: (0.17, 0.627)
        }
        self.RIGHTSIDE_POSITION = {
            0: (0.8, 0.46), 1: (0.847, 0.551), 2: (0.895, 0.643), 3: (0.766, 0.611),
            4: (0.721, 0.517),
        }
        
        self.bggen      = Background(background)
        self.background = self.bggen.image
        self.ui         = None

    def _update(self):
        
        for nums, members in enumerate(self.PLAYER_TEAM):
                possible_nums = [0, 1, 2]
                members.update()
                
                possible_nums.remove(nums)

                for allies in possible_nums:
                    if self.PLAYER_TEAM[allies] not in members.CONTEXT.ALLIES:
                        members.CONTEXT.ALLIES.insert(-1, allies)

                for enemies in self.ENEMY_TEAM:
                     if enemies not in members.COMBAT_ACTIONS.LISTOF_TARGETS:
                          members.COMBAT_ACTIONS.LISTOF_TARGETS.append(enemies)

        for entities in self.ENEMY_TEAM:
                entities.update()
                for members in self.PLAYER_TEAM:
                     if members not in entities.COMBAT_ACTIONS.LISTOF_TARGETS:
                          entities.COMBAT_ACTIONS.LISTOF_TARGETS.append(members)
            

    def draw(self):
        self.display.blit(self.background, (0, 0))
        self._update()

        def draw_player_team():
            for nums, members in enumerate(self.PLAYER_TEAM):
                members.rect.midbottom = ((WIDTH * self.RIGHTSIDE_POSITION[nums][0]), (HEIGHT * self.RIGHTSIDE_POSITION[nums][1]))
                self.display.blit(members.sprite, (members.rect[0], members.rect[1]))
        def draw_enemy_team():
            for nums, entities in enumerate(self.ENEMY_TEAM):
                entities.rect.midbottom = ((WIDTH * self.LEFTSIDE_POSITION[nums][0]), (HEIGHT * self.LEFTSIDE_POSITION[nums][1]))
                entities.sprite = pygame.transform.flip(entities.sprite, 1, 0)
                self.display.blit(entities.sprite, (entities.rect[0], entities.rect[1]))

        draw_enemy_team()
        draw_player_team()


    def fight(self):
        if self.ACTIVE_TURN == 'player':
            if self.PLAYER_TEAM[self.PLAYER_TURN].COMBAT_ACTIONS.play():
                self.PLAYER_TURN += 1
                if self.PLAYER_TURN >= len(self.PLAYER_TEAM):
                     self.PLAYER_TURN = 0
                     self.ACTIVE_TURN = 'enemy'
        if self.ACTIVE_TURN == 'enemy':
             if self.ENEMY_TEAM[self.ENEMY_TURN].COMBAT_ACTIONS.play():
                  self.ENEMY_TURN += 1
                  if self.ENEMY_TURN >= len(self.ENEMY_TEAM):
                       self.ENEMY_TURN = 0
                       self.ACTIVE_TURN = 'player'
        

    def start(self):
        self.draw()
        self.fight()