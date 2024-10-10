# **NEAT Wheels - Evolution in Motion** 🚗💨

### **Phase 2 of 5: Multiple Routes & Shortest Path Calculation**

---

Welcome back to the **NEAT Wheels - Evolution in Motion** project! After successfully completing **Phase 1**, where a basic self-driving car model was built, we now move on to **Phase 2** of the project: introducing multiple routes and calculating the shortest path using **Euclidean distance**.

### **🚀 What Was Done in Phase 1?**

In the first phase, I focused on laying the groundwork for car movement and controls, including:

- 📦 **Car Setup**: A car model that can move and rotate smoothly.
- 🛤️ **Track Loading**: Displaying a pre-defined track for the car to navigate.
- 🔄 **Car Rotation**: Implementing smooth rotation using `pygame.transform.rotozoom()`.
- 🏎️ **Velocity Control**: Utilizing `Vector2` for velocity and direction management.

This served as the foundation for more advanced AI-driven behavior that will be introduced in upcoming phases.

---

## **🗺️ Project Phases Overview**

Here’s a quick overview of the upcoming project phases:

1. **Basic Self-Driving Car using NEAT** (Completed ✅)
2. **Multiple Routes**: Introducing different paths and calculating the shortest distance using **Euclidean distance** (Next Phase ⏳)
3. **Stationary Obstacles**: Adding fixed obstacles the car needs to avoid.
4. **Moving Objects**: Introducing dynamic, moving obstacles that the car must dodge.
5. **Unity Integration**: Converting the entire project into **Unity** for a more realistic experience.

---

## **🌟 Current Focus: Phase 2 - Multiple Routes**

In **Phase 2**, the focus will be on adding multiple routes within the track. The goal is to have the car intelligently choose the shortest path using the **Euclidean distance** algorithm. This phase will lay the foundation for avoiding obstacles and dynamic route selection in future stages.

---

## **📂 Project Structure**

- **`Assets/`**: Contains track and car images for the simulation.
- **`main.py`**: Core logic for car movement, rotation, and track management.
- **`neat_config/`**: Configuration file for NEAT algorithm parameters.

---

## **💻 Technologies Used**

- **Python** 🐍
- **Pygame** 🎮
- **NEAT Algorithm** 🤖
  
---

## **📚 Libraries**

- **Pygame**: Pygame is a set of Python modules designed for writing video games. It provides functionality for rendering graphics, handling input, and managing game states. Official documentation: [Pygame Docs](https://www.pygame.org/docs/)
  
- **NEAT-Python**: NEAT (NeuroEvolution of Augmenting Topologies) is an evolutionary algorithm that evolves neural networks. This library helps in setting up and evolving neural networks for machine learning tasks. Official documentation: [NEAT-Python Docs](https://neat-python.readthedocs.io/en/latest/)

---

## **⚡ How to Run the Project Locally**

1. Clone the repository:
   ```bash
   git clone https://github.com/Shubhampatel001/NEAT-Wheels-Evolution-in-Motion.git
   ```
   
2. Navigate into the project directory:
   ```bash
   cd NEAT-Wheels-Evolution-in-Motion
   ```

3. Install dependencies:
   ```bash
   pip install pygame neat-python
   ```

4. Run the project:
   ```bash
   python main.py
   ```

---

## **🌟 What's Next?**

The next step is to introduce multiple routes in the track and implement an algorithm to choose the shortest path using **Euclidean distance**. This will allow the car to make more intelligent decisions when navigating complex routes.

Stay tuned for **Phase 2**! 📈

---

### **🙌 Contributing**

Feel free to open issues, submit pull requests, or suggest enhancements as I continue developing the next phases of this project!

---

#### **📝 License**

This project is licensed under the MIT License.
