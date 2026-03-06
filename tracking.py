import cv2
import numpy as np

# Load video
cap = cv2.VideoCapture("video2.mp4")

# Read two consecutive frames
ret, frame1 = cap.read()

# Skip some frames
for i in range(10):
    cap.read()

ret, frame2 = cap.read()

# Convert to grayscale
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

# Detect feature points
features = cv2.goodFeaturesToTrack(gray1,
                                   maxCorners=50,
                                   qualityLevel=0.3,
                                   minDistance=7)

# Track those features
p2, status, error = cv2.calcOpticalFlowPyrLK(gray1, gray2, features, None)

print("Pixel Tracking Results\n")

for i,(new,old) in enumerate(zip(p2,features)):

    x_new,y_new = new.ravel()
    x_old,y_old = old.ravel()

    dx = x_new - x_old
    dy = y_new - y_old

    print(f"Point {i+1}")
    print(f"Frame1: ({x_old:.2f},{y_old:.2f})")
    print(f"Frame2: ({x_new:.2f},{y_new:.2f})")
    print(f"Motion Vector (u,v): ({dx:.2f},{dy:.2f})\n")

    # Draw motion arrow
    cv2.arrowedLine(frame2,
                    (int(x_old),int(y_old)),
                    (int(x_new),int(y_new)),
                    (0,255,0),2)

# Show tracking result
cv2.imshow("Tracked Motion", frame2)

cv2.waitKey(0)
cv2.destroyAllWindows()

cap.release()