import cv2
from deepface import DeepFace

cap = cv2.VideoCapture("interview3.mp4")

print("Video opened:", cap.isOpened())

while True:
    ret, frame = cap.read()
    if not ret:
        break

    try:
        # Face detection
        faces = DeepFace.extract_faces(frame, enforce_detection=False)
        face_count = len(faces)

        if face_count > 1:
            cv2.putText(frame, "WARNING: Multiple People!",
                        (50,100), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0,0,255), 3)

        if face_count == 0:
            cv2.putText(frame, "Looking Away!",
                        (50,150), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0,0,255), 2)

        # Emotion
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']

        cv2.putText(frame, f"Emotion: {emotion}",
                    (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0,255,0), 2)

    except:
        pass

    cv2.imshow("Interview Analyzer", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()