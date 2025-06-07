import pygame
import sys
from tile import Tile

pygame.init()

width, height = 700, 700
rows, cols = 30, 30
cell_size = 40
def loadImage(S):
    pygame.transform.scale(pygame.image.load(S), (cell_size,cell_size))
tileTypes = [loadImage('sprites/floor.png'), loadImage('sprites/wall.png')]
grid = [[Tile(tileTypes[0], x, y) for x in range(rows)] for y in range(cols)]

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Treasure of The Depths")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for ypos in range(0, cols):
        for xpos in range(0, rows):
            grid[xpos][ypos].draw()

    pygame.display.flip()


pygame.quit()
sys.exit()
