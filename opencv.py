import cv2
import mediapipe as mp
import numpy as np
import time

def switch(argument):
    if argument == 1:
        videoCap()
    elif argument == 2:
        detectFinger()
    elif argument == 3:
        detectPos()
    elif argument == 4:
        detectSym()

def Menu():
    while True:
        print("--- Menu ---")
        print("1.Test Camera\n2.Detect Finger\n3.Detect Peosition of Finger\n4.Detect Symbol\n5.Exit")
        ans = int(input("Select: "))
        switch(ans)
        if ans == 5:
            print("Goodbye")
            break
        elif ans > 5:
            print("Please enter in 1 - 5")

def videoCap():
    cap = cv2.VideoCapture(0)
    while True:
        check, frame = cap.read()
        cv2.putText(frame, "Press E to close", (200, 470), cv2.FONT_HERSHEY_PLAIN, 2, (57, 130, 247), 3)
        if check == True:
            cv2.imshow("Video", frame)
            if cv2.waitKey(1) & 0xFF == ord('e'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

def detectFinger():
    cap = cv2.VideoCapture(0)
    
    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils
    
    while True:
        check, frame = cap.read()
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        print(results.multi_hand_landmarks)
        
        cv2.putText(frame, "Press E to close", (200, 470), cv2.FONT_HERSHEY_PLAIN, 2, (57, 130, 247), 3)
        
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
        
        if check == True:
            cv2.imshow("Video", frame)
            if cv2.waitKey(1) & 0xFF == ord('e'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

def detectPos():
    cap = cv2.VideoCapture(0)
    
    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils
    
    fps = 0
    frame_count = 0
    start_time = time.time()
    
    while True:
        frame_count += 1
        elapsed_time = time.time() - start_time
        if elapsed_time != 0:
            fps = frame_count / elapsed_time
        
        check, frame = cap.read()
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        # * print(results.multi_hand_landmarks)
        
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    print(id, cx, cy)
                
                mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
        
        cv2.putText(frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0 ,255), 3)
        cv2.putText(frame, "Press E to close", (200, 470), cv2.FONT_HERSHEY_PLAIN, 2, (57, 130, 247), 3)
        
        if check == True:
            cv2.imshow("Video", frame)
            if cv2.waitKey(1) & 0xFF == ord('e'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

def detectSym():
    Nfing = 5
    cap = cv2.VideoCapture(0)
    
    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils
    
    while True:
        check, frame = cap.read()
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        # * print(results.multi_hand_landmarks)
        
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    if id == 4:
                        id4 = int(id)
                        cx4 = cx
                    elif id == 3:
                        id3 = int(id)
                        cx3 = cx
                if cx4 > cx3:
                    Nfing = 4
                else:
                    Nfing = 5
                
                mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
        
        cv2.putText(frame, str(int(Nfing)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0 ,255), 3)
        cv2.putText(frame, "Press E to close", (200, 470), cv2.FONT_HERSHEY_PLAIN, 2, (57, 130, 247), 3)
        
        if check == True:
            cv2.imshow("Video", frame)
            if cv2.waitKey(1) & 0xFF == ord('e'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

def detectHand():
    cap = cv2.VideoCapture(0)
    
    arr = np.zeros((21, 2))
    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils
    while cap.isOpened():
        finger = []
        check, frame = cap.read()
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    arr[id] = [cx, cy]
                mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
                if arr[9, 1] < arr[0, 1]:
                    if (arr[5, 0] >= arr[9, 0]):
                        if (arr[4, 0] > arr[5, 0]) and (arr[4, 1] < arr[3, 1]):
                            finger.append("HR")
                        for i in range(8, 21, 4):
                            if (arr[i, 1] < arr[i - 2, 1]):
                                finger.append(f"{int(i/4) - 1}R")
                    else:
                        if (arr[4, 0] < arr[5, 0]) and (arr[4, 1] < arr[3, 1]):
                            finger.append("HL")
                        for i in range(8, 21, 4):
                            if (arr[i, 1] < arr[i - 2, 1]):
                                finger.append(f"{int(i/4) - 1}L")
                else:
                    if (arr[5, 0] <= arr[9, 0]):
                        if (arr[4, 0] > arr[5, 0]) and (arr[4, 1] > arr[3, 1]):
                            finger.append("HR")
                        for i in range(8, 21, 4):
                            if (arr[i, 1] > arr[i - 2, 1]):
                                finger.append(f"{int(i/4) - 1}R")
                    else:
                        if (arr[4, 0] < arr[5, 0]) and (arr[4, 1] > arr[3, 1]):
                            finger.append("HL")
                        for i in range(8, 21, 4):
                            if (arr[i, 1] > arr[i - 2, 1]):
                                finger.append(f"{int(i/4) - 1}L")
        
        cv2.putText(frame, "Finger : ", (10, 70), cv2.FONT_HERSHEY_PLAIN, 1, (218, 224, 159), 2)
        cv2.putText(frame, f"Finger Count: ", (10, 40), cv2.FONT_HERSHEY_PLAIN, 2, (218, 224, 159), 3)
        if len(finger) != 0:
            cv2.putText(frame, f"{' '.join(finger)}", (85, 70), cv2.FONT_HERSHEY_PLAIN, 1, (47, 209, 29), 2)
            cv2.putText(frame, f"{str(len(finger))}", (245, 40), cv2.FONT_HERSHEY_PLAIN, 2, (47, 209, 29), 3)
        else:
            cv2.putText(frame, "None", (85, 70), cv2.FONT_HERSHEY_PLAIN, 1, (57, 130, 247), 2)
            cv2.putText(frame, f"{str(len(finger))}", (245, 40), cv2.FONT_HERSHEY_PLAIN, 2, (57, 130, 247), 3)
        if check == True:
            cv2.imshow("Video", frame)
            if cv2.waitKey(1) & 0xFF == ord('e'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()