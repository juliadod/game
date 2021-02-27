import pygame
import json

from levelButton import LevelButton
from levelSelectionUI import LevelSelectionUI
from gameFieldUI import GameFieldUI
import colors
from level import Level

def load_level(level_name):
    input    = open('resources/levels/' + level_name + '.json', 'r')
    raw_data = input.read()
    data     = json.loads(raw_data)
    level    = Level.loadFromDict(data)
    return level

pygame.init()

size = [450, 800]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Парковка')

clock = pygame.time.Clock()

clock.tick(300)

level_selection_UI = LevelSelectionUI()
game_field_UI      = None

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEMOTION or \
           event.type == pygame.MOUSEBUTTONDOWN or \
           event.type == pygame.MOUSEBUTTONUP:
           if game_field_UI:
               result = game_field_UI.mouse_event(event)
               if result == 'exit':
                   game_field_UI = None
           else:
               level_selection_UI.mouse_event(event)

           level_number = level_selection_UI.mouse_event(event)
           if level_number:
               try:
                   game_field_UI = GameFieldUI(load_level('level ' + str(level_number)))
               except FileNotFoundError:
                   pass


    if game_field_UI:
        game_field_UI.draw(screen)
    else:
        level_selection_UI.draw(screen)

    pygame.display.update()
