import pygame as pg

from data import read

pg.init()

class Tile: 
  def __init__(
    self,
    x: int,
    y: int, 
    color: tuple[int, int, int] = (8, 8, 8)
  ):
    self.SIZE = read("tile_size")

    self.x: int = x
    self.y: int = y

    self.color = color

    self.bounds: pg.Rect = pg.Rect(self.x, self.y, self.SIZE, self.SIZE)

  def draw(self, master: pg.Surface): 
    pg.draw.rect(master, self.color, self.bounds)
