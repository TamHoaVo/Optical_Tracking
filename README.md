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
