import streamlit as st
import random
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time

def main():
    st.title("Permainan Batu Gunting Kertas")
    st.write("Tekan tombol **'Mulai Game'** untuk bermain dan gunakan kamera Anda.")
    st.write("Untuk keluar dari permainan, tekan tombol **'Stop Game'**.")
    
    start_game = st.button("Mulai Game")
    stop_game = st.button("Stop Game")
    
    if start_game:
        cap = cv2.VideoCapture(0)
        cap.set(3, 640)
        cap.set(4, 480)

        detector = HandDetector(maxHands=1, detectionCon=0.5)
        timer = 0
        stateResult = False
        scores = [0, 0]  # [AI, Player]
        imgAI = None
        initialTime = time.time()

        while True:
            success, img = cap.read()
            if not success:
                st.error("Kamera tidak terdeteksi. Pastikan kamera Anda aktif.")
                break

            imgBG = cv2.imread("Resources/BG.png")
            if imgBG is None:
                st.error("Gambar latar belakang tidak ditemukan. Pastikan file `Resources/BG.png` tersedia.")
                break

            imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
            imgScaled = imgScaled[:, 80:480]
            hands, img = detector.findHands(imgScaled)

            if stateResult is False:
                timer = time.time() - initialTime
                if timer > 3:
                    stateResult = True
                    timer = 0

                    if hands:
                        playerMove = None
                        hand = hands[0]
                        fingers = detector.fingersUp(hand)

                        if fingers == [0, 0, 0, 0, 0]:
                            playerMove = 1  # Batu
                        if fingers == [1, 1, 1, 1, 1]:
                            playerMove = 2  # Kertas
                        if fingers == [0, 1, 1, 0, 0]:
                            playerMove = 3  # Gunting

                        randomNumber = random.randint(1, 3)
                        imgAI = cv2.imread(f'Resources/{randomNumber}.png', cv2.IMREAD_UNCHANGED)
                        if imgAI is None:
                            st.error(f"Gagal memuat gambar AI: Resources/{randomNumber}.png")
                        else:
                            imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

                            # Logika menang/kalah
                            if (playerMove == 1 and randomNumber == 3) or \
                               (playerMove == 2 and randomNumber == 1) or \
                               (playerMove == 3 and randomNumber == 2):
                                scores[1] += 1
                                st.success("Pemain menang!")
                            elif (playerMove == 3 and randomNumber == 1) or \
                                 (playerMove == 1 and randomNumber == 2) or \
                                 (playerMove == 2 and randomNumber == 3):
                                scores[0] += 1
                                st.warning("AI menang!")

            cv2.putText(imgBG, str(scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
            cv2.putText(imgBG, str(scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)

            # Tampilkan hasil di Streamlit
            st.image(imgBG, channels="BGR")

            if stop_game:
                break

        cap.release()
        cv2.destroyAllWindows()

    elif stop_game:
        st.write("Permainan dihentikan. Tekan tombol **'Mulai Game'** untuk bermain lagi.")

if __name__ == "__main__":
    main()
