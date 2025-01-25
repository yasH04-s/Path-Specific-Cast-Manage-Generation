# test.py
from simulation_environment import SimulationEnvironment
from aruco_detector import ArucoDetector
from occupancy_grid import OccupancyGrid
from cast_mapping import CastMapper
from path_planner import PathPlanner

# Test Simulation Environment
def test_environment():
    env = SimulationEnvironment(size=(100, 100))
    env.add_obstacle(20, 20, 10, 30)
    env.add_obstacle(50, 40, 30, 10)
    env.place_robot((10, 10))
    env.visualize()

# Test ArUco Detection
def test_aruco():
    detector = ArucoDetector()
    marker = detector.generate_marker(1)
    cv2.imshow('ArUco Marker', marker)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Test Occupancy Grid
def test_grid():
    grid = OccupancyGrid(size=(100, 100))
    # Add some test cells
    grid.update_cell(50, 50, True)
    grid.update_cell(51, 50, False)
    plt.imshow(grid.grid, cmap='gray')
    plt.show()

# Test Cast Mapping
def test_cast_mapping():
    mapper = CastMapper(grid_size=(100, 100))
    cast_map = mapper.cast_rays(position=(50, 50))
    plt.imshow(cast_map, cmap='gray')
    plt.show()
if __name__ == "__main__":
    print("Select test to run:")
    print("1. Test Environment")
    print("2. Test ArUco")
    print("3. Test Grid")
    print("4. Test Cast Mapping")
    print("5. Run All Tests")
    choice = input("Enter choice (1-5): ")
    if choice == '1':
        test_environment()
    elif choice == '2':
        test_aruco()
    elif choice == '3':
        test_grid()
    elif choice == '4':
        test_cast_mapping()
    elif choice == '5':
        test_environment()
        test_aruco()
        test_grid()
        test_cast_mapping()