import pygame
from levelButton import LevelButton

pygame.init()

size = [1280, 720]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Парковка')

clock = pygame.time.Clock()

text = pygame.image.load('text.png') #.convert()

text_rect = text.get_rect(centerx = screen.get_rect().centerx,
                          y = 0.03*size[1])

button = LevelButton([50, 150], 150, 1)

clock.tick(60)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEMOTION:
            button.focus(event.pos)

        if event.type == pygame.MOUSEBUTTONDOWN:
            button.click(event.pos)

    screen.fill((40, 35, 56))

    screen.blit(text, text_rect )

    button.draw(screen)

    pygame.time.wait(5)

    pygame.display.update()
