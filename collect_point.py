import json
import numpy as np
import cv2
import matplotlib.pyplot as plt

# -------- LOAD POINTS --------
with open("points.json") as f:
    data = json.load(f)

def load_points(name):
    pts = np.array(data[name], dtype=np.float32)
    return pts

pts1 = load_points("img1.jpg")
pts2 = load_points("img2.jpg")
pts3 = load_points("img3.jpg")
pts4 = load_points("img4.jpg")

# -------- REFERENCE PLANE (img1) --------
ref_pts = pts1

# -------- COMPUTE HOMOGRAPHIES --------
H2, _ = cv2.findHomography(pts2, ref_pts)
H3, _ = cv2.findHomography(pts3, ref_pts)
H4, _ = cv2.findHomography(pts4, ref_pts)

# -------- WARP POINTS BACK TO SAME PLANE --------
def warp_points(pts, H):
    pts_h = np.hstack([pts, np.ones((pts.shape[0],1))])
    warped = (H @ pts_h.T).T
    warped = warped[:, :2] / warped[:, 2:]
    return warped

pts2_w = warp_points(pts2, H2)
pts3_w = warp_points(pts3, H3)
pts4_w = warp_points(pts4, H4)

# -------- COMBINE ALL POINTS --------
all_pts = np.vstack([ref_pts, pts2_w, pts3_w, pts4_w])

# -------- NORMALIZE --------
all_pts -= np.mean(all_pts, axis=0)
all_pts /= np.max(np.abs(all_pts))

# -------- ORDER POINTS --------
center = np.mean(all_pts, axis=0)
angles = np.arctan2(all_pts[:,1]-center[1],
                    all_pts[:,0]-center[0])
order = np.argsort(angles)
all_pts = all_pts[order]

# -------- PLOT --------
plt.scatter(all_pts[:,0], all_pts[:,1], s=80)

plt.plot(all_pts[:,0], all_pts[:,1], 'r-')
plt.plot([all_pts[-1,0], all_pts[0,0]],
         [all_pts[-1,1], all_pts[0,1]], 'r-')

plt.title("Planar Reconstruction (Homography)")
plt.axis('equal')
plt.grid()
plt.show()