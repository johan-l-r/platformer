import pygame as pg

import data

pg.init()

class Player: 
  def __init__(self): 
    self.SIZE: int = 64

    self.x = 0
    self.y = data.read("window_size") - self.SIZE

    self.direction = [0, 0]

    self.movement_speed = 400

    self.bounds = pg.Rect(
      self.x, 
      self.y, 
      self.SIZE, 
      self.SIZE
    )

  def handle_event(self, event: pg.Event): 
    if event.type == pg.KEYDOWN: 
      if event.key == pg.K_d: 
        self.direction[0] = 1 
      if event.key == pg.K_a: 
        self.direction[0] = -1 
      if event.key == pg.K_w: 
        self.direction[1] = -1

    if event.type == pg.KEYUP:
      self.direction[0] = 0

  def move(self, delta: float):
    self.x += self.movement_speed * self.direction[0] * delta    
    self.y += self.movement_speed * self.direction[1] * delta    

    self.bounds.x = self.x
    self.bounds.y = self.y

  def draw(self, master: pg.Surface): 
    pg.draw.rect(master, (189, 189, 189), self.bounds)
