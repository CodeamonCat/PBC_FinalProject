import sys
import pygame
from pygame.locals import QUIT

class Game:

    def __init__(self) -> None:
        self.__screen = None
        self.__screen_width = 800
        self.__screen_height = 600
    
    def init_screen(self):
        pygame.init()
        self.__screen = pygame.display.set_mode((self.__screen_width, self.__screen_height))
        pygame.display.set_caption('Hello World:)')
        self.__screen.fill((255, 255, 255))

    def init_showText(self):
        head_font = pygame.font.SysFont(None, 60)
        text_surface = head_font.render('Hello World!', True, (0, 0, 0))
        self.__screen.blit(text_surface, (10, 10))

def gameLoop(gameName):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    gameName.init_screen()
                    pygame.display.update()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == '__main__':
    test = Game()
    test.init_screen()
    test.init_showText()
    pygame.display.update()
    gameLoop(test)
