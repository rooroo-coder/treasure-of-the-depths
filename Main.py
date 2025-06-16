import pygame
import sys

# Simple Tile class since it was imported in original
class Tile:
    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
    
    def draw(self):
        window.blit(self.sprite, self.rect)

pygame.init()

width, height = 700, 700
rows, cols = 30, 30
cell_size = 40

def loadImage(S):
    return pygame.transform.scale(pygame.image.load(S), (cell_size, cell_size))

tileTypes = [loadImage('sprites/floor.png'), loadImage('sprites/wall.png')]
grid = [[Tile(x, y, tileTypes[0]) for x in range(rows)] for y in range(cols)]
player_sprite = loadImage('sprites/player_sprite.png')

# Player position
player_x, player_y = 1, 1

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Treasure of The Depths")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Add basic movement
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and player_y > 0:
                player_y -= 1
            elif event.key == pygame.K_DOWN and player_y < cols - 1:
                player_y += 1
            elif event.key == pygame.K_LEFT and player_x > 0:
                player_x -= 1
            elif event.key == pygame.K_RIGHT and player_x < rows - 1:
                player_x += 1

    # Draw tiles
    for y in range(0, cols):
        for x in range(0, rows):
            grid[x][y].draw()
    
    # Draw player
    player_rect = pygame.Rect(player_x * cell_size, player_y * cell_size, cell_size, cell_size)
    window.blit(player_sprite, player_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()