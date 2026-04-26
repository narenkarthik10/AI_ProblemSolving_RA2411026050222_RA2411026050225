# Artificial Intelligence - Problem Solving Assignment

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![HTML5](https://img.shields.io/badge/HTML5-Interactive-orange?style=for-the-badge&logo=html5)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow?style=for-the-badge&logo=javascript)

This repository contains the complete implementation of two AI problem-solving tasks. It features both purely algorithm-driven Python backend models and a highly interactive, modern web-based Graphical User Interface (GUI).

**🌐 Live Interactive Demo:** https://narenkarthik10.github.io/AI_ProblemSolving_RA2411026050222_RA2411026050225/

---

## 📂 Repository Structure

```text
/
├── index.html                   # High-fidelity Interactive GUI for the Route Finder
├── python_models/               # Standalone Python algorithmic implementations
│   ├── route_finder.py          # A* Search algorithm (Console Application)
│   └── loan_prediction.py       # KNN Classification algorithm (Pure Python ML)
└── README.md                    # Project Documentation
```


# Problem 1: GPS-Based City Route Finder (Problem 11)

## Problem Description: 
A navigation system designed to find the fastest and most optimal route between a starting location and a destination within a city represented as a weighted graph.

## Algorithm Used: 
A* Search Algorithm. This informed search strategy computes the shortest path by calculating the actual travel cost from the start node g(n) and combining it with a heuristic estimation of the distance to the goal (h(n)).

## Key Features:Interactive GUI (index.html): 
Features a dynamic, glassmorphism-styled dashboard with an animated particle background. Uses vis.js to render an interactive node graph where users can dynamically add locations, draw roads, and calculate paths in real-time.

Console App (route_finder.py): Includes a dynamic map builder allowing users to define custom nodes, edges, and heuristics directly via the command line.

## Execution Steps:
Frontend: Visit the live demo link above. Select a Start and Goal node, or use the "Edit" tools to modify the map, then click Calculate Optimal Route.
Backend: Run python python_models/route_finder.py in your terminal. Choose option 1 for the default map or option 2 to build a custom graph via text input.
