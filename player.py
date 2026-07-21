import pygame as pg

import data

pg.init()

class Player: 
  def __init__(self, x, y): 
    self.SIZE: int = 32

    # horizontal movement constants
    self.HORIZONTAL_ACCELERATION: int = 60 # limit 
    self.HORIZONTAL_FRICTION: float = 8

    # vertical movement constants
    self.GRAVITY: float = 10

    self.position: pg.math.Vector2 = pg.math.Vector2(x, y)
    self.velocity: pg.math.Vector2 = pg.math.Vector2(0, 0)
    self.acceleration: pg.math.Vector2 = pg.math.Vector2(0, 0)

    self.bounds: pg.Rect = pg.Rect(x, y, self.SIZE, self.SIZE)

    self.bounds.bottomleft = (x, y)

  def move(self, delta: float, key):
    # gravity is always pushing down
    self.acceleration = pg.math.Vector2(0, self.GRAVITY)

    if key[pg.K_a]: 
      self.acceleration.x = -1 * self.HORIZONTAL_ACCELERATION
    if key[pg.K_d]: 
      self.acceleration.x = self.HORIZONTAL_ACCELERATION

    self.acceleration.x -= self.velocity.x * self.HORIZONTAL_FRICTION
    self.velocity += self.acceleration * delta 
    self.position += self.velocity + 0.5 * self.acceleration * delta

    self.bounds.bottomleft = self.position

  def jump(self, delta): 
    pass

  def update(self, delta): 
    keys = pg.key.get_pressed()

    self.move(delta, keys)
    self.jump(delta)

  def draw(self, master: pg.Surface): 
    pg.draw.rect(master, (189, 189, 189), self.bounds)
