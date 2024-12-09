# EvoDrive - Genetic Algorithm for Autonomous Driving 🚗💡

EvoDrive is a project that combines genetic algorithms with advanced simulation techniques to create a pseudo-3D autonomous driving environment. Initially inspired by NEAT (NeuroEvolution of Augmenting Topologies), our project has evolved into a broader implementation of genetic algorithms for self-driving car simulations. This project demonstrates the use of AI to handle tasks such as obstacle avoidance, shortest path navigation, and dynamic world interaction.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Challenges Faced](#challenges-faced)
- [Future Plans](#future-plans)

---

## Project Overview

EvoDrive aims to simulate the following features in a dynamic environment:
1. Autonomous driving using genetic algorithms for evolutionary learning.
2. Handling stationary and moving obstacles in a realistic road setup.
3. Building a pseudo-3D environment with interactive elements such as traffic lights and road signs.
4. Dynamic route selection and shortest path computation using algorithms like Dijkstra’s.
5. Real-time visualization of neural network decisions.

---

## Features

### Core Functionalities
- **Genetic Algorithm for AI Evolution**: Mutation-based learning for car decision-making.
- **Obstacle Detection and Avoidance**: Sensors simulate real-world proximity detection.
- **Shortest Path Navigation**: Implementation of Dijkstra's algorithm for route optimization.
- **Dynamic Environments**: Real-time traffic simulation with AI dummy cars.

### Virtual World
- **Pseudo-3D World Design**: Roads, buildings, and trees with 3D-like effects.
- **Traffic Lights and Signs**: Dynamic traffic management with real-time signals.
- **Interactive Elements**: AI cars interacting with a procedurally generated environment.

### Visualization
- **Neural Network Representation**: Dynamic visualizations of the AI's decision-making process.
- **Bird’s-Eye View**: A fixed camera for tracking a single AI car's movements.
- **Mini-Map Navigation**: Simplified navigation for large virtual environments.

---

## Technologies Used

- **Programming Languages**: JavaScript
- **Libraries**: N/A
- **Algorithm**: Genetic Algorithm, Dijkstra's Algorithm
- **Simulation Tools**: Custom-built pseudo-3D environment 
- **Version Control**: GitHub

---

## How It Works

### **1. Simulation Environment**
The system creates a virtual road network where vehicles interact. The simulation tests various driving strategies, evaluating them based on predefined metrics like speed, safety, and fuel efficiency.

### **2. Genetic Algorithm for Optimization**
The genetic algorithm is the core mechanism driving strategy evolution.

- **Process**:
  - **Initial Population**: Randomly generated driving strategies are encoded as "chromosomes."
  - **Fitness Evaluation**: Strategies are tested in the simulation and scored based on metrics such as lap time, collision avoidance, and resource efficiency.
  - **Selection**: High-performing strategies are selected to propagate to the next generation.
  - **Crossover and Mutation**:
    - Crossover combines traits of two parent strategies to create offspring.
    - Mutation introduces random changes, ensuring diversity and avoiding local optima.

- **Why GA is Used**:
  GAs are ideal for exploring large, complex search spaces like driving behaviors where the optimal solution isn’t explicitly known.

### **3. Algorithms and Heuristics**

#### **a. Right-Hand Thumb Rule of Traffic**
- Vehicles follow this heuristic to maintain lane discipline and align their trajectories with road geometry.
- This rule ensures realistic driving dynamics, reduces lane violations, and enhances simulation authenticity.

#### **b. Dijkstra’s Algorithm for Pathfinding**
- The road network is represented as a graph with nodes (intersections) and edges (road segments).
- **Function**:
  - Computes the optimal path by minimizing costs like distance or travel time.
  - Ensures vehicles avoid obstacles and reach their destination efficiently.

#### **c. Interpolation for Smooth Path Generation**
- Generates intermediate waypoints between known points to create smooth vehicle trajectories.
- Splines are commonly used to ensure that vehicles follow a continuous and natural curve, avoiding abrupt changes.

#### **d. Envelope Intersection for Collision Detection**
- Vehicles and obstacles are encapsulated in bounding boxes for real-time collision detection.
- Overlapping envelopes trigger evasive actions (e.g., braking, steering adjustments).
- This technique ensures safety in dynamic and crowded environments.

### **4. Simulation Dynamics**
- **Interaction**:
  - Pathfinding (via Dijkstra) provides the initial navigation plan.
  - The genetic algorithm optimizes driving behaviors along the path.
  - Interpolation and collision detection refine movements and ensure safety.

- **Iterative Learning**:
  - Over generations, strategies evolve to meet or exceed performance benchmarks, resulting in efficient and robust autonomous driving solutions.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/EvoDrive-Genetic-Algorithm-for-Autonomous-Driving.git
   cd EvoDrive-Genetic-Algorithm-for-Autonomous-Driving
   
2. Run the JavaScript-based simulation:
   - Open index.html in your web browser.

## Challenges Faced
   - Hardware limitations prevented the use of CARLA and Unity for realistic simulation.
   - Debugging real-time simulations for accurate obstacle detection and pathfinding.
   - Optimization of genetic algorithms for dynamic environments with limited resources.

## Future Plans

- **Advanced AI Algorithms**: 
  - Introduce NEAT to complement the genetic algorithm for more adaptive decision-making.
  - Experiment with hybrid models combining genetic algorithms and deep learning.

- **Realistic Simulation Enhancements**:
  - Implement a fully 3D simulation environment using WebGL or Three.js for improved visual fidelity.
  - Incorporate weather effects (rain, fog, etc.) and varying road conditions (wet, icy, gravel).

- **Improved Pathfinding**:
  - Integrate A* algorithm alongside Dijkstra for more efficient route optimization.
  - Add support for dynamic re-routing in response to changing traffic and obstacles.

- **Traffic and Multi-Agent Behavior**:
  - Introduce cooperative AI cars capable of sharing information about traffic and obstacles.
  - Simulate complex traffic scenarios like intersections, roundabouts, and merging lanes.

- **Integration with Realistic Simulation Platforms**:
  - visit CARLA and Unity platforms for more realistic environment simulations.
  - Use Unity’s extensive library to create advanced object detection, traffic scenarios, and physics-based simulations.

- **Game Mode**:
  - Introduce a "Game Mode" where players can challenge the AI or design obstacles to test its capabilities.
  - Include leaderboards for AI performance in various scenarios.

These plans aim to push EvoDrive into new realms of capability and user interaction while staying accessible for further development and experimentation.

## License
   - This project is licensed under the MIT License. See the LICENSE file for more details.

## Contribution
   - We welcome contributions! Fork the repository, create a new branch for your changes, and submit a pull request. For major changes, please open an issue first to discuss your ideas.

## Acknowledgments
This project would not have been possible without the guidance and inspiration provided by various individuals and resources:

- **Radu Mariescu-Istodor**: A major credit goes to Radu Mariescu-Istodor for his detailed explanations, resources, and tutorials, which served as a foundation for understanding and implementing many aspects of this project. His work has been instrumental in shaping the technical and conceptual framework of EvoDrive.
- **Open-Source Community**: For providing tools, libraries, and platforms such as Pygame, JavaScript, and NEAT, which were critical to the development process.
- **Team Members**: Gratitude to all team members for their hard work, collaboration, and perseverance throughout the project.

We deeply appreciate all contributions and resources that have made this project a reality.

