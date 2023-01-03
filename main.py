import pygame

WIDHT = 1200
HEIGHT = 800

surface = pygame.display.set_model((WIDHT, HEIGHT))
pygame.display.set_caption('game of the live')

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            sys.exit()
    pygame.display.update()