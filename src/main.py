from Stable import Stable
from Flock import Flock

def main():
    herder_size = 3
    flock_size = 20
    width, height = 1000, 800 

    stable = Stable(flock_size, herder_size, width, height)  
    stable.delta = 0.1
    stable.max_speed = 1
    
    stable.separation_range = 0.001
    stable.alignment_range = 0.001
    stable.cohesion_range = 0.001

    stable.separation_strength = 0.02
    stable.alignment_strength = 0.005
    stable.cohesion_strength = 0.05
    
    stable.groid_to_herder_distance = 2.0
    stable.seperation_range_herders = 0.01

    stable.run()  

if __name__ == "__main__":
    main()