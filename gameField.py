import pygame
import colors
from level import Level

class GameField:

    def __init__(self, position, size, level):
        self.x    = position[0]
        self.y    = position[1]
        self.size = size
        self.field_tile_image = pygame.image.load('resources/images/field_tile.png')

        self.level = level

        for car in self.level.cars:
            car.x = self.x + car.x * 66
            car.y = self.y + car.y * 66

    def draw(self, surface):

        for row in range(0, 6):
            for column in range(0, 6):
                surface.blit(self.field_tile_image, [self.x + column * 66, self.y + row * 66])

        for car in self.level.cars:
            car.draw(surface)
