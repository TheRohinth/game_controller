import cv2
import time
import track_hand as th
import game_controls as gc

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = th.handDetector()
x = y = w = h = diff = -1
while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=False)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) > 0:
        diff = lmList[4][2]-lmList[3][2]
        if diff > 20:
            #print("down",diff)
            gc.hold_down()
        elif diff < -20:
            #print("up",diff)
            gc.hold_up()
        if (lmList[4][1] <= w//3 and lmList[4][2] <= h//3) or (lmList[4][1] >= w-w//3 and lmList[4][2] >= h-h//3):
            gc.hold_left()
        elif (lmList[4][1] >= w-w//3 and lmList[4][2] <= h//3) or (lmList[4][1] <= w//3 and lmList[4][2] >= h-h//3):
            gc.hold_right()
        elif (lmList[4][1] <= w//2 and lmList[4][2] <= h//2) or (lmList[4][1] >= w-w//2 and lmList[4][2] >= h-h//2):
            gc.release_l_f()

    x, y, w, h = cv2.getWindowImageRect('img')
    if(w>0):
        img = cv2.circle(img, (w//4, h//4), 35, (0, 0, 255), 2)
        img = cv2.circle(img, (w-w//4, h//4), 35, (0, 0, 255), 2)
        img = cv2.circle(img, (w//4, h-h//4), 35, (0, 0, 255), 2)
        img = cv2.circle(img, (w-w//4, h-h//4), 35, (0, 0, 255), 2)
    cv2.imshow("img", img)

    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break
cv2.destroyAllWindows()
print("Thank you")