import pygame

from root.settings import *
from core.level    import LevelCreator

# * Main Game Loop

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.m_name = pygame.display.set_caption('Dragon Rose')
        self.clock  = pygame.time.Clock()
        self.level  = LevelCreator()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       

                
            self.level.play()
            # pygame.draw.ellipse(self.screen, (90, 90, 90), (WIDTH / 2, HEIGHT / 2, 50, 20))

            pygame.display.update()
            self.clock.tick(GAMECLOCK)

if __name__ == '__main__':
    game = Game()
    game.run()