import pygame
from levelButton import LevelButton
from levelSelectionUI import LevelSelectionUI
from gameFieldUI import GameFieldUI
import colors

pygame.init()

size = [900, 800]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Парковка')

clock = pygame.time.Clock()

clock.tick(60)

level_selection_UI = LevelSelectionUI()
game_field_UI = GameFieldUI()

surface1 = pygame.Surface([450, 800])
surface2 = pygame.Surface([450, 800])

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEMOTION or \
           event.type == pygame.MOUSEBUTTONDOWN:
           level_selection_UI.mouse_event(event)

    level_selection_UI.draw(surface1)
    game_field_UI.draw(surface2)

    screen.blit(surface1, [0, 0])
    screen.blit(surface2, [450, 0])

    pygame.time.wait(5)

    pygame.display.update()
