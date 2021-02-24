import pygame

from stars import Stars

class LevelButton:

    rect_image = pygame.image.load('rect_image.png')

    def __init__(self, position, size, number):
        self.x    = position[0]
        self.y    = position[1]
        self.size = size

        self.number_image = pygame.image.load(str(number) + '.png')

        self.star = Stars(0)


    def draw(self, surface):

        surface.blit(LevelButton.rect_image, [self.x, self.y, self.size, self.size])
        surface.blit(self.number_image, [self.x + 58, self.y + 15])

        self.star.draw(surface, [self.x + 30, self.y + 85, 88, 55])
