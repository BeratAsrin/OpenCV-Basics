import cv2

# cap = cv2.VideoCapture("videos/video.mp4") # read video from file
cap = cv2.VideoCapture(0) # read video from camera, 0 stands for camera

while True: # read each frame of video
    ret, frame = cap.read() # ret gets booleand value true or false, frame gets the matrix of each frame
    if ret == 0: # if ret is false then break the video
        break
    cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
    cv2.imshow("Video", frame) # shows the video
    cv2.waitKey(10) # each frame waits on the screen for ... ms
    if cv2.getWindowProperty('Video', cv2.WND_PROP_VISIBLE) < 1: # if X on window is pressed
        break

cap.release()