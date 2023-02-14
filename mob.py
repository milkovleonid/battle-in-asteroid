#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
import os

MONSTER_WIDTH = 22
MONSTER_HEIGHT = 64
health = 4
GRAVITY = 0.25
zrenie = 200
MONSTER_COLOR = "#2110FF"
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами


imagep_pack_died = [
    image.load('%s/py_files/smert0.png' % ICON_DIR),
    image.load('%s/py_files/smert1.png' % ICON_DIR),
    image.load('%s/py_files/smert2.png' % ICON_DIR),
    image.load('%s/py_files/smert3.png' % ICON_DIR),
    image.load('%s/py_files/smert4.png' % ICON_DIR),
    image.load('%s/py_files/smert5.png' % ICON_DIR)]


class Monster(sprite.Sprite):
    def __init__(self, x, y, coords):
        sprite.Sprite.__init__(self)
        self.coords = coords
        self.health = 3
        self.image = Surface((MONSTER_WIDTH, MONSTER_HEIGHT))
        self.image = image.load('%s/py_files/mobik.png' % ICON_DIR)
        self.prav = image.load('%s/py_files/mobik.png' % ICON_DIR)
        self.lev = image.load('%s/py_files/lmobik.png' % ICON_DIR)
        #self.image = transform.scale(self.image, (22, 64))
        self.rect = Rect(x, y, 22, 64)
        self.startX = x  # начальные координаты
        self.startY = y
        self.q = 0
        self.mask = mask.from_surface(self.image)
        self.onGround = True  # На земле ли я?
        self.xvel = 0  # cкорость передвижения по горизонтали, 0 - стоит на месте
        self.yvel = 0  # скорость движения по вертикали, 0 - не двигается
    def update(self, platforms, pula, tochka_prg, hero, korobk, zomba):
        if hero.rect.x < self.rect.x:
            self.image = self.lev
            self.image = transform.scale(self.image, (22, 64))
            self.mask = mask.from_surface(self.image)
            if hero.rect.x + 200 > self.rect.x:
                if self.rect.x not in range(hero.rect.x - 20, hero.rect.x + 20):
                    self.xvel = -1.5

        if hero.rect.x > self.rect.x:
            self.image = self.prav
            self.image = transform.scale(self.image, (22, 64))
            self.mask = mask.from_surface(self.image)
            if hero.rect.x < self.rect.x + 200:
                if self.rect.x not in range(hero.rect.x - 20, hero.rect.x + 20):
                    self.xvel = 1.5



        if self.health < 1:
            self.xvel = 0  # вычисляем сколько прошло секунд
            if self.health // -25 == 6:
                    zomba.remove(self.rect)
                    self.kill()

            elif self.health // -25 < 6:
                self.image = imagep_pack_died[self.health // -25]
                self.image = transform.scale(self.image, (22, 64))
        if not self.onGround:
            self.yvel += GRAVITY

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
            if hero.rect.y < self.rect.y and hero.rect.y < 480 and hero.rect.y > 292:
                if hero.rect.x < self.rect.x:
                    if p.rect.x - 7 == self.rect.x and p.rect.y - 64 == self.rect.y:
                        self.rect.y -= 68
                        self.rect.x -= 10

            if hero.rect.y < self.rect.y and hero.rect.y < 480 and hero.rect.y > 292:
                if hero.rect.x > self.rect.x:
                    if p.rect.x + 7 == self.rect.x and p.rect.y - 64 == self.rect.y:
                        self.rect.y -= 68
                        self.rect.x += 10


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
        chisl = 0
        wan = 0
        wan2 = 0
        chisl2 = 0
        for p in pula:
            if self.rect.x > 400:
                w = 0
                wan = 0
                while w < self.rect.x:
                    w += 400
                    wan += 1
            chisl = self.rect.x - 400 * wan
            if p.rect.x > 400:
                w1 = 0
                wan2 = 0
                while w1 < p.rect.x:
                    w1 += 400
                    wan2 += 1
            #chisl = self.rect.x - 400 * wan
            chisl2 = p.rect.x - 400 * wan2
            if self.mask.overlap_area(p.mask, (chisl2 - chisl, p.rect.y - self.rect.y)):
                print('-')
                self.health -= 1
                p.kill()

        for z in zomba:
            if sprite.collide_rect(self, z):  # если есть пересечение платформы с игроком
                #if z.rect.x in [self.rect.x - 10, self.rect.x + 10]:
                if z.rect.x < self.rect.x:
                    self.rect.left = z.rect.right

                #if z.rect.x in [self.rect.x - 10, self.rect.x + 10]:  # если движется влево
                if z.rect.x > self.rect.x:
                    self.rect.right = z.rect.left




