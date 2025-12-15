🎓 Smart Attendance System using Face Recognition

A Python-based smart attendance automation system that uses real-time face recognition to identify individuals through a webcam and automatically record attendance with timestamps, eliminating manual effort and proxy attendance.

📌 Features

Real-time face detection and recognition using a webcam

Automatic attendance marking with date and time

Supports multiple images per person for better accuracy

CSV-based attendance logging (ignored from GitHub for data safety)

Simple and modular Python codebase

Fast and contactless attendance process

🛠️ Technologies Used

Python 3

OpenCV (cv2)

face_recognition library

NumPy

datetime

CSV file handling

📂 Project Structure
Attendance-Tracker/
│
├── ImagesAttendance/        # Known face images (one folder per person)
├── Attendance.py            # Main face recognition & attendance script
├── Verify_Images.py         # Script to verify and encode images
├── README.md                # Project documentation
├── .gitignore               # Ignored files (CSV logs, etc.)

⚙️ How It Works

The system loads and encodes known face images from the ImagesAttendance folder.

A webcam captures live video frames.

Faces are detected and compared with stored encodings.

When a match is found:

The person’s name is identified

Attendance is automatically recorded with date and time

Duplicate entries for the same day are avoided.

▶️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/aniffahmed/Attendance-Tracker.git
cd Attendance-Tracker

2️⃣ Install Required Libraries
pip install opencv-python face-recognition numpy


⚠️ Note: face_recognition requires dlib.
Make sure Python and CMake are properly installed.

3️⃣ Add Known Faces

Create folders inside ImagesAttendance/

Folder name = Person Name

Add 1–5 clear face images per person

Example:

ImagesAttendance/
├── Anif/
│   ├── img1.jpg
│   └── img2.jpg

4️⃣ Run the System
python Attendance.py


Press q to exit the webcam window.

🔐 Data Privacy

Attendance CSV files are intentionally ignored using .gitignore

Prevents sensitive data from being pushed to GitHub

Ensures safe and clean version control

🚀 Future Enhancements

GUI-based interface (Tkinter / PyQt)

Cloud-based attendance storage

Email/SMS attendance reports

Face mask detection integration

Mobile app support

Database integration (MySQL / Firebase)

📚 Use Cases

Educational institutions

Corporate offices

Training centers

Secure access environments

👤 Author

Anif Ahmed
Electronics and Communication Engineering (ECE)
GitHub: https://github.com/aniffahmed

⭐ If you found this project useful, feel free to star the repository.
