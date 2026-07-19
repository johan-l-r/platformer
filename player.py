import pygame as pg

import data

pg.init()

class Player: 
  def __init__(self, x, y): 
    self.SIZE: int = 32

    self.position = pg.math.Vector2(x, y)
    self.velocity = pg.math.Vector2(0, 0)
    self.acceleration = pg.math.Vector2(0, 0)

    self.HORIZONTAL_VELOCITY = 6
    self.HORIZONTAL_FRICTION = 0.25

    self.bounds = pg.Rect(x, y, self.SIZE, self.SIZE)
    self.bounds.topleft = (x, y)

  def handle_event(self, event: pg.Event): 
    pass

  def move(self, delta: float, key):
    self.acceleration = pg.math.Vector2(0, 0)
    if key[pg.K_a]: 
      self.acceleration.x = -1 * self.HORIZONTAL_VELOCITY
    if key[pg.K_d]: 
      self.acceleration.x = self.HORIZONTAL_VELOCITY

    self.acceleration.x -= self.velocity.x * self.HORIZONTAL_FRICTION
    self.velocity += self.acceleration
    self.position += self.velocity + 0.5 * self.acceleration

    self.bounds.topleft = self.position

  def jump(self, delta): 
    pass

  def update(self, delta): 
    keys = pg.key.get_pressed()

    self.move(delta, keys)
    self.jump(delta)

  def draw(self, master: pg.Surface): 
    pg.draw.rect(master, (189, 189, 189), self.bounds)
