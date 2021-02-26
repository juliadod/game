import pygame
import colors

class TextLabel:

    font = pygame.font.SysFont('Roboto', 40)
    long_rect = pygame.image.load('resources\\images\\long_rect.png')

    def __init__(self, position, size, text):
        self.x    = position[0]
        self.y    = position[1]
        self.size = size
        self.text = text
        self.text_image = TextLabel.font.render(str(text), 1, colors.ORANGE)

    def draw(self, surface):
        surface.blit(TextLabel.long_rect, [self.x, self.y, self.size[0], self.size[1]])
        surface.blit(self.text_image, self.text_image.get_rect(center = [self.x + self.size[0]//2,
                                                                   self.y + self.size[1]//2]))
