import cv2
import mediapipe as mp

class Hand_Controller:
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.hand_x = 0.4

    def cam_available(self) -> bool:
        return self.capture.isOpened()
    
    def close_cam(self) -> None:
        self.capture.release()
        cv2.destroyAllWindows()
    
    def get_hand_position(self) -> float:
        return self.hand_x
    
    def detect_hand(self) -> None:
        frame_loaded, frame = self.capture.read()

        if not frame_loaded:
            return

        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.hand_x = hand_landmarks.landmark[self.mp_hands.HandLandmark.WRIST].x


