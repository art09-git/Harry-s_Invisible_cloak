import cv2 # opencv for image processing
#creating a video capture object to capture the video through webcam
cap = cv2.VideoCapture(0) # this is my webcam

#getting the background image
while(cap.isOpened()):
    ret, frame = cap.read() #simply reading from the webcam
    if ret == True:
        cv2.imshow('frame',frame)
        if cv2.waitKey(5) == ord('q'):
            #save the background image
            cv2.imwrite('background.jpg',frame)
            break
cap.release()
cv2.destroyAllWindows()
#this code will capture the background image when we press 'q' and save it as background.jpg