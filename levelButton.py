import pygame

from stars import Stars

class LevelButton:

    rect_image = pygame.image.load('rect_image.png')

    def __init__(self, position, size, number):
        self.x    = position[0]
        self.y    = position[1]
        self.size = size

        self.number_image = pygame.image.load(str(number) + '.png')

        self.star = Stars(3)

        self.fullness               = 1
        self.is_focussed            = False
        self.time_when_get_focussed = None


    def draw(self, surface):
        #   pygame.draw.rect(surface, (240, 143, 40), [self.x, self.y, self.size, self.size], fill, 44)

        if self.fullness >= 2:
            self.fullness -= 1

        if self.time_when_get_focussed:
            self.fullness = (pygame.time.get_ticks() - self.time_when_get_focussed) // 2

        if self.fullness >= self.size // 2:
            self.fullness = self.size // 2

        pygame.draw.rect(surface, (240, 143, 40), [self.x, self.y, self.size, self.size], self.fullness, 44)

        surface.blit(LevelButton.rect_image, [self.x, self.y, self.size, self.size])
        surface.blit(self.number_image, [self.x + 58, self.y + 15])

        self.star.draw(surface, [self.x + 30, self.y + 85, 88, 55])


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
