import pygame

def changColor(image, color):
    colouredImage = pygame.Surface(image.get_size())
    colouredImage.fill(color)

    finalImage = image.copy()
    finalImage.blit(colouredImage, (0, 0), special_flags = pygame.BLEND_MULT)
    return finalImage

class Stars:

    hollow_star_image = pygame.image.load('hollow_star.png')
    filled_star_image = pygame.image.load('filled_star.png')

    def __init__(self, score):
        self.score = score


    def draw(self, surface, rect):

        if (self.score >= 1):
            surface.blit(changColor(Stars.filled_star_image, (0, 255, 0)), [rect[0]     , rect[1] + 20])
        else:
            surface.blit(Stars.hollow_star_image, [rect[0]     , rect[1] + 20])

        if (self.score >= 2):
            surface.blit(Stars.filled_star_image, [rect[0] + 55, rect[1] + 20])
        else:
            surface.blit(Stars.hollow_star_image, [rect[0] + 55, rect[1] + 20])

        if (self.score >= 3):
            surface.blit(Stars.filled_star_image, [rect[0] + 28, rect[1]     ])
        else:
            surface.blit(Stars.hollow_star_image, [rect[0] + 28, rect[1]     ])


        #pygame.draw.rect(surface, (0, 255, 0), rect, 20, 25)
