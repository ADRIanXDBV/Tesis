import cv2

def condicionalesLetras(dedos, frame):
    font = cv2.FONT_HERSHEY_SIMPLEX
    if dedos == [1, 1, 0, 0, 0, 0]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
            cv2.putText(frame, 'A', (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
            print("A")

    if dedos == [0, 0, 0, 0, 0, 0]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'E', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("E")

    if dedos == [0, 0, 1, 0, 0, 0]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'I', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("I")

    if dedos == [1, 0, 1, 0, 0, 0]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'O', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("O")

    if dedos == [0, 0, 1, 0, 0, 1]:
            cv2.rectangle(frame, (0, 0), (100, 100), (255, 255,255), -1)
            cv2.putText(frame, 'U', (20, 80), font, 3, (0,0,0),2,cv2.LINE_AA)
            print("U")

    return dedos