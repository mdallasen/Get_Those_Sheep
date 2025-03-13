# Get Those Sheep

Development of "animals" herding agents leveraging both rules based and learning techniques. Use **boids** to simulate flocking behavior and create environment for "herders" to perform there respective tasks of consolidating and driving "animals" through a predefined "gate". 

Goal: Move "animals", randomly placed around a defined paddock or stable following a boids like flock, through a randomly placed gate.  

## Project Structure

```plaintext
├── src/
│   └── Flock.py
│   └── Groid.py
│   └── Herder.py (to be developed)
│   └── main.py 
│   └── Stable.py 
├── .gitignore
├── LICENSE
└── README.md
└── requirements.txt
```

## Source Description

- Flock: Initalizes and determines the parameters of the flock of animals
- Groid: Defines the rules of each individual animal
- Herder: Defines the rules or learning techniques required for each herder
- Main: Develops and deploys the simulation 
- Stable: Defines the paramaters that the simulation operates in and the location of the "gate" / exit point that the herders attempt to drive the animals through

