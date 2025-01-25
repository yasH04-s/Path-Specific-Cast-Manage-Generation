import matplotlib.pyplot as plt
from simulation_environment import SimulationEnvironment
from aruco_detector import ArucoDetector
from occupancy_grid import OccupancyGrid
from cast_mapping import CastMapper
from path_planner import PathPlanner

def run_simulation():
    # Initialize all components
    env = SimulationEnvironment(size=(100, 100))
    aruco_detector = ArucoDetector()
    occupancy_grid = OccupancyGrid(size=(100, 100))
    cast_mapper = CastMapper(grid_size=(100, 100))
    path_planner = PathPlanner(grid_size=(100, 100))

    # Set up environment
    env.add_obstacle(20, 20, 10, 30)  # Add vertical obstacle
    env.add_obstacle(50, 40, 30, 10)  # Add horizontal obstacle
    env.add_aruco_marker(1, (80, 80))  # Add marker
    env.place_robot((10, 10))  # Place robot

    # Generate cast map from robot position
    cast_map = cast_mapper.cast_rays(env.robot_position)
    # Update occupancy grid
    for y in range(100):
        for x in range(100):
            if cast_map[y, x] == 1:
                occupancy_grid.update_cell(x, y, env.map[y, x] == 1)

    # Build navigation graph and find path
    path_planner.build_graph(occupancy_grid.grid)
    path = path_planner.find_path(env.robot_position, (90, 90))

    # Visualize results
    plt.figure(figsize=(15, 5))

    # Plot original environment with path
    plt.subplot(131)
    plt.title('Environment with Path')
    plt.imshow(env.map, cmap='gray')
    if path:
        path_x, path_y = zip(*path)
        plt.plot(path_x, path_y, 'r-', linewidth=2, label='Path')
    plt.plot(env.robot_position[0], env.robot_position[1], 'bo', label='Robot')
    plt.legend()

    # Plot cast map
    plt.subplot(132)
    plt.title('Cast Map')
    plt.imshow(cast_map, cmap='gray')

    # Plot occupancy grid
    plt.subplot(133)
    plt.title('Occupancy Grid')
    plt.imshow(occupancy_grid.grid, cmap='gray')
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    run_simulation()