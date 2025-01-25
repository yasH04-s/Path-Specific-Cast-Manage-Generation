import numpy as np
class CastMapper:
    def __init__(self, grid_size):
        self.grid_size = grid_size
    def cast_rays(self, position, angle_range=360, ray_length=50):
        cast_map = np.zeros(self.grid_size)
        angles = np.linspace(0, 2 * np.pi, angle_range)
        for angle in angles:
            x, y = position
            dx = np.cos(angle)
            dy = np.sin(angle)
            for _ in range(ray_length):
                x += dx
                y += dy
                grid_x, grid_y = int(x), int(y)
                if not (0 <= grid_x < self.grid_size[0] and 0 <= grid_y < self.grid_size[1]):
                    break
                cast_map[grid_y, grid_x] = 1
        return cast_map