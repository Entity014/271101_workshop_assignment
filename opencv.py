import cv2
import mediapipe as mp
import numpy as np
import time

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
        check, frame = cap.read()
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    arr[id] = [cx, cy]
                if arr[0, 1] > arr[8, 1]:
                    if arr[4, 0] > arr[17, 0]:
                        if arr[0, 0] < arr[5, 0]:
                            if arr[8, 1] < arr[5, 1]:
                                print("นิ้วชี้ขวา")
                            if arr[12, 1] < arr[9, 1]:
                                print("นิ้วกลางขวา")
                            if arr[16, 1] < arr[13, 1]:
                                print("นิ้วนางขวา")
                            if arr[20, 1] < arr[17, 1]:
                                print("นิ้วก้อยขวา")
                        if (arr[4, 0] > arr[8, 0]) and (arr[4, 1] < arr[2, 1]):
                            print("นิ้วโป้งขวา")
                    else:
                        if arr[0, 0] > arr[5, 0]:
                            if arr[8, 1] < arr[5, 1]:
                                print("นิ้วชี้ซ้าย")
                            if arr[12, 1] < arr[9, 1]:
                                print("นิ้วกลางซ้าย")
                            if arr[16, 1] < arr[13, 1]:
                                print("นิ้วนางซ้าย")
                            if arr[20, 1] < arr[17, 1]:
                                print("นิ้วก้อยซ้าย")
                        if (arr[4, 0] < arr[8, 0]) and (arr[4, 1] < arr[2, 1]):
                            print("นิ้วโป้งซ้าย")
                elif arr[0, 1] < arr[8, 1]:
                    if arr[4, 0] < arr[20, 0]:
                        if arr[0, 0] < arr[5, 0]:
                            if arr[8, 1] > arr[5, 1]:
                                print("นิ้วชี้ขวา")
                            if arr[12, 1] > arr[9, 1]:
                                print("นิ้วกลางขวา")
                            if arr[16, 1] > arr[13, 1]:
                                print("นิ้วนางขวา")
                            if arr[20, 1] > arr[17, 1]:
                                print("นิ้วก้อยขวา")
                        if (arr[4, 0] > arr[8, 0]) and (arr[4, 1] > arr[2, 1]):
                            print("นิ้วโป้งขวา")
                    else:
                        if arr[0, 0] > arr[5, 0]:
                            if arr[8, 1] < arr[5, 1]:
                                print("นิ้วชี้ซ้าย")
                            if arr[12, 1] < arr[9, 1]:
                                print("นิ้วกลางซ้าย")
                            if arr[16, 1] < arr[13, 1]:
                                print("นิ้วนางซ้าย")
                            if arr[20, 1] < arr[17, 1]:
                                print("นิ้วก้อยซ้าย")
                        if (arr[4, 0] > arr[8, 0]) and (arr[4, 1] < arr[2, 1]):
                            print("นิ้วโป้งซ้าย")
                mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
        
        if check == True:
            cv2.imshow("Video", frame)
            if cv2.waitKey(1) & 0xFF == ord('e'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()