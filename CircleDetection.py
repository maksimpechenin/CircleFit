import cv2 as cv
import numpy as np
import math

img = cv.imread('Resourse/photo1638458075-5.jpeg')
imgGrey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
imgCanny = cv.Canny(imgGrey,150,200)
ret,thresh = cv.threshold(imgCanny,127,255, 3)
contours,hierarchy = cv.findContours(thresh, 1, 2)
max = cv.contourArea(contours[0])
cnt = contours[0]
for i in range(len(contours)):
    if cv.contourArea(contours[i]) > max:
        cnt = contours[i]
        max = cv.contourArea(cnt)
area = max
print(str(area))

(x,y),radius = cv.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
circlArea = math.pi*(radius)**2
print(str(circlArea))
print(f'Вы нарисовали окружность на :{100*area/circlArea:.2f} точно')
circl = cv.circle(img,center,radius,(0,255,0),2)



cv.imshow('circl',circl)
cv.imshow('thresh',thresh)

cv.waitKey(0)
cv.destroyAllWindows()