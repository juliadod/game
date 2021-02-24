import pygame

class Stars:

    hollow_star_image = pygame.image.load('hollow_star.png')
    filled_star_image = pygame.image.load('filled_star.png')

    def __init__(self, score):
        self.score = score


    def draw(self, surface, rect):
        surface.blit(Stars.hollow_star_image, [rect[0] + 28, rect[1]     ])
        surface.blit(Stars.hollow_star_image, [rect[0]     , rect[1] + 20])
        surface.blit(Stars.hollow_star_image, [rect[0] + 55, rect[1] + 20])

        #pygame.draw.rect(surface, (0, 255, 0), rect, 2)
