import pygame as pg 

from data import read
from player import Player
from tilemap import TileMap

pg.init()

class Game: 
  def __init__(self): 
    self.running: bool = False

    self.tilemap = TileMap("./level.txt")
    self.player = Player(self.tilemap.player_spawn[0], self.tilemap.player_spawn[1])

    self.window: pg.Surface = pg.display.set_mode((
      read("window_size"), 
      read("window_size")
    ))

    self.clock: pg.Clock = pg.time.Clock()

  def update(self, delta): 
    self.player.update(delta)

  def draw(self): 
    self.tilemap.draw_tilemap(self.window)
    self.player.draw(self.window)

  def run(self): 
    self.running = True

    while self.running: 
      for event in pg.event.get(): 
        if event.type == pg.QUIT: 
          self.running = False

      delta = self.clock.tick(60) / 1000.0 

      self.window.fill((8, 8, 8)) 

      self.update(delta)

      self.draw()

      pg.display.flip()
