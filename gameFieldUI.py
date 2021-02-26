import pygame
from textLabel import TextLabel
from bigStars import BigStars
import colors

class GameFieldUI:

    button_back = pygame.image.load('resources\\images\\left_arrow.png')
    sound = pygame.image.load('resources\\images\\sound.png')

    def __init__(self):
        self.current_level = TextLabel([97 , 14], [256, 60], "Уровень 1")
        self.best_score    = TextLabel([97 , 200], [256, 60], "Лучший счет")
        self.steps         = TextLabel([97 , 280], [256, 60], "Шаги")
        self.big_stars     = BigStars(0)

    def draw(self, surface):
        surface.fill(colors.DARK_BLUE)
        self.current_level.draw(surface)
        self.best_score.draw(surface)
        self.steps.draw(surface)
        surface.blit(GameFieldUI.button_back, [10 , 14,  78, 60])
        surface.blit(GameFieldUI.sound      , [362, 14, 78 , 60])
        self.big_stars.draw(surface, [150, 92, 150, 93])
