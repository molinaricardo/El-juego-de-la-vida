import pygame

class Cell(pygame.sprite.Sprite):

    def __init__(self, width, height, pos_x, pox_y):
        pygame.sprite.Sprite.__init__(self)

        self.width = width
        self.height = height

        self.pos_x = pos_x
        self.pos_y = pox_y

