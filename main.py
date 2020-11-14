import pygame as pg
import sys
from os import path
from settings import *
from sprites import *


class Game:
    def __init__(self):
        # initialize pygame and create window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.running = True
        self.load_data()

    def load_data(self):
        self.load_map_data()

    def load_map_data(self):
        self.map_data = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.white_players = pg.sprite.Group()
        self.black_players = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == 'w':
                    WhitePlayer(self, col, row)
                if tile == 'b':
                    BlackPlayer(self, col, row)

    def run(self):
        # Game Loop
        self.playing = True

        while self.playing:
            # keep loop running at the right speed
            self.dt = self.clock.tick(FPS) / 1000

            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - update
        self.all_sprites.update()

    def events(self):
        # Game Loop - events
        # process input (events)
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if self.playing:
                        self.playing = False
                    self.running = False
                elif event.key == pg.K_LEFT:
                    self.player.move(dx=-1, dy=0)
                elif event.key == pg.K_RIGHT:
                    self.player.move(dx=1, dy=0)
                elif event.key == pg.K_UP:
                    self.player.move(dx=0, dy=-1)
                elif event.key == pg.K_DOWN:
                    self.player.move(dx=0, dy=1)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, DARKGREY, (x, 0), (x, HEIGHT))

        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, DARKGREY, (0, y), (WIDTH, y))

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def quit(self):
        pg.quit()
        sys.exit()

    def show_start_screen(self):
        # game splash / start screen
        pass

    def show_gameover_screen(self):
        # game over / continue screen
        pass


g = Game()
g.show_start_screen()

while g.running:
    g.new()
    g.run()
    g.show_gameover_screen()

g.quit()
