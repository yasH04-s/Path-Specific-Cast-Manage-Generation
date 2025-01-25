# verification.py
def verify_setup():
    try:
        import numpy as np
        import cv2
        import matplotlib.pyplot as plt
        print("All required packages are installed!")

        # Test numpy
        arr = np.array([1, 2, 3])
        print("NumPy works!")

        # Test OpenCV
        img = np.zeros((100, 100), dtype=np.uint8)
        print("OpenCV works!")

        # Test matplotlib
        plt.plot([1, 2, 3], [1, 2, 3])
        plt.show()
        print("Matplotlib works!")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    verify_setup()