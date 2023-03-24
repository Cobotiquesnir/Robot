import cv2
import mediapipe as mp
from pyniryo import *

mp_hands = mp.solutions.hands

robot = NiryoRobot("169.254.200.200")
robot.calibrate_auto()

cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)

        image_height, image_width, _ = image.shape
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for ids, landmrk in enumerate(hand_landmarks.landmark):
                    cx = landmrk.x * image_width
                    cy = landmrk.y * image_height
                    cz = landmrk.z * image_width * image_height

                    if cy < 600:  
                        robot.move_joints([-1.4, -0.2, 0.76, 1.9, -1.1, -0.3])

                mp.solutions.drawing_utils.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow("Cobotique", image)

        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
