import cv2
import dlib

webcam = cv2.VideoCapture(0)

while True:
    ret, frame = webcam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_detector_hog = dlib.get_frontal_face_detector()

    detections = face_detector_hog(frame, 1)

    for face in detections:
        l, t, r, b = face.left(), face.top(), face.right(), face.bottom()
        cv2.rectangle(frame, (l, t), (r, b), (0, 255, 0), 2)

    cv2.imshow('WebCam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()