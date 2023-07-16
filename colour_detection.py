import cv2
import numpy as np

def detect_color(frame):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the color ranges
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    lower_green = np.array([36, 25, 25])
    upper_green = np.array([86, 255, 255])

    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Create masks for each color
    red_mask = cv2.inRange(hsv_frame, lower_red, upper_red)
    green_mask = cv2.inRange(hsv_frame, lower_green, upper_green)
    blue_mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)

    # Check if any color is detected
    if np.sum(red_mask) > 0:
        print("Red detected")
    elif np.sum(green_mask) > 0:
        print("Green detected")
    elif np.sum(blue_mask) > 0:
        print("Blue detected")

# Initialize video capture
cap = cv2.VideoCapture(0colour)

while True:
    # Read the frame
    ret, frame = cap.read()

    # Perform color detection on the frame
    detect_color(frame)

    # Display the frame
    cv2.imshow('Color Detection', frame)

    # Check for key press
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
