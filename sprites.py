import pygame as pg
from settings import *


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__(self.groups)
        self.game = game
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE


class WhitePlayer(Player):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.white_players
        super().__init__(game, x, y)
        self.init_image()

    def init_image(self):
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()


class BlackPlayer(Player):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.black_players
        super().__init__(game, x, y)
        self.init_image()

    def init_image(self):
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
