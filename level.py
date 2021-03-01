import json

import pygame

from car import Car

class Level:

    def __init__(self, name = ''):
        self.cars       = []
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

        serialised['cars'] = cars

        return serialised

    def save_to_json(self):
        #print(self.cars[0].__dict__())
        return json.dumps(vars(self), indent = 4)

    def load_from_json(self, source):
        input    = open(source, 'r')
        raw_data = input.read()
        json_data     = json.loads(raw_data)

        self.name       = json_data['name']
        self.best_score = json_data['best score']

        for car in json_data['cars']:
            self.cars.append(Car(car['name'],
                                (car['x'], car['y']),
                                car['image'],
                                car['state']))

        return self
