#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Импортируем библиотеку pygame
import sys

import pygame.display
from pygame import *

import sama_igra
import cat
from mob import *
from korob import *
from drop import *
from sama_igra import *
from strelba import *
from platform import *
from turel import *
import os
from zagruzka import *
import math

# Объявляем переменные

pul_coor = (0, 0)
WIN_WIDTH = 800  # Ширина создаваемого окна
WIN_HEIGHT = 640  # Высота
ICON_DIR = os.path.dirname(__file__)
veapon = 0
zv11 = False
zv2 = False
zv1 = False
zv21 = False
sp_orug = [0]
oboyma_0 = 22
all_bullets = []
oboyma_1 = 30
CameraX, CameraY = 0, 0
oboyma_2 = 6
bullets_0 = 31
flag = False
ty = False
bullets_1 = 30
vistrels = 0
bullets_2 = 12
ideal_oboyma_0 = 22
ideal_oboyma_1 = 30
ideal_oboyma_2 = 6
zrenie = 75
tch1, tch2 = 0, 0
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_1 = ('%s/py_files/lvl1.png' % ICON_DIR)
zast = ('%s/py_files/zastavka.png' % ICON_DIR)

BACKGROUND_2 = ('%s/py_files/lvl2.png' % ICON_DIR)

hero = Player((66, 512))
veaponi = hero.veapon

def menu(screen, zv1, zv2, zv11, zv21):
    flag = False
    timer = pygame.time.Clock()
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    entiti = pygame.sprite.Group()
    bg = image.load(zast)
    bg = transform.scale(bg, (800, 640))
    click = False
    knopk1 = knop1(click, mouse.get_pos(), zv1, zv11)
    knopk2 = knop2(click, mouse.get_pos(), zv2, zv21)

    entiti.add(knopk2, knopk1)
    screen.blit(bg, (0, 0))
    for e in entiti:
        screen.blit(e.image, e.rect)

    pygame.display.flip()
    stop = 1
    while stop:
        timer.tick(60)
        for event in pygame.event.get():  # Обрабатываем события
            if event.type == QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if mouse.get_pos()[0] in range(150, 330) and mouse.get_pos()[1] in range(280, 460):
                        sostoyanie = 1
                        stop = 0
                    if mouse.get_pos()[0] in range(450, 630) and mouse.get_pos()[1] in range(280, 460):
                        flag = True
                        sostoyanie = 2
                        stop = 0
    return flag

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)
        self.dx = 0
        self.dy = 0

    def apply(self, target):
        bb = target.rect
        return bb.move(self.state.topleft)

    def update(self, target):
        bb = target.rect
        self.state = self.camera_func(self.state, bb)


    def reverse(self, pos):
        return (pos[0] - self.state.left, pos[1] -self.state.top)

    def reverse1(self, pos):
        return (pos[0] - self.state.left, pos[1] -self.state.top)

def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    t = -t + WIN_HEIGHT / 2
    l = -l + WIN_WIDTH / 2



    l = min(0, l)  # Не движемся дальше левой границы

    l = max(-(camera.width - WIN_WIDTH), l)  # Не движемся дальше правой границы
    if -l > 0:
        q = 0
        s = 0
        while q < -l:
            q += 400
            s += 1
        l = -400 * s
    t = max(-(camera.height - WIN_HEIGHT), t)  # Не движемся дальше нижней границы
    t = min(0, t)  # Не движемся дальше верхней границы

    return Rect(l, t, w, h)

