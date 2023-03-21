import cvzone
import mediapipe as mp
import HandTrackingModule as htm
import cv2
import time
import serial
import struct

cap = cv2.VideoCapture(0)

def _map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
arduino = serial.Serial('/dev/cu.usbmodem14201', 9600)
detector = htm.handDetector(detectionCon=0.75)

pTime = 0
cTime = 0
cx = 0
cy = 0
x = 180
y = 180
z = 180
posz = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        if lmList[12][2] < lmList[10][2]:
            posz = 1
        else:
            posz = 0

    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                h,w,c = img.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            posx = _map(cx, 550 , 1100, 90, 180)
            posy = _map(cy, 330, 650, 90, 180)

            posx = max(min(posx, 255), 0)
            posy = max(min(posy, 255), 0)
            posz = max(min(posz, 1), 0)

            positions_bytes = struct.pack('BBB', posx, posy, posz)
            arduino.write(positions_bytes)

            if posx < 0:
                posx = 0
            elif posx > 180:
                posx = 180

            if posy < 0:
                posy = 0
            elif posy > 180:
                posy = 180

            print(12, posx, posy, posz)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
