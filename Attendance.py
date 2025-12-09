import os
os.environ["QT_LOGGING_RULES"] = "*.warning=false"
# Attendance System with Face Recognition
# ---------------------------------------
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import csv

# --------------------------------------------------------------------------
# Load and Encode Known Faces (Supports multiple images per person)
# --------------------------------------------------------------------------
path = 'ImagesAttendance'
images = []
known_face_names = []
 
print("Loading and encoding known faces...")

if not os.path.exists(path):
    print(f"❌ Folder '{path}' not found. Create it and add face folders (one per person).")
    exit()

for person_name in os.listdir(path):
    person_folder = os.path.join(path, person_name)
    if not os.path.isdir(person_folder):
        continue  # skip if not a folder

    for filename in os.listdir(person_folder):
        file_path = os.path.join(person_folder, filename)
        curImg = cv2.imread(file_path)
        if curImg is None:
            print(f"⚠️ Skipping file: {filename} (not an image)")
            continue
        images.append(curImg)
        known_face_names.append(person_name)  # same name for all images of that person

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        try:
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        except IndexError:
            print(f"⚠️ No face found in one of the images.")
            continue
    return encodeList

known_face_encodings = findEncodings(images)
print("✅ Encoding complete! Ready for facial recognition.")

# --------------------------------------------------------------------------
# Attendance CSV Setup
# --------------------------------------------------------------------------
current_date = datetime.now().strftime("%Y-%m-%d")
csv_filename = f'Attendance_{current_date}.csv'
students_marked_for_today = []

with open(csv_filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Time'])

# --------------------------------------------------------------------------
# Live Video Capture
# --------------------------------------------------------------------------
video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # force Windows backend

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("❌ Failed to grab frame from webcam.")
        break

    # Resize frame to 1/4 size for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Detect faces and encodings
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if len(known_face_encodings) > 0:
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

        # Mark attendance only once per day
        if name != "Unknown" and name not in students_marked_for_today:
            current_time = datetime.now().strftime("%H:%M:%S")
            with open(csv_filename, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([name, current_time])
            students_marked_for_today.append(name)
            print(f"✅ Attendance marked for: {name}")

        # Draw rectangle and name on video
        top, right, bottom, left = face_location
        top, right, bottom, left = top*4, right*4, bottom*4, left*4  # scale back
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, bottom+30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Attendance System', frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("👋 Exiting program...")
        break

# --------------------------------------------------------------------------
# Cleanup
# --------------------------------------------------------------------------
video_capture.release()
cv2.destroyAllWindows()