from flask import Flask, render_template, Response, request
import cv2
import mediapipe as mp

app = Flask(__name__)
def gen_frames():
    cap = cv2.VideoCapture(0)
    mp_hands = mp.solutions.hands
    with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.75) as hands:
        while True:
            success, frame = cap.read()
            if not success:
                break
            frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
            frame.flags.writeable = False
            results = hands.process(frame)
            frame.flags.writeable = True
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    cap.release()



