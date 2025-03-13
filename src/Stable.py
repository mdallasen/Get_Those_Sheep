from Flock import Flock
import pygame as pg

import pygame as pg
from Flock import Flock

class Stable(Flock): 
    def __init__(self, flock_size, width, height):
        super().__init__(flock_size, width, height)  

        pg.init()
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption("Flock Simulation")
        self.clock = pg.time.Clock()
        self.running = True

    def draw_groids(self):
        """ Render all groids on the screen """
        self.screen.fill((0, 0, 0))  

        for groid in self.flock:
            x, y = int(groid.position[0]), int(groid.position[1])
            pg.draw.circle(self.screen, (0, 255, 0), (x, y), 2)  

        pg.display.flip()

    def run(self):
        """ Main loop to update and display the simulation """
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:  
                    self.running = False

            self.update()  
            self.draw_groids()  
            
            self.clock.tick(30)  

        pg.quit