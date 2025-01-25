import numpy as np
import matplotlib.pyplot as plt

class SimulationEnvironment:
    def __init__(self, size=(100, 100)):
        self.size = size
        self.map = np.zeros(size)
        self.robot_position = None
        self.markers = {}

    def add_obstacle(self, x, y, width, height):
        self.map[y:y + height, x:x + width] = 1

    def add_aruco_marker(self, marker_id, position):
        self.markers[marker_id] = position

    def place_robot(self, position):
        self.robot_position = position

    def visualize(self):
        plt.figure(figsize=(8, 8))
        plt.imshow(self.map, cmap='gray')
        if self.robot_position:
            plt.plot(self.robot_position[0], self.robot_position[1], 'ro', label='Robot')
        for marker_id, pos in self.markers.items():
            plt.plot(pos[0], pos[1], 'go', label=f'Marker {marker_id}')
        plt.legend()
        plt.grid(True)
        plt.title('Simulation Environment')
        plt.show()