import pygame

class Game:

    def __init__(self):
        self.__clock = None
        self.__FPS = 40
        self.__screen = None
        self.__screen_width = 800
        self.__screen_height = 600
    
    def init_screen(self):
        pygame.init()
        self.__screen = pygame.display.set_mode([self.__screen_width, self.__screen_height])
        pygame.display.set_icon(Game.get_image('image\管中閔(左).jpg', 20, 20))
        pygame.display.set_caption("112 Simulator")

    def display_cover(self):
        cover_background = Game.get_image('image\start.jpg', self.__screen_width, self.__screen_height)
        self.__screen.blit(cover_background, (0, 0))
        """
        show text here if needed
        """
        pygame.display.update()
        display_cover = True
        while display_cover:
            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == event.key:
                            print("===leave cover page")
                            display_cover = False
                    if event.type == pygame.QUIT:
                        pygame.quit()

    def init_setting(self):
        self.__clock = pygame.time.Clock()

    def get_clock(self):
        return (self.__clock)
    
    def get_FPS(self):
        return (self.__FPS)

    def get_screen(self):
        return (self.__screen)

    @classmethod
    def get_image(cls, fileName, image_width, image_height):
        # fileName should be the relative path of the image
        cls.__image = pygame.image.load(fileName)
        cls.__image = pygame.transform.scale(cls.__image, (image_width, image_height))
        return (cls.__image)