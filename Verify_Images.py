import cv2
import face_recognition
import os

path = 'ImagesAttendance'
for person_name in os.listdir(path):
    person_folder = os.path.join(path, person_name)
    if not os.path.isdir(person_folder):
        continue
    for filename in os.listdir(person_folder):
        file_path = os.path.join(person_folder, filename)
        img = cv2.imread(file_path)
        if img is None:
            print(f"❌ Cannot read {file_path}")
            continue
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        faces = face_recognition.face_locations(rgb)
        print(f"{filename}: {len(faces)} face(s) detected")