import random
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time

cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)
detector = HandDetector(maxHands=1, detectionCon=0.5)
timer = 0
stateResult = False
startGame = False
scores = [0, 0]
imgAI = None

while True:
   imgBG = cv2.imread("Resources/BG.png")
   success, img = cap.read()
   
   imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
   imgScaled = imgScaled[:, 80:480]
   hands, img = detector.findHands(imgScaled)
   
   if startGame:
       if stateResult is False:
           timer = time.time() - initialTime
           cv2.putText(imgBG, str(int(timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)
           
           if timer > 3:
               stateResult = True
               timer = 0
               
               if hands:
                   playerMove = None
                   hand = hands[0]
                   fingers = detector.fingersUp(hand)
                   print("Jari terdeteksi:", fingers)
                   
                   if fingers:
                       if fingers == [0, 0, 0, 0, 0]:
                           playerMove = 1
                           print("Batu terdeteksi")
                       if fingers == [1, 1, 1, 1, 1]:
                           playerMove = 2
                           print("Kertas terdeteksi")
                       if fingers == [0, 1, 1, 0, 0]:
                           playerMove = 3
                           print("Gunting terdeteksi")
                           
                       print(f"Gerakan pemain: {playerMove}")
                       randomNumber = random.randint(1, 3)
                       print(f"Gerakan AI: {randomNumber}")
                       
                       imgpath = f'Resources/{randomNumber}.png'
                       print(f"Muat gambar: {imgpath}")
                       imgAI = cv2.imread(imgpath, cv2.IMREAD_UNCHANGED)
                       
                       if imgAI is None:
                           print(f"Gagal memuat gambar AI: {imgpath}")
                       else:
                           print("Gambar AI berhasil dimuat")
                           imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))
                           
                           if (playerMove == 1 and randomNumber == 3) or \
                              (playerMove == 2 and randomNumber == 1) or \
                              (playerMove == 3 and randomNumber == 2):
                               scores[1] += 1
                               print("Pemain menang!")
                               
                           if (playerMove == 3 and randomNumber == 1) or \
                              (playerMove == 1 and randomNumber == 2) or \
                              (playerMove == 2 and randomNumber == 3):
                               scores[0] += 1
                               print("AI menang!")
                               
   imgBG[234:654, 795:1195] = imgScaled
   
   if stateResult and imgAI is not None:
       imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))
       
   cv2.putText(imgBG, str(scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
   cv2.putText(imgBG, str(scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
   
   cv2.imshow("Latar Belakang", imgBG)
   key = cv2.waitKey(1)
   
   if key == ord('s'): # untuk memulai game
       startGame = True
       initialTime = time.time()
       stateResult = False
   elif key == ord('q'): # untuk keluar dari game
       break

cap.release()
cv2.destroyAllWindows()
