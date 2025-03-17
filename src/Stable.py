from Flock import Flock
import pygame as pg

class Stable(Flock):
    def __init__(self):
        super().__init__(
            flock_size = 100,
            herder_size = 3,
            width = 1000,
            height = 500,
            max_speed = 0.5,  
            delta = 10,  
            separation_range = 50,  
            separation_strength = 0.05,  
            alignment_range = 100,  
            alignment_strength = 0.03,  
            cohesion_range = 150, 
            cohesion_strength = 0.02,  
            groid_to_herder_distance = 200,  
            separation_range_herders = 100,  
            max_speed_herders = 0.3,
            separation_strength_herder = 0.05
        )

        pg.init()
        self.screen = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption("Flock Simulation")
        self.clock = pg.time.Clock()
        self.running = True

    def draw(self):
        """
        Render all groids and herders on the screen.
        """
        self.screen.fill((0, 0, 0))

        for groid in self.flock:
            x, y = int(groid.position[0]), int(groid.position[1])
            pg.draw.circle(self.screen, (0, 255, 0), (x, y), 2)

        for herder in self.herders:
            x, y = int(herder.position[0]), int(herder.position[1])
            pg.draw.circle(self.screen, (0, 0, 255), (x, y), 2)

        pg.display.flip()

    def run(self):
        """
        Main loop to update and display the simulation.
        """
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:  
                    self.running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:  
                        self.running = False

            self.update()

            self.draw()

            self.clock.tick(60)

        pg.quit()