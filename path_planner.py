import numpy as np
from queue import PriorityQueue

class PathPlanner:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.navigation_graph = {}

    def build_graph(self, occupancy_grid):
        self.navigation_graph.clear()

        for y in range(self.grid_size[0]):
            for x in range(self.grid_size[1]):
                if occupancy_grid[y, x] != 1:
                    node = (x, y)
                    self.navigation_graph[node] = []

                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        new_x, new_y = x + dx, y + dy
                        if (0 <= new_x < self.grid_size[1] and
                                0 <= new_y < self.grid_size[0] and
                                occupancy_grid[new_y, new_x] != 1):
                            self.navigation_graph[node].append((new_x, new_y))

    def find_path(self, start, goal):
        def heuristic(a, b):
            return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

        frontier = PriorityQueue()
        frontier.put((0, start))
        came_from = {start: None}
        cost_so_far = {start: 0}

        while not frontier.empty():
            current = frontier.get()[1]

            if current == goal:
                break

            for next_pos in self.navigation_graph.get(current, []):
                new_cost = cost_so_far[current] + 1

                if next_pos not in cost_so_far or new_cost < cost_so_far[next_pos]:
                    cost_so_far[next_pos] = new_cost
                    priority = new_cost + heuristic(goal, next_pos)
                    frontier.put((priority, next_pos))
                    came_from[next_pos] = current

        path = []
        current = goal
        while current is not None:
            path.append(current)
            current = came_from.get(current)
        path.reverse()

        return path