import cv2
import mediapipe as mp
from mediapipe.python.solutions import hands, drawing_utils
import pyautogui
import time

cam = cv2.VideoCapture(0)

# Reduce resolution for speed
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Hand detection
mp_hands = hands

Hands_det = mp_hands.Hands(max_num_hands=1)

# Drawing utils
draw_utils = drawing_utils

# Initial values
x1 = y1 = x2 = y2 = 0

# Delay controller
last_action = time.time()

while True:

    ret, frame = cam.read()

    if not ret:
        break

    frame_height, frame_width, _ = frame.shape

    # Convert BGR -> RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Hand processing
    output = Hands_det.process(rgb)

    detected_hands = output.multi_hand_landmarks  # type: ignore

    if detected_hands:

        for hand in detected_hands:

            # Draw landmarks
            draw_utils.draw_landmarks(frame, hand)

            landmarks = hand.landmark

            for id, landmark in enumerate(landmarks):

                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                # Index fingertip
                if id == 8:

                    x1 = x
                    y1 = y

                    cv2.circle(frame,(x1, y1),8,(0, 255, 255),-1)

                # Thumb tip
                if id == 4:

                    x2 = x
                    y2 = y

                    cv2.circle(frame,(x2, y2),8,(255, 0, 255),-1)

            # Distance calculation
            dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

            # Draw line
            cv2.line(frame,(x1, y1),(x2, y2),(0, 255, 0),5)

            # Show distance
            cv2.putText(frame,f"Distance: {int(dist)}",(50, 50),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 0, 255),2)

            # Delay action
            if time.time() - last_action > 0.01:

                if dist > 80:

                    pyautogui.press('volumeup')

                else:

                    pyautogui.press('volumedown')

                last_action = time.time()

    cv2.imshow("Hand Volume Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()