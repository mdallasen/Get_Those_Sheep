import numpy as np

class Herder: 
    def __init__(self, position, velocity, flock):

        self.position = position
        self.velocity = velocity 
        self.flock = flock
        self.separation_range = flock.separation_range_herders
        self.herders = flock.herders
        self.max_speed = flock.max_speed_herders
        self.delta = flock.delta
        self.acceleration = np.array([0.0, 0.0], dtype=float)
        self.separation_strength_herder = flock.separation_strength_herder

    def update(self):
        """
        Updates the position of the Groid based on flocking behaviors.
        """
        separation = self.separation()

        self.acceleration = separation
        self.velocity += self.acceleration * self.delta 
        velocity_norm = np.linalg.norm(self.velocity)

        if velocity_norm > self.max_speed: 
            self.velocity = (self.velocity / velocity_norm) * self.max_speed
        
        self.position += self.velocity * self.delta
        self.enforce_boundaries(self.flock.width, self.flock.height) 

    def separation(self):
        """ 
        Steer away from nearby Herders.
        """
        neighborhood = 0
        direction = np.array([0.0, 0.0])

        for neighbour in self.flock.herders: 
            if neighbour is not self: 
                distance = np.linalg.norm(self.position - neighbour.position)
                
                if 0 < distance < self.separation_range:
                    difference = (self.position - neighbour.position) / distance
                    direction += difference
                    neighborhood += 1 
                    
        if neighborhood > 0: 
            direction /= neighborhood
            norm = np.linalg.norm(direction)
            if norm > 0: 
                direction = (direction / norm) * self.separation_strength_herder

        return direction
    
    def enforce_boundaries(self, width, height):
        """
        Wrap around boundaries or contain movement within limits.
        """
        if self.position[0] < 0: self.position[0] = width
        if self.position[0] > width: self.position[0] = 0
        if self.position[1] < 0: self.position[1] = height
        if self.position[1] > height: self.position[1] = 0

