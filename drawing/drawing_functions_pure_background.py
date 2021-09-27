import cv2, numpy

canvas = numpy.zeros((512,512,3), dtype=numpy.uint8) + 255 # white background (x index ,y index , rgb color code)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()