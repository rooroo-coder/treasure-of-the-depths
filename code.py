import pygame
import sys


pygame.init()


width, height = 700, 700
rows, cols = 30, 30  
cell_width = width // cols
cell_height = height // rows


window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Grid Window")


WHITE = (255, 255, 255)
GRAY = (200, 200, 200)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    window.fill(WHITE)

    
    for x in range(0, width, cell_width):
        pygame.draw.line(window, GRAY, (x, 0), (x, height))
    for y in range(0, height, cell_height):
        pygame.draw.line(window, GRAY, (0, y), (width, y))


    pygame.display.flip()


pygame.quit()
sys.exit()
