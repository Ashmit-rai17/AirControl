import cv2 as cv
import pyautogui
#img = cv.imread('balckdog.jpg')
#cv.imshow('Dog' , img)
#cv.waitKey(0)
capture = cv.VideoCapture(0)
screen_width, screen_height = pyautogui.size()
while True:
    isTrue , frame = capture.read()
    gray = cv.cvtColor(frame , cv.COLOR_BGR2GRAY)
    _, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
    edges = cv.Canny(gray , 100 , 200)
    edges_res = cv.resize(edges , (screen_width , screen_height))
    
    cv.imshow('Video' , frame)
    cv.imshow('Grayscaled' , gray)
    #cv.imshow('Threshold' , thresh)
    cv.imshow('Edge detection', edges_res)
   


    if cv.waitKey(20) & 0xFF ==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
