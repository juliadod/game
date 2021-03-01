import pygame

import colors

class BigStars:

    big_hollow_star = pygame.image.load('resources/images/big_hollow_star.png')
    big_filled_star = pygame.image.load('resources/images/big_filled_star.png')

    def __init__(self, score):
        self.score = score


    def draw(self, surface, rect):
        if (self.score >= 1):
            surface.blit(BigStars.big_filled_star, [rect[0], rect[1] + 35])
        else:
            surface.blit(BigStars.big_hollow_star, [rect[0], rect[1] + 35])

        if (self.score >= 2):
            surface.blit(BigStars.big_filled_star, [rect[0] + 92, rect[1] + 35])
        else:
            surface.blit(BigStars.big_hollow_star, [rect[0] + 92, rect[1] + 35])

        if (self.score >= 3):
            surface.blit(BigStars.big_filled_star, [rect[0] + 46, rect[1]] )
        else:
            surface.blit(BigStars.big_hollow_star, [rect[0] + 46, rect[1]] )
