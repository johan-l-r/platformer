import pygame as pg 

from data import read
from player import Player

pg.init()

class Game: 
  def __init__(self): 
    self.running = False

    self.player = Player()

    self.window = pg.display.set_mode((
      read("window_size"), 
      read("window_size")
    ))

    self.clock = pg.time.Clock()

  def run(self): 
    self.running = True

    while self.running: 
      for event in pg.event.get(): 
        if event.type == pg.QUIT: 
          self.running = False

        self.player.handle_event(event)

      delta = self.clock.tick(60) / 1000.0 

      self.window.fill((8, 8, 8)) 

      self.player.move(delta)

      self.player.draw(self.window)

      pg.display.flip()
