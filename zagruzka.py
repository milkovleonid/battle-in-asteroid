from pygame import *
import os
kol_vo_yr = 2
ICON_DIR = os.path.dirname(__file__)
width = 700
height = 700
black = (0, 0, 0)
white = (255, 255, 255)
perehod1 = False
perehod2 = False
zv2 = 0
zv1 = 0


class knop1(sprite.Sprite):
    def __init__(self, click, pos, zv1, zv11):
        sprite.Sprite.__init__(self)
        self.sostoyanie = 0
        self.image11 = image.load('%s/py_files/pixil-frame-0 (3).png' % ICON_DIR)
        self.image12 = image.load('%s/py_files/pixil-frame-0 (10).png' % ICON_DIR)
        self.image13 = image.load('%s/py_files/pixil-frame-0 (11).png' % ICON_DIR)
        sp_iz = [self.image11, self.image12, self.image13]
        if zv1:
            self.a = sp_iz[1]
        elif zv11:
            self.a = sp_iz[2]
        else:
            self.a = sp_iz[0]
        self.a = transform.scale(self.a, (500, 500))
        self.image = self.a
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 150, 200



class knop2(sprite.Sprite):
    def __init__(self, click, pos, zv2, zv21):
        sprite.Sprite.__init__(self)
        self.sostoyanie = 0
        self.image21 = image.load('%s/py_files/pixil-frame-0 (8).png' % ICON_DIR)
        self.image22 = image.load('%s/py_files/pixil-frame-0 (7).png' % ICON_DIR)
        self.image23 = image.load('%s/py_files/pixil-frame-0 (6).png' % ICON_DIR)
        sp_iz1 = [self.image21, self.image22, self.image23]
        if zv2:
            self.b = sp_iz1[1]
        elif zv21:
            self.b = sp_iz1[2]
        else:
            self.b = sp_iz1[0]
        self.b = transform.scale(self.b, (500, 500))
        self.image = self.b
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 450, 200



