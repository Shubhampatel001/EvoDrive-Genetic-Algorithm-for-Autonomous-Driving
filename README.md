# **NEAT Wheels - Evolution in Motion** 🚗💨

### **Phase 1 of 5: Basic Self-Driving Car Model**

---

Welcome to the **NEAT Wheels - Evolution in Motion** project! This is a personal project aimed at building an intelligent, evolving self-driving car using the **NEAT (NeuroEvolution of Augmenting Topologies)** algorithm. The current repository contains the **Phase 1** of the project, where a basic self-driving car moves on a pre-defined track.

### **🚀 What Have I Done So Far?**

In this initial phase, I've focused on creating a foundational car movement model with basic controls, including:

- 📦 **Car Setup**: A car that can move and rotate based on user input.
- 🛤️ **Track Loading**: Displaying a pre-loaded track image where the car moves.
- 🔄 **Car Rotation**: Using `pygame.transform.rotozoom()` for smooth rotation and resizing.
- 🏎️ **Velocity Control**: Implementing `Vector2` for handling the speed and direction of the car.

This serves as the **first step** toward a more complex AI-driven self-driving car simulation.

---

## **🗺️ Project Phases Overview**

Here’s a quick breakdown of the upcoming phases of this project:

1. **Basic Self-Driving Car using NEAT** (Current Phase)
2. **Multiple Routes**: Introducing different paths and calculating the shortest distance using **Euclidean distance**.
3. **Stationary Obstacles**: Adding stationary obstacles that the car needs to avoid.
4. **Moving Objects**: Introducing dynamic, moving obstacles that the car must dodge.
5. **Unity Integration**: Converting the entire project into **Unity** for a more realistic experience.

---

## **📂 Project Structure**

- **`Assets/`**: Contains the track and car images used in the simulation.
- **`main.py`**: The core code for handling car movement, rotation, and track display.

---

## **💻 Technologies Used**

- **Python** 🐍
- **Pygame** 🎮
- **NEAT Algorithm** 🤖
  
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

The next step is to introduce multiple routes in the track and implement an algorithm to choose the shortest path using Euclidean distance.

Stay tuned for **Phase 2**! 📈

---

### **🙌 Contributing**

Feel free to open issues, submit pull requests, or suggest enhancements as I continue developing the next phases of this project!

---

#### **📝 License**

This project is licensed under the MIT License.

---

