import heapq

def a_star_search(graph, heuristics, start, goal):
    open_set = []
    # Push (f_cost, g_cost, node, path)
    heapq.heappush(open_set, (0 + heuristics[start], 0, start, [start]))
    
    explored = []
    g_costs = {start: 0}

    while open_set:
        _, current_cost, current_node, path = heapq.heappop(open_set)
        
        if current_node not in explored:
            explored.append(current_node)

        if current_node == goal:
            return path, current_cost, explored

        for neighbor, weight in graph.get(current_node, {}).items():
            tentative_g_cost = current_cost + weight
            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristics.get(neighbor, 0)
                heapq.heappush(open_set, (f_cost, tentative_g_cost, neighbor, path + [neighbor]))

    return None, 0, explored

# Graph based on the assignment's sample input
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'D': 1},
    'D': {'F': 3},
    'E': {'F': 1},
    'F': {}
}

# Heuristic (estimated distance to goal F)
heuristics = {'A': 7, 'B': 6, 'C': 4, 'D': 2, 'E': 1, 'F': 0}

print("--- GPS-Based City Route Finder (A* Algorithm) ---")
start_node = 'A'
goal_node = 'F'

print(f"Finding route from {start_node} to {goal_node}...\n")
path, cost, explored = a_star_search(graph, heuristics, start_node, goal_node)

if path:
    print(f"Optimal Path (A*): {' -> '.join(path)}")
    print(f"Total Cost: {cost}")
    print(f"Nodes Explored: {', '.join(explored)}")
else:
    print("No valid path exists.")
