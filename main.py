# This file was created by: Tomas Santos
# Import libraries 
import pygame as pg
from settings import *
from sprites import *
import sys
from random import randint
from os import path

from math import floor
'''
Game design truths:
goals, rules, feedback, freedom, what the verb, and will it form a sentence 

- Sound effects
- Changing enemies
- Teleportation
'''

class Cooldown():
    def __init__(self):
        self.current_time = 0
        self.event_time = 0
        self.delta = 0
    def ticking(self):
        self.current_time = floor((pg.time.get_ticks())/1000)
        self.delta = self.current_time - self.event_time
    def countdown(self, x):
        x = x - self.delta
        if x != None:
            return x
    def event_reset(self):
        self.event_time = floor((pg.time.get_ticks())/1000)
    def timer(self):
        self.current_time = floor((pg.time.get_ticks())/1000)

# Create a game class
class Game:
    # Define intalizing
    def __init__(self):
        pg.init()
        # Creating window
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        # Setting the name of the window to My First Video Game
        pg.display.set_caption("My First Video Game")
        # Setting the time
        # frames per seconds pretty much
        self.clock = pg.time.Clock()
        # pg.key.set_repeat(500, 100)
        # self.running = True
        self.load_data()
        #Running the game
        #later on we'll store game into with this
    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'images')
        self.player_img = pg.image.load(path.join(img_folder, 'Mario.png')).convert_alpha()
        self.map_data = []
        '''
        The with statement is a context manager in Python. 
        It is used to ensure that a resource is properly closed or released 
        after it is used. This can help to prevent errors and leaks.
        '''
        # create map from file
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                print(line)
                self.map_data.append(line)
                # print(self.map_data)
    def new(self):
        self.test_timer = Cooldown()
        print("create new game...")
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.bigger = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        self.power_ups = pg.sprite.Group()
        self.mob = pg.sprite.Group()
        self.teleport = pg.sprite.Group()
        self.pew_pews = pg.sprite.Group()
        # self.player = Player(self, 10, 10)
        # self.all_spritres.add(self.player)
        #  for x in range(10, 20):
        #     Wall(self x, 5)
        for row, tiles in enumerate(self.map_data):
            print(row)
            for col, tile in enumerate(tiles):
                print(col)
                if tile == '1':
                    print("a wall at", row, col)
                    Wall(self, col, row)
                if tile == 'p':
                    self.player = Player(self, col, row)
                    self.playercol = col
                    self.playerrow = row
                if tile == 'B':
                    Bigger(self, col, row)
                if tile == 'C':
                    Coin(self, col, row)
                if tile == 'U':
                    PowerUp(self, col, row)
                if tile == 'M':
                    Mob(self, col, row)
                if tile == 't':
                    Teleport(self, col, row)
    
    #Run methods, causes the game to work
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            #this is input
            self.events()
            #this is processing
            self.update()
            #this is output
            self.draw()    


    def quit(self):
        pg.quit()
        sys.exit()
    # method
    # def input(self):
        # pass 
    #print(self.clock.get_fps())

    # new motion

    # UPDATE THE UPDATE
    def update(self):
        self.all_sprites.update()
        self.test_timer.ticking()
        
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))
    
    # def draw_text(self, surface, text, size, color, x, y):
    #     font_name = pg.font.match_font('arial')
    #     font = pg.font.Font(font_name, size)
    #     text_surface = font.render(text, True, color)
    #     text_rect = text_surface.get_rect()
    #     text_rect.topleft = (x*TILESIZE,y*TILESIZE)
    #     surface.blit(text_surface, text_rect)

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.draw_text(self.screen, str(self.test_timer.countdown(45)), 24, WHITE, WIDTH/2 - 32, 2)
        pg.display.flip()
    
    def draw_text(self, surface, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x,y)
        surface.blit(text_surface, text_rect)
    

    
    #events, and checks if we clicked 'X'
    def events(self):
             # listening for events
             for event in pg.event.get():
                # when you hit the red x the window closes the game ends
                if event.type == pg.QUIT:
                    self.quit()
                    print("the game has ended...")
                # keyboard events
                # if event.type == pg.KEYDOWN:
                    # if event.key == pg.K_LEFT:
                        # self.player.move(dx=-1)
                # if event.type == pg.KEYDOWN:
                    # if event.key == pg.K_RIGHT:
                        # self.player.move(dx = 1)
                # if event.type == pg.KEYDOWN:
                    # if event.key == pg.K_UP:
                        # self.player.move(dy = -1)
                # if event.type == pg.KEYDOWN:
                    # if event.key == pg.K_DOWN:
                        # self.player.move(dx = 1)
    # def show_start_screen(self):
    #     pass
    # def show_go_screen(self):
    #     pass
# Assign Game to g
g = Game()
# g.show_g_screen()
while True:
    g.new()
    g.run()
    # g.show_go_screen()

# Questions:
# 1. What does line 18 specifically do?
# 2. What does "pass" mean?
# 3. What does line 25 do?

