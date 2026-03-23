# Optical Flow Motion Tracking – README

## Overview

This project demonstrates motion tracking between two video frames using optical flow. The goal is to compute pixel motion between consecutive frames and validate the theoretical motion tracking equation derived from the brightness constancy assumption.

Two videos are analyzed. Optical flow is computed to visualize motion, and feature points are tracked between frames to measure pixel displacement.

---

## Requirements

The following Python libraries are required:

* Python 3.x
* OpenCV (cv2)
* NumPy

Install dependencies using:

pip install opencv-python numpy

---

## Files

video1.mp4 – first input video
video2.mp4 – second input video
optical_flow.py – script for computing optical flow visualization
tracking_validation.py – script for feature tracking and motion validation

---

## How to Run

### 1. Optical Flow Visualization

Run the script to compute dense optical flow and visualize motion between frames.

python optical_flow.py

The program will display the optical flow video where:

* Color represents motion direction
* Brightness represents motion magnitude

Press **ESC** to exit the visualization.

---

### 2. Motion Tracking Validation

Run the tracking script:

python tracking_validation.py

The program will:

* Extract two frames from the video
* Detect feature points
* Track the feature points using the Lucas–Kanade method
* Print pixel displacement values (dx, dy)

Example output:

Point 8
Frame1: (271,364)
Frame2: (254.13,363.62)
Motion Vector (u,v): (-16.87,-0.38)

---

## Output

The program produces:

* Optical flow visualization showing motion direction and magnitude
* Pixel motion vectors for tracked feature points
* Validation of theoretical motion equations using actual pixel displacement

---

## Summary

The results demonstrate that optical flow can accurately estimate motion between frames. Static regions produce near-zero motion vectors, while moving objects generate larger displacement values, validating the theoretical motion tracking model.


# Planar Reconstruction using Homography (Multi-View)

##  Overview

This project reconstructs the **planar structure of an object** using four images taken from different viewpoints. Instead of full 3D Structure-from-Motion (SfM), a **homography-based approach** is used since the object lies on a flat plane.

The method aligns all views to a **common reference image**, producing a consistent 2D representation of the object and its boundary.

---

##  Key Idea

For planar objects, the projection model simplifies:

[
x' \sim Hx
]

where:

* (x), (x'): corresponding image points
* (H): homography matrix

This allows direct mapping between views without explicitly reconstructing 3D geometry.

---

## Input

### 1. Images

* `img1.jpg`, `img2.jpg`, `img3.jpg`, `img4.jpg`

### 2. Correspondence File (`points.json`)

Contains manually selected pixel coordinates for the same 4 points across all images.

Example:

```json
{
  "img1.jpg": [[u1,v1], [u2,v2], [u3,v3], [u4,v4]],
  "img2.jpg": [...],
  "img3.jpg": [...],
  "img4.jpg": [...]
}
```

---

##  Methodology

### Step 1: Load Correspondences

Points are loaded for each image and converted into NumPy arrays.

---

### Step 2: Select Reference Plane

* `img1` is chosen as the **reference view**
* All other images are mapped onto this plane

---

### Step 3: Estimate Homography

For each image:

[
x_{\text{ref}} \sim H_i x_i
]

Using:

```python
cv2.findHomography()
```

Each homography is computed from **4 point correspondences**.

---

### Step 4: Warp Points

Points are transformed using:

[
x' = \frac{Hx}{w}
]

Implemented as:

```python
warped = (H @ pts_h.T).T
warped = warped[:, :2] / warped[:, 2:]
```

---

### Step 5: Combine Views

All transformed points are stacked:

[
\mathcal{P} = \bigcup_i H_i x_i
]

This aggregates information from all views.

---

### Step 6: Normalize

To remove scale and translation ambiguity:

[
x \leftarrow \frac{x - \mu}{\max |x|}
]

---

### Step 7: Order Points

Points are sorted using angular ordering:

[
\theta = \tan^{-1}\left(\frac{y - y_c}{x - x_c}\right)
]

This ensures correct boundary visualization.

---

### Step 8: Visualization

* Scatter plot of reconstructed points
* Lines connecting points to form boundary

---

##  Output

* A **2D planar reconstruction** of the object
* A **quadrilateral shape** representing the object boundary

Note:

* The shape may appear skewed due to **projective distortion**
* Homography preserves lines but not angles or lengths

---

##  Limitations

* Only **4 points** are used → sensitive to noise
* Manual point selection introduces small errors
* Output is **projectively correct**, not metrically accurate

---

##  Possible Improvements

* Use more feature points (≥ 8)
* Apply **metric rectification** to recover true geometry
* Use automatic feature detection (e.g., ORB, SIFT)

---

##  Conclusion

This implementation demonstrates that for planar scenes, **homography is sufficient** to reconstruct structure across multiple views. It avoids the instability of full SfM while still capturing the geometry of the object.

---

##  How to Run

```bash
python your_script.py
```

Make sure:

* `points.json` is in the same directory
* All images are available

