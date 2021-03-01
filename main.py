import pygame

from levelButton import LevelButton
from levelSelectionUI import LevelSelectionUI
from gameFieldUI import GameFieldUI
import colors
from level import Level
from sound import Sound

pygame.init()

size = [450, 800]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Парковка')

clock = pygame.time.Clock()

clock.tick(300)

level_selection_UI = LevelSelectionUI()
game_field_UI      = None

Sound.toggle_music()

finished_levels = {}

level_number = None
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

               if result == 'sound':
                   Sound.sound_on = not Sound.sound_on
                   Sound.toggle_music()

               if result == 'win':
                   finished_levels[level_number] = True
                   level_selection_UI.level_buttons[level_number - 1].star.score = 3

           else:
               level_selection_UI.mouse_event(event)

               level_number = level_selection_UI.mouse_event(event)
               if level_number :
                   #try:
                   game_field_UI = GameFieldUI(Level().load_from_json('resources/levels/level ' + str(level_number) + '.json'))
                   #except FileNotFoundError:

    if game_field_UI:
        game_field_UI.draw(screen)
    else:
        level_selection_UI.draw(screen)

    pygame.display.update()
