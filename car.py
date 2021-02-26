import pygame

import colors

class Car:

    def __init__(self, name, position, image, state):
        self.name   = name
        self.x      = position[0]
        self.y      = position[1]
        self.state  = state
        self.image  = image

        if state == "H":
            self.image = pygame.transform.rotozoom(self.image, 90, 1)

    def rect(self):
        width, height = self.image.get_width(), self.image.get_height()
        return pygame.Rect(self.x, self.y, width, height)

    def click(self, click_pos):
        x, y = click_pos

        if self.rect().collidepoint([x, y]):
            return True

        return False


    def draw(self, surface):
        surface.blit(self.image, [self.x, self.y])
        pygame.draw.rect(surface, (255, 0, 0), self.rect(), 1)


    @property
    def __dict__(self):
        serialised = {}

        serialised['name']   = self.name
        serialised['x']      = self.x
        serialised['y']      = self.y
        serialised['length'] = self.length
        serialised['state']  = int(self.state)

        return serialised
