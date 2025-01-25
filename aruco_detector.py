import numpy as np
import cv2
import cv2.aruco as aruco
import matplotlib.pyplot as plt
class ArucoDetector:
    def __init__(self):
        self.aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
        self.parameters = aruco.DetectorParameters()

    def generate_marker(self, marker_id, size=200):
        """Generate ArUco marker image"""
        marker = np.zeros((size, size), dtype=np.uint8)
        marker = aruco.generateImageMarker(self.aruco_dict, marker_id, size, marker, 1)
        return marker

    def detect_markers(self, image):
        """Detect ArUco markers in image"""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        corners, ids, rejected = aruco.detectMarkers(gray, self.aruco_dict, parameters=self.parameters)
        return corners, ids

# Test code
if __name__ == "__main__":
    # Create detector instance
    detector = ArucoDetector()
    # Generate a marker
    marker_id = 1
    marker_image = detector.generate_marker(marker_id)

    # Display the marker using matplotlib
    plt.figure(figsize=(8, 8))
    plt.subplot(121)
    plt.title(f'ArUco Marker ID: {marker_id}')
    plt.imshow(marker_image, cmap='gray')

    # Create a test image with the marker
    test_image = np.zeros((400, 400, 3), dtype=np.uint8)
    test_image[100:300, 100:300] = cv2.cvtColor(marker_image, cv2.COLOR_GRAY2BGR)

    # Detect the marker
    corners, ids = detector.detect_markers(test_image)

    # Draw detected markers
    if ids is not None:
        aruco.drawDetectedMarkers(test_image, corners, ids)

    # Display the detection result
    plt.subplot(122)
    plt.title('Marker Detection')
    plt.imshow(cv2.cvtColor(test_image, cv2.COLOR_BGR2RGB))
    plt.tight_layout()
    plt.show()
    print(f"Generated marker with ID: {marker_id}")
    if ids is not None:
        print(f"Detected markers with IDs: {ids}")
    else:
        print("No markers detected")