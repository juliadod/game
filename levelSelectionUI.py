import pygame

from levelButton import LevelButton
from stars import Stars
import colors

class LevelSelectionUI:

    def __init__(self):
        font = pygame.font.SysFont('constan', 45)
        self.text_image = font.render('Выберите уровень', True, colors.ORANGE)
        self.car_image = pygame.image.load('resources/images/car.png')

        self.level_buttons = []

        level_number = 1
        for row in range(0, 4):
            for column in range(0, 3):
                self.level_buttons.append(LevelButton([25 + 140 * column, 134 + 140 * row], 120, level_number))
                level_number += 1

    def mouse_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            for button in self.level_buttons:
                button.focus(event.pos)

        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.level_buttons:
                if(button.click(event.pos)):
                    return button.number

        return None

    def draw(self, surface):
        surface.fill(colors.DARK_BLUE)

        surface.blit(self.car_image, (self.car_image.get_rect(centerx = surface.get_rect().centerx,
                                                              bottom = surface.get_rect().bottom )))

        surface.blit(self.text_image, self.text_image.get_rect(centerx = surface.get_rect().centerx,
                                                     y = 0.03*surface.get_height()))

        for button in self.level_buttons:
            button.draw(surface)
