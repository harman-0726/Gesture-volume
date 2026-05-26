# Hand Gesture Volume Control using OpenCV + MediaPipe

A real-time AI-based hand gesture volume control system built using Python, OpenCV, MediaPipe, and PyAutoGUI.

This project detects the distance between the thumb tip and index finger tip using your webcam and controls the system volume accordingly.

---

## Features

- Real-time hand tracking
- Detects thumb and index finger landmarks
- Calculates finger distance
- Controls system volume using gestures
- Fast and lightweight
- Built using OpenCV and MediaPipe

---

## Technologies Used

- Python
- OpenCV
- MediaPipe
- PyAutoGUI

---

## How It Works

1. Webcam captures live video.
2. MediaPipe detects hand landmarks.
3. Thumb tip (`id = 4`) and index fingertip (`id = 8`) are tracked.
4. Distance between fingers is calculated.
5. If fingers move apart → volume increases.
6. If fingers move close → volume decreases.

---

## Hand Landmarks Used

| Landmark ID | Finger Part |
|---|---|
| 4 | Thumb Tip |
| 8 | Index Finger Tip |

---

## Installation

Install required libraries:

```bash
pip install opencv-python mediapipe pyautogui
