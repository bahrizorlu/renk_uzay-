#https://pysource.com/2021/10/19/simple-color-recognition-with-opencv-and-python/
import cv2
import serial
import time
arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)

cap = cv2.VideoCapture(0)  # 0 olarak değiştirildi
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = int(width / 2)
    cy = int(height / 2)

    # Pick pixel value
    pixel_center = hsv_frame[cy, cx]
    hue_value = pixel_center[0]

    color = "Undefined"
    if hue_value < 10:
        color = "KIRMIZI"
        num = '1'
        write_read(num)
        print(num)
   
    
        
    elif hue_value < 88:
        color = "YEŞİL"
        num='2'
        print(num)
        write_read(num)
        
    elif hue_value < 20:
        color = "MAVi"
        num='3'
        write_read(num)
        print(num)
      
   
        
    else:
        color = "KIRMIZI"
        num='1'
        write_read(num)
        print(num)
        

    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

    cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
    cv2.putText(frame, color, (cx - 200, 100), 0, 3, (b, g, r), 5)
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
