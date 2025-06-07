import Main
import pygame

pygame.init()

class Tile:
    X, Y = 0, 0
    img = 0
    overlay = "none"

    def __init__(self, X, Y, img):
        self.X = X
        self.Y = Y
        self.img = img

    def getPixelX(self):
        return ((self.X - Main.playerX) * Main.cell_size) + Main.offsetX

    def getPixelY(self):
        return ((self.Y - Main.playerY) * Main.cell_size) + Main.offsetY

    def draw(self):
        Main.window.blit(self.img, (Tile.getPixelX(self.X), Tile.getPixelY(self.Y)))