import pygame
from textLabel import TextLabel
from bigStars import BigStars
import colors
from gameField import GameField

class GameFieldUI:
    button_back_image = pygame.image.load('resources/images/left_arrow.png')
    sound_image = pygame.image.load('resources/images/sound.png')
    #level_number = level_selection_UI.mouse_event(event)

    def __init__(self, level):
        self.current_level = TextLabel([97 , 14], [256, 60] , str(level.name))  # +  str(level_number))
        self.best_score    = TextLabel([97 , 200], [256, 60], 'Лучший счет')
        self.steps         = TextLabel([97 , 280], [256, 60], 'Шаги')
        self.big_stars     = BigStars(0)
        self.game_field    = GameField((28, 378), 394, level)
        self.score         = 0


    def mouse_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.Rect([10 , 14,  78, 60]).collidepoint(event.pos):
                # нажата кнопка назад
                return 'exit'

            if pygame.Rect([362, 14,  78, 60]).collidepoint(event.pos):
                # нажата кнопка звука
                return 'sound'

        result = self.game_field.mouse_event(event)

        if result == 'win':
            self.big_stars.score = 3
            return 'win'

        if result:
            self.score += 1
            self.steps.set_text('Шаги ' + str(self.score))


    def draw(self, surface):
        surface.fill(colors.DARK_BLUE)

        self.current_level.draw(surface)
        self.best_score.draw(surface)
        self.steps.draw(surface)

        surface.blit(GameFieldUI.button_back_image, [10 , 14,  78, 60])
        surface.blit(GameFieldUI.sound_image      , [362, 14,  78, 60])

        self.big_stars.draw(surface, [150, 92, 150, 93])

        self.game_field.draw(surface)
