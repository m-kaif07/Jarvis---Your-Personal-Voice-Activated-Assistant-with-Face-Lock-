import cv2
import face_recognition as fr
import time

def face_lock(img_path):
    # Load the  encoded face image
    known_face = fr.load_image_file(img_path)
    known_face_encoding = fr.face_encodings(known_face)[0]

    # Initialize the webcam, in case of computer's default camera, change it to 0
    video_capture = cv2.VideoCapture(1)

    # Set a start time to track elapsed time
    start_time = time.time()
    duration = 5  # Extend the duration to seconds

    while time.time() - start_time < duration:
        ret, frame = video_capture.read()

        # Find all face locations in the frame (coordinates)
        face_locations = fr.face_locations(frame)
        face_encodings = fr.face_encodings(frame, face_locations)

        # to check if a face is matched
        face_matched = False

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Check if the current face matches the known face
            matches = fr.compare_faces([known_face_encoding], face_encoding)

            if True in matches:
                face_matched = True
                color = (0, 255, 0)
                text = "Program Unlocked !"
            else:
                color = (0, 0, 255)
                text = "Unknown"

            # Draw a rectangle around the face and display the name
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, text, (left, top - 12), font, 0.7, color, 2)

        # Display the frame / video
        cv2.imshow('Face_lock', frame)

        if cv2.waitKey(1) == 27:
            break

    video_capture.release()
    cv2.destroyAllWindows()
    return face_matched
