import cv2
import imutils

# Open the webcam
cam = cv2.VideoCapture(0)

firstFrame = None
area = 500

while True:
    # Read the frame from the camera
    ret, img = cam.read()
    if not ret:
        break
    
    text = "Normal"

    # Resize the frame
    img = imutils.resize(img, width=500)

    # Convert to grayscale
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0)

    # Capture the first frame
    if firstFrame is None:
        firstFrame = gaussianImg
        continue

    # Calculate the absolute difference between the first frame and the current frame
    imgDiff = cv2.absdiff(firstFrame, gaussianImg)

    # Threshold the difference image
    threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]

    # Dilate the thresholded image
    threshImg = cv2.dilate(threshImg, None, iterations=2)

    # Find contours in the thresholded image
    cnts = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        # Ignore small contours
        if cv2.contourArea(c) < area:
            continue
        # Compute the bounding box for the contour
        (x, y, w, h) = cv2.boundingRect(c)
        # Draw the bounding box on the frame
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Moving Object Detected"

    print(text)
    # Display the text on the frame
    cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    # Show the frame
    cv2.imshow("cameraFeed", img)

    # Exit the loop if 'q' is pressed
    key = cv2.waitKey(10)
    #print(key)
    if key == ord("q"):
        break

# Release the webcam and close windows
cam.release()
cv2.destroyAllWindows()
