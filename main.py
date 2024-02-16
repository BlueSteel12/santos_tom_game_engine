# This file was created by: Tomas Santos
# Import libraries 
import pygame as pg
from settings import *
from sprites import *
import sys
from random import randint
from os import path

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
        pg.key.set_repeat(500, 100)
        self.running = True
        self.load_data()
        #Running the game
        #later on we'll store game into with this
    def load_data(self):
        game_folder = path.dirname(__file__)
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
                print(self.map_data)
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.bigger = pg.sprite.Group()
        # self.player = Player(self, 10, 10)
        # self.all_spritres.add(self.player)
        #  for x in range(10, 20):
        #     Wall(self x, 5)
        for row, tiles in enumerate(self.map_data):
            print(row)
            for col, tile in enumerate(tiles):
                print(col)
                if tile == 'x':
                    print("a wall at", row, col)
                    Wall(self, col, row)
                if tile == 'p':
                    self.player = Player(self, col, row)
                if tile == '*':
                    Bigger(self, col, row)
    
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
    def input(self):
        pass 
    #print(self.clock.get_fps())

    # new motion

    # UPDATE THE UPDATE
    def update(self):
        self.all_sprites.update()
        
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
        pg.display.flip()
    
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
    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass
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

