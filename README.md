# EvoDrive - Genetic Algorithm for Autonomous Driving 🚗💡

EvoDrive is a project that combines genetic algorithms with advanced simulation techniques to create a pseudo-3D autonomous driving environment. Initially inspired by NEAT (NeuroEvolution of Augmenting Topologies), our project has evolved into a broader implementation of genetic algorithms for self-driving car simulations. This project demonstrates the use of AI to handle tasks such as obstacle avoidance, shortest path navigation, and dynamic world interaction.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Project Structure](#project-structure)
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

1. **Driving Mechanics**: 
   - Car movement based on acceleration, friction, and rotation using trigonometry.
   - Keyboard controls for initial manual testing.

2. **Genetic Algorithm**:
   - Cars evolve their driving behavior through genetic mutations and selection.
   - Fitness scores are based on distance covered and obstacles avoided.

3. **Sensors and Collision Detection**:
   - Ray-casting sensors for proximity detection of obstacles and road edges.
   - Segment intersections used for accurate collision detection.

4. **Dynamic Route Selection**:
   - Integration of Dijkstra's algorithm for finding optimal paths.

5. **Virtual World Building**:
   - Procedural generation of roads, buildings, and trees.
   - Realistic traffic simulation with dummy cars and road markings.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/EvoDrive-Genetic-Algorithm-for-Autonomous-Driving.git
   cd EvoDrive-Genetic-Algorithm-for-Autonomous-Driving
