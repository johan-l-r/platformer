import pygame as pg

from data import read
from tile import Tile

pg.init()

class TileMap: 
  def __init__(self, file_path: str): 
    self.file_path: str = file_path

    self.TILE_SIZE: int = read("tile_size")

    self.player_spawn = ()

    self.start_x: int = 0
    self.start_y: int = 0

    self.tilemap = self.load_tiles()

  def draw_tilemap(self, master: pg.Surface): 
    for tile in self.tilemap: 
      tile.draw(master)

  def read_file(self): 
    with open(self.file_path, "r") as file: 
      content: str = file.read()

    tilemap: list[list[str]] = []

    # get list of lines 
    file_lines: list[str] = content.splitlines()

    for line in file_lines: 
      # remove whitespaces and str into list of chars 
      chars: list[str] = list(line.replace(" ", ""))

      row: list[str] = []

      for char in chars: 
        row.append(char)

      tilemap.append(row)

    print(tilemap)
    return tilemap

  def load_tiles(self): 
    tiles = []

    x, y = 0, 0

    tilemap: list[list[str]] = self.read_file()

    for row in tilemap: 
      x = 0

      for tile in row: 
        if tile == "0": 
          self.start_x, self.start_y = x * self.TILE_SIZE, y * self.TILE_SIZE
        elif tile == "1": 
          tiles.append(Tile(x * self.TILE_SIZE, y * self.TILE_SIZE, (189, 189, 189)))
        elif tile == "2": 
          self.player_spawn = (
            x * self.TILE_SIZE, 
            y * self.TILE_SIZE
          )

        x += 1
      y += 1

    return tiles
