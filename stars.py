import pygame

class Stars:

    hollow_star_image = pygame.image.load('hollow_star.png')
    filled_star_image = pygame.image.load('filled_star.png')

    def __init__(self, score):
        self.score = score


    def draw(self, surface, rect):

        if (self.score >= 1):
            surface.blit(changColor(Stars.filled_star_image, (0, 255, 0)), [rect[0], rect[1]])
        else:
            surface.blit(Stars.hollow_star_image, [rect[0], rect[1]])

        if (self.score >= 2):
            surface.blit(Stars.filled_star_image, [rect[0] + 23, rect[1] - 20])
        else:
            surface.blit(Stars.hollow_star_image, [rect[0] + 23, rect[1] - 20])

        if (self.score >= 3):
            surface.blit(Stars.filled_star_image, [rect[0] + 43, rect[1]] )
        else:
            surface.blit(Stars.hollow_star_image, [rect[0] + 43, rect[1]] )


        #pygame.draw.rect(surface, (0, 255, 0), rect, 20, 25)
