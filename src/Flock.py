import numpy as np
from Groid import Groid 

class Flock:
    def __init__(self, flock_size = 600, width=800, height=600, max_speed=2.0, delta=5, 
                 separation_range=20, separation_strength=1.5, 
                 alignment_range=40, alignment_strength=1.0, 
                 cohesion_range=50, cohesion_strength=1.2):

        self.width, self.height = width, height
        self.flock_size = flock_size
        self.max_speed = max_speed
        self.delta = delta
        self.separation_range = separation_range
        self.separation_strength = separation_strength
        self.alignment_range = alignment_range
        self.alignment_strength = alignment_strength
        self.cohesion_range = cohesion_range
        self.cohesion_strength = cohesion_strength

        self.flock = []  

        for _ in range(flock_size):
            position = np.array([np.random.uniform(0, width), np.random.uniform(0, height)])
            velocity = np.array([np.random.uniform(-1, 1), np.random.uniform(-1, 1)])
            groid = Groid(position, velocity, self) 
            self.flock.append(groid)  

    def update(self):
        for groid in self.flock:
            groid.update()