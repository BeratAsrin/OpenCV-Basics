import cv2 as cv
import numpy as np

import cv2 as cv 
import numpy as np

canvas = np.zeros((512,1000,3), dtype= np.uint8) + 255 

cv.putText(canvas, "Berat Asrin", (50,200), cv.FONT_HERSHEY_SIMPLEX, 4, (0,0,0), cv.LINE_AA)

cv.imshow("Canvas", canvas)
cv.waitKey(0)
cv.destroyAllWindows()
