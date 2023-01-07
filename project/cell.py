import pygame

LIVE = (255, 255, 255)
DEATH = (0, 0, 0)

def generate_cells(width_screen, height_screen, width):
    cells = list()

    for pos_x in range(0, width_screen // width_cell):
        rows = list()
        for pos_y in range(0, height_screen // height_cell):
            rows.append(Cell(width_cell, height_cell, pos_x, pos_y))

        columns.append(rows)
    
    return columns 

class Cell(pygame.sprite.Sprite):

    def __init__(self, width, height, pos_x, pox_y):
        pygame.sprite.Sprite.__init__(self)

        self.width = width
        self.height = height

        self.pos_x = pos_x
        self.pos_y = pox_y

        self.update_rect()

    def update_rect(self):
        self.rect = self.get_rect()

        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

    def get_rect(self):
        self.image = pygame.Surface((self.width, self.height))

        self.image.fill(LIVE)

        return self.image.get_rect()