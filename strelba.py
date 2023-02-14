import pygame
from pygame import *
import math
import os


ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами
all_bullets = []

pul = ('%s/py_files/pula.png' % ICON_DIR)

class buttonin(sprite.Sprite):
    def __init__(self, posit, po, veaponi):
        sprite.Sprite.__init__(self)
        self.pos = po[0] + 20, po[1] + 32
        mx, my = posit
        self.dir = (mx - self.pos[0], my - self.pos[1])
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0] / length, self.dir[1] / length)
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
        self.image = pygame.Surface((7, 2)).convert_alpha()
        self.image = image.load(pul)
        self.image = transform.scale(self.image, (7, 2))
        self.image = pygame.transform.rotate(self.image, angle)
        self.mask = mask.from_surface(self.image)
        self.speed = 4
        if veaponi == 0:
            self.rect = Rect(self.pos, (7, 2))
        elif veaponi == 1:
            self.rect = Rect(self.pos, (7, 2))
            self.speed = 5
        else:
            self.rect = Rect(self.pos, (8, 4))
        print(veaponi)

    def update(self, screen, coords, platforms, zomba, korobk, pulli):

        self.pos = (self.pos[0] + (self.dir[0] * self.speed),
                    self.pos[1] + (self.dir[1] * self.speed))
        self.rect.x, self.rect.y = self.pos
        self.coolide(platforms, zomba, korobk, pulli)
        screen.blit(self.image, self.rect)
    def coolide(self, platforms, zomba, korobk, pulli):
        for p in platforms:
            if Rect.colliderect(self.rect, p):
                pulli.remove(self.rect)
                self.kill()
        for z in zomba:
            if Rect.colliderect(self.rect, z):
                pulli.remove(self.rect)
                self.kill()
        for k in korobk:
            if Rect.colliderect(self.rect, k):
                pulli.remove(self.rect)
                self.kill()

    def smena(self, veapon, oboyma_0, oboyma_1, oboyma_2, bullets_0, bullets_1, bullets_2, ideal_oboyma_0,
              ideal_oboyma_1, ideal_oboyma_2):
        if veapon == 0:
            if oboyma_0 > 0:
                oboyma_0 -= 1
            else:
                bullets_0 -= ideal_oboyma_0
                oboyma_0 += ideal_oboyma_0
                # music
        if veapon == 1:
            if oboyma_1 > 0:
                oboyma_1 -= 1
            else:
                bullets_1 -= ideal_oboyma_1
                oboyma_1 += ideal_oboyma_1
        if veapon == 2:
            if oboyma_2 > 0:
                oboyma_2 -= 1
            else:
                bullets_2 -= ideal_oboyma_2
                oboyma_2 += ideal_oboyma_2


'''
        
    '''
