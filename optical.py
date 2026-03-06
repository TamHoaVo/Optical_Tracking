import cv2
import numpy as np

# Open video
cap = cv2.VideoCapture("video1.mp4")

# Check if video opened correctly
if not cap.isOpened():
    print("Error opening video file")
    exit()

# Read first frame
ret, frame1 = cap.read()

# Convert to grayscale
prvs = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

# Create HSV image for visualization
hsv = np.zeros_like(frame1)
hsv[...,1] = 255   # full saturation

while True:

    ret, frame2 = cap.read()

    if not ret:
        break

    # Convert frame to grayscale
    next = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # Calculate optical flow
    flow = cv2.calcOpticalFlowFarneback(
        prvs, next,
        None,
        0.5,    # pyramid scale
        3,      # levels
        15,     # window size
        3,      # iterations
        5,      # poly_n
        1.2,    # poly_sigma
        0
    )

    # Convert flow vectors to magnitude and angle
    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])

    # Encode direction as hue
    hsv[...,0] = ang * 180 / np.pi / 2

    # Encode magnitude as brightness
    hsv[...,2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)

    # Convert HSV to BGR for display
    rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    # Show optical flow
    cv2.imshow('Optical Flow', rgb)

    # Press ESC to stop
    if cv2.waitKey(30) & 0xff == 27:
        break

    # Update previous frame
    prvs = next

# Release video
cap.release()

# Close windows
cv2.destroyAllWindows()