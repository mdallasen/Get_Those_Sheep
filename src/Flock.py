import numpy as np
from Groid import Groid 
from Herder import Herder

class Flock:
    def __init__(self, flock_size, herder_size, 
                 width, height, max_speed, delta, 
                 separation_range, separation_strength, 
                 alignment_range, alignment_strength, 
                 cohesion_range, cohesion_strength, 
                 groid_to_herder_distance, separation_range_herders, 
                 max_speed_herders, separation_strength_herder):

        self.width, self.height = width, height
        self.flock_size = flock_size
        self.herder_size = herder_size
        self.max_speed = max_speed
        self.delta = delta
        self.separation_range = separation_range
        self.separation_strength = separation_strength
        self.alignment_range = alignment_range
        self.alignment_strength = alignment_strength
        self.cohesion_range = cohesion_range
        self.cohesion_strength = cohesion_strength
        self.groid_to_herder_distance = groid_to_herder_distance
        self.separation_range_herders = separation_range_herders
        self.max_speed_herders = max_speed_herders
        self.separation_strength_herder = separation_strength_herder 

        self.flock = []  
        self.herders = []

        for _ in range(flock_size):
            position = np.array([np.random.uniform(0, width), np.random.uniform(0, height)])
            velocity = np.array([np.random.uniform(-1, 1), np.random.uniform(-1, 1)])
            groid = Groid(position, velocity, self)
            self.flock.append(groid)

        for _ in range(herder_size):
            position = np.array([np.random.uniform(0, width), np.random.uniform(0, height)])
            velocity = np.array([np.random.uniform(-1, 1), np.random.uniform(-1, 1)])
            herder = Herder(position, velocity, self)
            self.herders.append(herder) 

    def update(self):
        for groid in self.flock:
            groid.update()
        
        for herder in self.herders: 
            herder.update()