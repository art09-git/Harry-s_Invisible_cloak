import cv2 # opencv for image processing
import numpy as np # numerical library for image handling

capture = cv2.VideoCapture(0) # capturing video from webcam
background = cv2.imread('background.jpg') # reading the background image
while(capture.isOpened()):
    ret, frame = capture.read() # reading from webcam
    if ret == True:
        # converting the color space from BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # generating mask to detect red color
        lower_red = np.array([0,120,70])
        upper_red = np.array([10,255,255])
        mask1 = cv2.inRange(hsv, lower_red, upper_red)

        lower_red = np.array([170,120,70])
        upper_red = np.array([180,255,255])
        mask2 = cv2.inRange(hsv, lower_red, upper_red)

        #generating the final mask to detect red color
        mask1 = mask1 + mask2

        # refining the mask (removing noise)
        mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
        mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3,3),np.uint8))

        # creating an inverted mask to segment out the red color from the frame
        mask2 = cv2.bitwise_not(mask1)

        # segmenting the red color part out of the frame using bitwise and with the inverted mask
        res1 = cv2.bitwise_and(frame, frame, mask=mask2)

        # creating image showing static background frame pixels only for the masked region
        res2 = cv2.bitwise_and(background, background, mask=mask1)

        # generating the final output by merging res1 and res2
        final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
        
        cv2.imshow('Invisible Cloak', final_output) # displaying the output to the user

        if cv2.waitKey(5) == ord('q'): # wait for 'q' key to stop
            break
capture.release()
cv2.destroyAllWindows() # closing all the windows opened by opencv