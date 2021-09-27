import cv2

img = cv2.imread("images/image.jpg", cv2.IMREAD_GRAYSCALE) # read related image using grayscale filter

cv2.namedWindow("Image Frame", cv2.WINDOW_NORMAL) # create new frame
cv2.imshow("Image Frame", img) # place image into the frame

cv2.imwrite("images/image1.jpg", img) # save the image 

cv2.waitKey(0) # prevent closing
cv2.destroyAllWindows() # close all frames