# Smart Attendance System

Face-recognition attendance demo: Python scripts for real-time capture, recognition, and automated CSV logging.
---

## Quick summary
- Core: `Attendance.py` — Main loop for webcam capture, face matching, and logging.
- Setup: `Verify_Images.py` — Helper script to verify and encode known faces.
- Storage: Auto-generated CSV files (e.g., `Attendance_YYYY-MM-DD.csv`).
- Assets: `ImagesAttendance/` directory for storing registered user images.

---

## Features
- Real-time face detection using OpenCV and `face_recognition`.
- Automatic, timestamped attendance logging.
- Built-in logic to prevent duplicate entries on the same day.
- Fast, offline, and fully contactless operation.

---

## Quickstart (local)
Prereqs: Python 3.x, CMake (required for the `dlib` backend).

Install deps and run:

```powershell
git clone [https://github.com/aniffahmed/Attendance-Tracker.git](https://github.com/aniffahmed/Attendance-Tracker.git)
cd Attendance-Tracker
pip install opencv-python face-recognition numpy
python Attendance.py

Demo sequence: Add images → Run script → Face recognized:

    Create a folder ImagesAttendance/StudentName/ and add 1-5 clear photos.

    Run python Attendance.py.

    Step in front of the webcam; your face is recognized and marked in today's CSV.

    Press q to exit the webcam window.

Configuration & privacy

    .gitignore intentionally excludes *.csv files to prevent sensitive attendance logs from being committed to version control.

    No external databases or internet connection required; all matching is processed locally against the ImagesAttendance directory.
