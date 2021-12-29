import CMKuan_player, CMKuan_event
import pygame, os

class Game:
    __map = []
    __map_dict = {}
    __position =  None

    def __init__(self):
        self.__allsprite = pygame.sprite.Group()
        self.__clock = None
        self.__FPS = 40
        self.__player = None
        self.__screen = None
        self.__screen_height = 600
        self.__screen_width = 800

    def display_background(self):
        image_path = os.path.join("image", str(Game.__position)+".png")
        self.__screen.blit(Game.get_image(image_path, self.__screen_width, self.__screen_height), (0, 0))

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

    def display_player(self):
        self.__allsprite.update()
        self.__allsprite.draw(self.__screen)

    def display_status(self):
        background_color = (255, 255, 255)
        pygame.draw.rect(self.__screen, background_color, (600,0,200,100))  # (x, y, width, height)
        """
        show status text here if needed
        """
        text, text_rect = self.display_text("Time", 40)
        text_rect.topright = self.__screen_width, 0 # (right, top)
        self.__screen.blit(text, text_rect)
    
    def display_text(self, text, size):
        text_color = (0, 0, 139)    # #00008B_darkblue
        text_background_color = (50, 205, 50)   # #32CD32_lightgreen
        text_font = pygame.font.Font(pygame.font.match_font("微軟正黑體"), size)
        text = text_font.render(text, True, text_color, text_background_color)
        text_rect = text.get_rect()
        return text, text_rect

    def get_clock(self):
        return (self.__clock)
    
    def get_FPS(self):
        return (self.__FPS)

    def get_screen(self):
        return (self.__screen)

    def init_screen(self):
        pygame.init()
        self.__screen = pygame.display.set_mode([self.__screen_width, self.__screen_height])
        pygame.display.set_icon(Game.get_image('image\管中閔(左).jpg', 20, 20))
        pygame.display.set_caption("112 Simulator")

    def init_setting(self):
        self.__clock = pygame.time.Clock()
        Game.__map.extend([[0,0,0],[0,1,0],[0,0,0]])
        Game.__position = 4
        for i in range(3):
            for j in range(3):
                num = i*3+j
                Game.__map_dict[num] = [i, j]
        self.__player = CMKuan_player.Player()
        self.__allsprite.add(self.__player)

    def update_clock(self):
        self.__clock.tick(self.__FPS)
    
    @classmethod
    def get_image(cls, fileName, image_width, image_height):
        # fileName should be the relative path of the image
        cls.__image = pygame.image.load(fileName)
        cls.__image = pygame.transform.scale(cls.__image, (image_width, image_height))
        return (cls.__image)
    
    @classmethod
    def get_map(cls):
        return (cls.__map)
    
    @classmethod
    def get_position(cls):
        return (cls.__position)

    @staticmethod
    def update_class_map(position):
        Game.__map = [[0,0,0], [0,0,0], [0,0,0]]
        pos_x, pos_y = Game.__map_dict[position]
        Game.__map[pos_x][pos_y] = 1
        Game.__position = position