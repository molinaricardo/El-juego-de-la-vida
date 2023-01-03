import pygame
from cell import Cell

WIDHT = 120
HEIGHT = 80

pygame.init()

surface = pygame.display.set_mode((WIDHT, HEIGHT))
pygame.display.set_caption('game of the live')

cells = list()
cells.append(Cell(50, 50, 0, 0))

sprites = pygame.sprite.Group()
sprites.add(cells)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            sys.exit()
    
    pygame.display.update()