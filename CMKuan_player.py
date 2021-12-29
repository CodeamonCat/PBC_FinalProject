import pygame
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP, K_u

class Player(pygame.sprite.Sprite):

    def __init__(self):
        self.__height = 600
        self.__width = 800
        self.__player_height = 60
        self.__player_width = 60
        self.__speed = 5
        self.image = pygame.Surface((self.__player_width, self.__player_height))
        self.image = pygame.transform.scale(Player.get_image('image\管中閔(左).jpg', self.__player_width, self.__player_height), (self.__player_width, self.__player_height))
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.x = self.__width//2
        self.rect.y = self.__height//2

    def update(self):
        keys = pygame.key.get_pressed()
        
        # player move
        if keys[K_RIGHT]:
            self.rect.x += self.__speed
            self.image = pygame.transform.scale(Player.get_image('image\管中閔(右).jpg', self.__player_width, self.__player_height), (self.__player_width, self.__player_height))
        if keys[K_DOWN]:
            self.rect.y += self.__speed
        if keys[K_LEFT]:
            self.rect.x -= self.__speed
            self.image = pygame.transform.scale(Player.get_image('image\管中閔(左).jpg', self.__player_width, self.__player_height), (self.__player_width, self.__player_height))
        if keys[K_UP]:
            self.rect.y -= self.__speed

        # boundary case
        if self.rect.right >= self.__width:
            self.rect.x -= (self.__width-self.__player_width)
        if self.rect.bottom >= self.__height:
            self.rect.y -= (self.__height-self.__player_height)
        if self.rect.left <= 0:
            self.rect.x += (self.__width-self.__player_width)
        if self.rect.top <= 0:
            self.rect.y += (self.__height-self.__player_height)

    @classmethod
    def get_image(cls, fileName, image_width, image_height):
        # fileName should be the relative path of the image
        cls.__image = pygame.image.load(fileName)
        cls.__image = pygame.transform.scale(cls.__image, (image_width, image_height))
        return (cls.__image)
