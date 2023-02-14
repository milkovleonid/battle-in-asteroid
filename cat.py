import pygame.time
from pygame import *
import os


puhka = 0
PLATFORM_WIDTH = 64
PLATFORM_HEIGHT = 64
GRAVITY = 0.25
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами


class cattic(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image = image.load('%s/py_files/cat.png' % ICON_DIR)
        self.image = transform.scale(self.image, (64, 64))
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