def main():
    sostoyanie = 0
    vistrels = 0
    flag = False
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("battle in the Asteroid")  # Пишем в шапку

    if sostoyanie == 0:
        yr = menu(screen, False, False, False, False)



    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    # будем использовать как фон
    bg = image.load(BACKGROUND_1)  # Заливаем поверхность сплошным цветом
    if yr:
        bg = image.load(BACKGROUND_2)
    bg = transform.scale(bg, (830, 640))
    left = right = False  # по умолчанию - стоим
    r = f = False
    up = False
    entities = pygame.sprite.Group()  # Все объекты
    pullit = pygame.sprite.Group()
    pulli = pygame.sprite.Group()
    platforms = []  # то, во что мы будем врезаться или опираться
    zomba = []
    TURELI = []
    korobk = []
    tochki = []
    dropi = []
    sp_puli = []
    puli_tur = []
    zzyq = []
    turel_P = []

    entities.add(hero)

    level = [
        "--------------------------------------------------------------------",
        "-                                                                   -",
        "-          z    z   z                           z                   -",
        "-       -     --  --                                                -",
        "-                                                       z           -",
        "-                     -         #                      ---          -",
        "-                            ----                                   -",
        "-       ----    --       --                z       -          -     -",
        "-              z       z                 # #     z     z            -",
        "--------------------------------------------------------------------"]

    level1 = [
        "--------------------------------------------------------------------",
        "-                                                                  -",
        "-        z          z                                              -",
        "-       -         --           -            z                      -",
        "-               -                           -                      -",
        "-           z           -          #                      ---   z  -",
        "-          -                   -  -                           ------",
        "-       -            -      --                       -        -    -",
        "-              z              z   z  z    W        z     z       c -",
        "--------------------------------------------------------------------"]

    timer = pygame.time.Clock()
    cor_z = []
    x = y = 0  # координаты
    levelin = level
    if flag == True:
        levelin = level1
    for row in levelin:  # вся строка
        for col in row:  # каждый символ
            if col == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "z":
                ms = Monster(x, y, (hero.rect.x, hero.rect.y))
                entities.add(ms)
                cor_z.append((x, y))
                zomba.append(ms)

            if col == "#":
                korobc = korob(x, y)
                entities.add(korobc)
                korobk.append(korobc)
                if random.randint(1, 40) in [7, 9, 17, 31, 25, 3, 18]:
                    droping = drop(x, y)
                    entities.add(droping)
                    dropi.append(droping)
            if col == "W":
                Zzy = zzy(x, y, (hero.rect.x, hero.rect.y))
                entities.add(Zzy)
                zzyq.append(Zzy)
            if col == "c":
                catt = cat.cattic(x, y)
                entities.add(catt)


            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля
    total_level_width = len(levelin[0]) * PLATFORM_WIDTH
    total_level_height = len(levelin) * PLATFORM_HEIGHT
    camera = Camera(camera_configure, total_level_width, total_level_height)
    while 1:  # Основной цикл программы
        timer.tick(60)
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == QUIT:
                exit()
            if e.type == KEYDOWN and e.key == K_f:
                f = True
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == pygame.MOUSEBUTTONDOWN:
                click = True
                if hero.rect.x > 400:
                    q = 0
                    s = 0
                    while q < hero.rect.x:
                        q += 400
                        s += 1
                    bb = hero.rect.x - (400 * (s - 1))
                else:
                    bb = hero.rect.x
                if vistrels < 10:
                    pula = buttonin(mouse.get_pos(), (bb, hero.rect.y), veaponi)
                    sp_puli.append(pula)
                    pulli.add(pula)
                    vistrels += 1


            if e.type == KEYDOWN and e.key == K_r:
                vistrels = 0
                r = True
            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYUP and e.key == K_r:
                r = False
            if e.type == KEYUP and e.key == K_f:
                f = False

        screen.blit(bg, (0, 0))

        # Каждую итерацию необходимо всё перерисовывать
        camera.update(hero)

        # центризируем камеру относительно персонажа
        hero.update(left, right, up, platforms, sp_orug, r, f, dropi, zomba, veapon, oboyma_0, oboyma_1, oboyma_2,
                    bullets_0, bullets_1, bullets_2, ideal_oboyma_0, ideal_oboyma_1, ideal_oboyma_2, korobk, sostoyanie, zzyq)
        img = image.load(('%s/py_files/serdce.png' % ICON_DIR))
        img = transform.scale(img, (50, 50))
        pygame.font.init()  # you have to call this at the start,
        # if you want to use this module.
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface = my_font.render('10/' + str(10 - vistrels), False, (0, 0, 0))

        if hero.health < 0:
            menu(screen, False, False, False, False)
            hero.rect.x = 66
            hero.health = 100
            main()
        for z in zomba:
            z.update(platforms, sp_puli, tochki, hero, korobk, zomba)




        for zo in zzyq:
            zo.update(platforms, sp_puli, tochki, hero, korobk, zomba)
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        if hero.health > 75:
            screen.blit(img, (270, 0))
        if hero.health > 50:
            screen.blit(img, (190, 0))
        if hero.health > 25:
            screen.blit(img, (110, 0))
        if hero.health > 1:
            screen.blit(img, (30, 0))
        screen.blit(text_surface, (720, 590))
        for k in korobk:
            k.update(zomba, pulli, korobk)
        for bullet in pulli:
            camera.apply(bullet)
            bullet.update(screen, hero, platforms, zomba, korobk, pulli)
            for i in zomba:
                if Rect.colliderect(bullet.rect, i):
                    pulli.remove(bullet)
                    bullet.kill()
            for j in korobk:
                if Rect.colliderect(bullet.rect, j):
                    pulli.remove(bullet)
                    bullet.kill()
            for p in platforms:
                if Rect.colliderect(bullet.rect, p):
                    pulli.remove(bullet)
                    bullet.kill()
        if flag and hero.rect.x in range(3900, 3915):
            zv2 = True
            menu(screen, zv2, False, False, False)
            if zomba == []:
                zv21 = True
                menu(screen, False, zv2, False, zv21)
            hero.rect.x = 66
            hero.health = 100
            main()
        if hero.rect.x in range(4065, 4075) and not flag:
            zv1 = True
            menu(screen, zv1, False, False, False)
            if zomba == []:
                zv11 = True
                menu(screen, zv1, False, zv11, False)
            hero.rect.x = 66
            hero.health = 100
            main()
        pygame.display.update()  # обновление и вывод всех изменений на экран


if __name__ == "__main__":
    main()
