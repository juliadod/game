import pygame
import colors

class GameField:

    def __init__(self, position, size):
        self.x    = position[0]
        self.y    = position[1]
        self.size = size
        self.field_tile_image = pygame.image.load('resources/images/field_tile.png')

    def draw(self, surface):

        for row in range(0, 6):
            for column in range(0, 6):
                surface.blit(self.field_tile_image, [self.x + column * 66, self.y + row * 66])
