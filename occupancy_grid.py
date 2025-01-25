import numpy as np
class OccupancyGrid:
    def __init__(self, size):
        self.size = size
        self.grid = np.zeros(size)  # -1: free, 0: unknown, 1: occupied
        self.probability_grid = np.ones(size) * 0.5

    def update_cell(self, x, y, occupied, confidence=0.9):
        if not (0 <= x < self.size[0] and 0 <= y < self.size[1]):
            return

        prior = np.log(self.probability_grid[y, x] / (1 - self.probability_grid[y, x]))
        if occupied:
            posterior = prior + np.log(confidence / (1 - confidence))
        else:
            posterior = prior + np.log((1 - confidence) / confidence)

        self.probability_grid[y, x] = 1 - (1 / (1 + np.exp(posterior)))

        if self.probability_grid[y, x] > 0.7:
            self.grid[y, x] = 1
        elif self.probability_grid[y, x] < 0.3:
            self.grid[y, x] = -1