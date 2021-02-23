import pygame
from levelButton import LevelButton
pygame.init()

size = [1280, 720]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Парковка")

clock = pygame.time.Clock()

text = pygame.image.load('text.png') #.convert()

text_rect = text.get_rect(centerx = screen.get_rect().centerx,
                          y = 0.03*size[1])

print(screen.get_rect().width)

button = LevelButton([50, 150], 150, 1)


done = False
while not done:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    screen.fill((40, 35, 56))

    screen.blit(text, text_rect )

    button.draw(screen)
    pygame.display.update()
