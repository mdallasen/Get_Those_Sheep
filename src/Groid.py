import numpy as np 
import pandas as pd 

class Memeber: 
    def __init__(self, position, velocity, flock, max_speed, delta, separation_range, separation_strength, 
                 alignment_range, alignment_strength, cohesion_range, cohesion_strength):

        # Initialize position and movement
        self.position = np.array(position, dtype = float)
        self.velocity = np.array(velocity, dtype = float)
        self.acceleration = np.array([0.0, 0.0], dtype = float)
        self.flock = flock 
        self.max_speed = max_speed
        self.delta = delta

        # Determine direction
        self.separation_range = separation_range
        self.separation_strength = separation_strength
        self.alignment_range = alignment_range
        self.alignment_strength = alignment_strength        
        self.cohesion_range = cohesion_range
        self.cohesion_strength = cohesion_strength

    def update(self): 

        seperation = self.separation()
        alignment = self.alignment()
        cohesion = self.cohesion()

        self.acceleration = seperation + alignment + cohesion
        self.velocity += self.acceleration 
        velocity_norm = np.linalg.norm(self.velocity)

        if velocity_norm > self.max_speed: 
            self.velocity = (self.velocity / velocity_norm) * self.max_speed
        
        self.position += self.velocity * self.delta

    def separation(self):
        """ 
        Current member should steer to avoid crowding local members

        """
        neighbourhood = 0
        direction = np.array([0.0, 0.0])

        for neighbour in self.flock: 
            if neighbour is not self: 
                distance = np.linalg.norm(self.position - neighbour.position)
                
                if distance > 0 and distance < self.separation_range:
                    difference = (self.position - neighbour.position) / distance
                    direction += difference
                    neighbourhood += 1 
                    
        if neighbourhood > 0: 
            direction /= neighbourhood
            norm = np.linalg.norm(direction)

            if norm > 0: 
                direction = (direction / norm) * self.separation_strength

        return direction

    def alignment(self):
        """ 
        Current member should steer towards the average heading of local members
        
        """
        neighbourhood = 0
        direction = np.array([0.0, 0.0])

        for neighbour in self.flock: 
            if neighbour is not self: 
                distance = np.linalg.norm(self.position - neighbour.position)
                
                if distance > 0 and distance < self.alignment_range:
                    direction += neighbour.velocity
                    neighbourhood += 1 
                    
        if neighbourhood > 0: 
            direction /= neighbourhood
            norm = np.linalg.norm(direction)

            if norm > 0: 
                direction = (direction / norm) * self.alignment_strength

        return direction

    def cohesion(self): 
        """ 
        Current member should steer to move toward the average position of local members
        
        """
        centroid = np.array([0.0, 0.0])
        neighbourhood = 0
        direction = np.array([0.0, 0.0])

        for neighbour in self.flock: 
            if neighbour is not self: 
                distance = np.linalg.norm(self.position - neighbour.position)
                
                if distance > 0 and distance < self.cohesion_range:
                    centroid += neighbour.position
                    neighbourhood += 1 
                    
        if neighbourhood > 0: 
            centroid /= neighbourhood
            direction = centroid - self.position
            norm = np.linalg.norm(direction)

            if norm > 0: 
                direction = (direction / norm) * self.cohesion_strength

        return direction