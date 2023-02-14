from pygame import *
import random
import os
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 22


ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами
dropi = [('%s/py_files/vintovka.png' % ICON_DIR),
         ('%s/py_files/rygye.png' % ICON_DIR)]


class drop(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.a = random.randint(1, 10)
        self.da = False
        self.ww = 0
        if self.a in [1, 6]:
            self.image = image.load(dropi[0])
            self.image = transform.scale(self.image, (64, 32))
        else:
            self.image = image.load(dropi[1])
            self.image = transform.scale(self.image, (64, 32))
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


    def update(self, hero, veapon, sp_orug, dropi):
        if sprite.collide_rect(self, hero):

            if self.a in [1, 6]:
                sp_orug.append('1')
                self.ww = 1

            else:
                sp_orug.append('2')
                self.ww = 2
            self.da = True
        if self.da:
            self.kill()
            dropi.remove(self.rect)
