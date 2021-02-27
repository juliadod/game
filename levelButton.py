import pygame

from stars import Stars
import colors

pygame.init()

class LevelButton:

    rect_image = pygame.image.load('resources/images/rect.png')

    font = pygame.font.SysFont('Roboto', 70)

    def __init__(self, position, size, number):
        self.x    = position[0]
        self.y    = position[1]
        self.size = size
        self.number = number
        self.number_image = LevelButton.font.render(str(number), 1, colors.ORANGE)

        self.star = Stars(0)

        self.fullness               = 1
        self.is_focussed            = False
        self.time_when_get_focussed = None



    def draw(self, surface):

        #   pygame.draw.rect(surface, colors.ORANGE, [self.x, self.y, self.size, self.size], fill, 44)

        if self.fullness >= 2:
            self.fullness -= 1

        if self.time_when_get_focussed:
            self.fullness = (pygame.time.get_ticks() - self.time_when_get_focussed) // 1

        if self.fullness >= self.size // 2:
            self.fullness = self.size // 2

        pygame.draw.rect(surface, colors.ORANGE, [self.x, self.y, self.size, self.size], self.fullness, 44)

        surface.blit(LevelButton.rect_image, [self.x, self.y, self.size, self.size])

        surface.blit(self.number_image, self.number_image.get_rect(centerx = self.x + self.size // 2,
                                                                       y = self.y + self.size * 0.10))

        self.star.draw(surface, [self.x + 25, self.y + 84, 27, 27])

    def focus(self, mouse_pos):
        x = mouse_pos[0]
        y = mouse_pos[1]

        rect = pygame.Rect(self.x, self.y, self.size, self.size)

        if rect.collidepoint([x, y]):
            if not self.is_focussed:
                self.time_when_get_focussed = pygame.time.get_ticks()
                self.is_focussed            = True

            return True

        self.is_focussed            = False
        self.time_when_get_focussed = None
        return False


    def click(self, click_pos):
        x = click_pos[0]
        y = click_pos[1]

        rect = pygame.Rect(self.x, self.y, self.size, self.size)
        if rect.collidepoint([x, y]):
            return True

        return False
