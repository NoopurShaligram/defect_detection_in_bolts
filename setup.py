import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray_frame, 80,255, cv2.THRESH_BINARY_INV)
    
    #detect
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x,y) , (x+w, y+h), (0,255,0), 3)
    #belt = frame[y1:y2 , x1:x2]
    #x1 = , y1= top left
    #x2= , y2= bottom right
    cv2.imshow("frame ", frame)
    cv2.imshow("frame gray", gray_frame)
    cv2.imshow("threshold", threshold)
    #cv2.imshow("belt", belt)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
