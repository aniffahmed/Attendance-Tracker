# Smart Attendance System using Face Recognition

A Python-based smart attendance system that automatically marks attendance by recognizing faces in real time using a webcam.

## Features
- Real-time face detection and recognition
- Automatic attendance logging with timestamp
- Eliminates manual attendance process

## Tech Stack
- Python
- OpenCV
- face_recognition library
- NumPy

## How It Works
1. The system captures live video from a webcam.
2. Faces are detected and compared with known face encodings.
3. When a match is found, attendance is marked automatically.

## Installation & Usage
```bash
pip install -r requirements.txt
python main.py
