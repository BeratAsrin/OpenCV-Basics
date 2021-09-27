import cv2 as cv 
import numpy as np

canvas = np.zeros((512,512,3), dtype= np.uint8) + 255 

cv.line(canvas, (50,50), (512,512), (0,0,255), thickness=2)
cv.line(canvas, (10,50), (200,512), (0,255,0), thickness=10)

cv.rectangle(canvas, (50,50), (100,100), (255,0,0), thickness=10)
cv.rectangle(canvas, (100,100), (200,200), (255,255,0), thickness=-1)

cv.circle(canvas, (400,400), 50, (255,0,255), thickness=2)
cv.circle(canvas, (250,50), 20, (255,0,255), thickness=-1)

cv.ellipse(canvas, (300,300), (80,150), 0, 90, 360, (0,0,0), thickness=-1)

cv.imshow("Canvas", canvas)
cv.waitKey(0)
cv.destroyAllWindows()
