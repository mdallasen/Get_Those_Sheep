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

## Source Code Description

- Flock: Initalizes and determines the parameters of the flock of animals
- Groid: Defines the rules of each individual animal
- Herder: Defines the rules or learning techniques required for each herder
- Main: Develops and deploys the simulation 
- Stable: Defines the paramaters that the simulation operates in and the location of the "gate" / exit point that the herders attempt to drive the animals through

## How to Use

1. Go to terminal
2. Clone repository in desired folder via git clone https://github.com/your-username/Automated-Herding.git
3. Set up virtual enviornment and install dependencies via pip install -r requirements.txt
4. Open coding environment and run main.py
5. If wanting to change the parameters, go to Stable.py and change there
