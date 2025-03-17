import numpy as np 

class Groid:  
    def __init__(self, position, velocity, flock):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.array([0.0, 0.0], dtype=float)
        self.flock = flock  
        self.max_speed = flock.max_speed
        self.delta = flock.delta
        self.separation_range = flock.separation_range
        self.separation_strength = flock.separation_strength
        self.alignment_range = flock.alignment_range
        self.alignment_strength = flock.alignment_strength
        self.cohesion_range = flock.cohesion_range
        self.cohesion_strength = flock.cohesion_strength
        self.groid_to_herder_distance = flock.groid_to_herder_distance

    def update(self):
        """
        Updates the position of the Groid based on flocking behaviors.
        """
        separation = self.separation()
        alignment = self.alignment()
        cohesion = self.cohesion()

        self.acceleration = separation + alignment + cohesion
        self.velocity += self.acceleration
        velocity_norm = np.linalg.norm(self.velocity)

        if velocity_norm > self.max_speed: 
            self.velocity = (self.velocity / velocity_norm) * self.max_speed
        
        self.position += self.velocity * self.delta
        self.enforce_boundaries(self.flock.width, self.flock.height) 

    def separation(self):
        """ 
        Steer away from nearby Groids and Herders.
        """
        neighborhood = 0
        direction = np.array([0.0, 0.0])

        for neighbour in self.flock.flock: 
            if neighbour is not self: 
                distance = np.linalg.norm(self.position - neighbour.position)
                
                if 0 < distance < self.separation_range:
                    difference = (self.position - neighbour.position) / distance
                    direction += difference
                    neighborhood += 1 

        for herder in self.flock.herders: 
             distance = np.linalg.norm(self.position - herder.position)

             if 0 < distance < self.groid_to_herder_distance: 
                difference = (self.position - herder.position) / distance
                direction += difference
                neighborhood += 1
                    
        if neighborhood > 0: 
            direction /= neighborhood
            norm = np.linalg.norm(direction)
            if norm > 0: 
                direction = (direction / norm) * self.separation_strength

        return direction

    def alignment(self):
        """ 
        Steer towards the average velocity of nearby Groids.
        """
        neighborhood = 0
        direction = np.array([0.0, 0.0])

        for neighbour in self.flock.flock:  
            if neighbour is not self: 
                distance = np.linalg.norm(self.position - neighbour.position)
                
                if 0 < distance < self.alignment_range:
                    direction += neighbour.velocity
                    neighborhood += 1 
                    
        if neighborhood > 0: 
            direction /= neighborhood
            norm = np.linalg.norm(direction)
            if norm > 0: 
                direction = (direction / norm) * self.alignment_strength

        return direction

    def cohesion(self): 
        """ 
        Steer towards the center of mass of nearby Groids.
        """
        centroid = np.array([0.0, 0.0])
        neighborhood = 0
        direction = np.array([0.0, 0.0])

        for neighbour in self.flock.flock:
            if neighbour is not self: 
                distance = np.linalg.norm(self.position - neighbour.position)
                
                if 0 < distance < self.cohesion_range:
                    centroid += neighbour.position
                    neighborhood += 1 
                    
        if neighborhood > 0: 
            centroid /= neighborhood
            direction = centroid - self.position
            norm = np.linalg.norm(direction)
            if norm > 0: 
                direction = (direction / norm) * self.cohesion_strength

        return direction

    def enforce_boundaries(self, width, height):
        """
        Wrap around boundaries or contain movement within limits.
        """
        if self.position[0] < 0 or self.position[0] > width:
            self.velocity[0] *= -1  
            self.position[0] = max(0, min(self.position[0], width)) 

        if self.position[1] < 0 or self.position[1] > height:
            self.velocity[1] *= -1  
            self.position[1] = max(0, min(self.position[1], height)) 