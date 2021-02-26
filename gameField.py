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

        self.active_car = None

    def rect(self):
        return pygame.Rect([self.x, self.y, self.size, self.size])

    def mouse_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for car in self.level.cars:
                if car.click(event.pos):
                    self.active_car = car

        if event.type == pygame.MOUSEBUTTONUP:
            self.active_car = None

        if event.type == pygame.MOUSEMOTION \
           and self.active_car != None:
           if self.active_car.state == "H":
                self.active_car.x += event.rel[0]

                for car in self.level.cars:
                    if self.active_car != car:
                        if self.active_car.rect().colliderect(car.rect()) or \
                          not self.rect().contains(self.active_car.rect()):
                            self.active_car.x -= event.rel[0]

           else:
                self.active_car.y += event.rel[1]

                for car in self.level.cars:
                    if self.active_car != car:
                        if self.active_car.rect().colliderect(car.rect()) or \
                           not self.rect().contains(self.active_car.rect()):
                            self.active_car.y -= event.rel[1]



    def draw(self, surface):

        for row in range(0, 6):
            for column in range(0, 6):
                surface.blit(self.field_tile_image, [self.x + column * 66, self.y + row * 66])

        for car in self.level.cars:
            car.draw(surface)
