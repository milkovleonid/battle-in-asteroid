#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pygame import *
import os
import math

MONSTER_WIDTH = 64
MONSTER_HEIGHT = 64
health = 5
zrenie = 75
vistrel = False


ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами




class zzy(sprite.Sprite):
    def __init__(self, x, y, coords):
        sprite.Sprite.__init__(self)
        self.coords = x, y
        self.health = 12
        self.image = Surface((MONSTER_WIDTH * 2, MONSTER_HEIGHT * 3))
        self.image = image.load('%s/py_files/zzy.png' % ICON_DIR)
        self.prav = image.load('%s/py_files/zzy.png' % ICON_DIR)
        self.lev = image.load('%s/py_files/zzy.png' % ICON_DIR)
        self.image = transform.scale(self.image, (128, 192))
        self.rect = Rect(x, y, MONSTER_WIDTH * 2, MONSTER_HEIGHT * 3)
        self.startX = x  # начальные координаты
        self.startY = y
        self.q = 0
        self.onGround = True  # На земле ли я?
        self.xvel = 0  # cкорость передвижения по горизонтали, 0 - стоит на месте
        self.yvel = 0  # скорость движения по вертикали, 0 - не двигается

    def update(self, platforms, pula, tochka_prg, hero, korobk, zomba):
        if hero.rect.x < self.rect.x:
            self.image = self.lev
            self.image = transform.scale(self.image, (128, 192))
            if hero.rect.x + 400 > self.rect.x:
                if self.rect.x not in range(hero.rect.x - 20, hero.rect.x + 20):
                    self.xvel = -0.25

        if hero.rect.x > self.rect.x:
            self.image = self.prav
            self.image = transform.scale(self.image, (128, 192))
            if hero.rect.x < self.rect.x + 400:
                if self.rect.x not in range(hero.rect.x - 20, hero.rect.x + 20):
                    self.xvel = 0.25
        if self.health < 1:
            self.xvel = 0
            self.kill()


        if not self.onGround:
            self.yvel += 0.25

        self.onGround = False  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms, pula, tochka_prg, hero, korobk, zomba)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms, pula, tochka_prg, hero, korobk, zomba)

    def collide(self, xvel, yvel, platforms, pula, tochka_prg, hero, korobk, zomba):
        for p in platforms:
            if sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком
                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0


        for o in korobk:
            if sprite.collide_rect(self, o):  # если есть пересечение пла
                if xvel > 0:  # если движется вправо
                    self.rect.right = o.rect.left  # то не движется вправ
                if xvel < 0:  # если движется влево
                    self.rect.left = o.rect.right  # то не движется влево
                if yvel > 0:  # если падает вниз
                    self.rect.bottom = o.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердо
                    self.yvel = 0  # и энергия падения пропадает
                if yvel < 0:  # если движется вверх
                    self.rect.top = o.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает
        for p in pula[:]:
            if sprite.collide_rect(self, p):
                self.health -= 1







