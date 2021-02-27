import pygame

from car import Car


class Level:

    def __init__(self, name = ''):
        self.cars       = []
        self.obstacles  = []
        self.name       = name
        self.best_score = 0

    @property
    def __dict__(self):
        serialised = {}

        serialised['name']       = self.name
        serialised['best score'] = self.best_score

        cars = []
        for car in self.cars:
            cars.append(vars(car))

        serialised['cars']       = cars
        serialised['obstacles']  = self.obstacles

        return serialised


    def loadFromDict(source):
        level = Level()

        level.name       = source['name']
        level.best_score = source['best score']

        for car in source['cars']:
            level.cars.append(Car(car['name'],
                                  (car['x'], car['y']),
                                  pygame.image.load(car['image']),
                                  car['state']))

        for obstacle in source['obstacles']:
            level.cars.append(Car(obstacle['name'],
                                  (obstacle['x'], obstacle['y']),
                                  pygame.image.load(obstacle['image']),
                                  obstacle['state']))
        return level
