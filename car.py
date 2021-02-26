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


    def click(self, click_pos):
        x = click_pos[0]
        y = click_pos[1]

        rect = self.image.get_rect()
        if rect.collidepoint([x, y]):
            return True

        return False


    def draw(self, surface):
        surface.blit(self.image, [self.x, self.y])


    @property
    def __dict__(self):
        serialised = {}

        serialised['name']   = self.name
        serialised['x']      = self.x
        serialised['y']      = self.y
        serialised['length'] = self.length
        serialised['state']  = int(self.state)

        return serialised
