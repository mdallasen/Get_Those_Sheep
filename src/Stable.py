from Flock import Flock
import pygame as pg
import pygame_gui

class Stable(Flock):
    def __init__(self):
        super().__init__(
            flock_size = 120, 
            herder_size = 3,  
            width = 1800,
            height = 900,
            
            max_speed = 0.8,  
            delta = 15, 

            separation_range = 25,  
            separation_strength = 1.8,  

            alignment_range=50, 
            alignment_strength=2.5, 

            cohesion_range=60,  
            cohesion_strength=3.0,  
            
            groid_to_herder_distance = 400,  
            separation_range_herders = 150, 
            
            max_speed_herders = 1.2,  
            separation_strength_herder = 0.7 
        )

        pg.init()
        self.screen = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption("Flock Simulation")
        self.clock = pg.time.Clock()
        self.running = True

        self.manager = pygame_gui.UIManager((self.width, self.height))
        self.font = pg.font.Font(None, 24)

        self.parameters = {
            "max_speed": (0.1, 2.5, 0.8),  
            "delta": (1, 50, 15),  
            "separation_range": (5, 80, 25),  
            "separation_strength": (0.1, 5.0, 1.5),  
            "alignment_range": (10, 120, 50),  
            "alignment_strength": (0.1, 5.0, 2.5), 
            "cohesion_range": (10, 120, 60),  
            "cohesion_strength": (0.1, 5.0, 2.8),  
            "groid_to_herder_distance": (100, 1000, 300),  
            "separation_range_herders": (50, 300, 150),  
            "max_speed_herders": (0.1, 1.5, 1.2),  
            "separation_strength_herder": (0.01, 2.0, 0.8)  
        }

        self.sliders = {}
        self.labels = {}

        y_offset = 50
        x_label_offset = self.width - 400
        x_slider_offset = self.width - 200 

        for param, (min_val, max_val, start_val) in self.parameters.items():
            self.labels[param] = (x_label_offset, y_offset + 5)

            self.sliders[param] = pygame_gui.elements.UIHorizontalSlider(
                relative_rect=pg.Rect((x_slider_offset, y_offset), (150, 20)),
                start_value=start_val,
                value_range=(min_val, max_val),
                manager=self.manager
            )

            y_offset += 30  

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

        for param, pos in self.labels.items():
            value = getattr(self, param, 0)
            self.render_text(f"{param}: {value:.2f}", pos[0], pos[1])

        self.manager.draw_ui(self.screen)
        pg.display.flip()

    def render_text(self, text, x, y):
        """
        Render text on the screen.
        """
        text_surface = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(text_surface, (x, y))
    
    def update_parameters(self):
        """
        Update flock simulation parameters from sliders.
        """
        for param in self.sliders:
            new_value = self.sliders[param].get_current_value()
            setattr(self, param, new_value)

        for groid in self.flock:
            groid.max_speed = self.max_speed
            groid.delta = self.delta
            groid.separation_range = self.separation_range
            groid.separation_strength = self.separation_strength
            groid.alignment_range = self.alignment_range
            groid.alignment_strength = self.alignment_strength
            groid.cohesion_range = self.cohesion_range
            groid.cohesion_strength = self.cohesion_strength
            groid.groid_to_herder_distance = self.groid_to_herder_distance

        for herder in self.herders:
            herder.max_speed = self.max_speed_herders
            herder.separation_range = self.separation_range_herders
            herder.separation_strength = self.separation_strength_herder
   
    def run(self):
        """
        Main loop to update and display the simulation.
        """
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0  

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.running = False

                self.manager.process_events(event)

            self.update_parameters()
            self.manager.update(time_delta)
            self.update()
            self.draw()

        pg.quit()