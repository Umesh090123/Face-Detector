# importing opencv
import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('FaceDetection_frontalface_default.xml')

# To capture video from webcam. 
Cap = cv2.VideoCapture(0)
# To use a video file as input

while True:
    
    # Read the frame
    _, img = Cap.read()
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    # Draw the rectangle around each face
    for (X, Y, W, H) in faces:
        cv2.rectangle(img, (X, Y), (X + W, Y + H), (255, 0, 0), 2)
    
    # Display
    cv2.imshow('Face Detector', img)
    
    # Stop if escape key is pressed
    #cv2.imshow('Face Detector', img)
    k = cv2.waitKey(1)
    
    # wait for ESC key to exit
    if k == 27:   
        cv2.destroyAllWindows()
        break
    
    #wait for 's' key to save and exit
    elif k == ord('s'):                   
        cv2.imwrite('student.png', img)
        cv2.destroyAllWindows()
        break
        
# Release the VideoCapture object
Cap.release()
cv2.destroyAllWindows()