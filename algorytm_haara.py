import numpy as np
import cv2 as cv
import datetime
import time 
start = time.time()
now = datetime.datetime.now()
print("Obecny czas : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))
car_cascade = cv.CascadeClassifier('cars.xml')
img = cv.imread('vectra.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cars = car_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in cars:
  cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
  roi_gray = gray[y:y+h, x:x+w]
  roi_color = img[y:y+h, x:x+w]
end = time.time()
execution_time = (end - start)
print(f"Czas rozpoznania obiektu {execution_time}")
cv.imshow('Car recognition Haar method',img)
cv.waitKey(0)
cv.destroyAllWindows()
