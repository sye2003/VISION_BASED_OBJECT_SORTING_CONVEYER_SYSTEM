import cv2
import numpy as np
import serial
import time

# Change to your Arduino COM port
ser = serial.Serial('COM3', 9600)
time.sleep(2)  # Wait for serial connection to establish

cap = cv2.VideoCapture(0)

# To avoid spamming same command
last_sent = ""
cooldown = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame. Exiting...")
        break

    frame = cv2.resize(frame, (640, 480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define HSV ranges for colors
    color_ranges = {
        'Red':    [(0, 120, 70), (10, 255, 255), (170, 120, 70), (180, 255, 255)],
        'Green':  [(36, 100, 100), (86, 255, 255)],
        'Blue':   [(94, 80, 2), (126, 255, 255)],
        'Yellow': [(15, 100, 100), (35, 255, 255)],
    }

    for color, ranges in color_ranges.items():
        if color == 'Red':
            mask1 = cv2.inRange(hsv, np.array(ranges[0]), np.array(ranges[1]))
            mask2 = cv2.inRange(hsv, np.array(ranges[2]), np.array(ranges[3]))
            mask = mask1 + mask2
        else:
            mask = cv2.inRange(hsv, np.array(ranges[0]), np.array(ranges[1]))

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 1500:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
                cv2.putText(frame, color, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)

                # Send only if not just sent
                if time.time() - cooldown > 1.5 or last_sent != color:
                    command = color[0].encode()  # 'R', 'G', 'B', 'Y'
                    ser.write(command)
                    print(f"Sent to Arduino: {command}")
                    last_sent = color
                    cooldown = time.time()

    cv2.imshow("Color Sorter", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
ser.close()
cv2.destroyAllWindows()
