import cv2

alg = "haarcascade_frontalface_default.xml"

haar_cascade = cv2.CascadeClassifier(alg) #loading algorithm

video_path=".mp4"
cam = cv2.VideoCapture(video_path) #Cam id initialization

#img
#video_path"pic.jpg"
#img=cv2.imread(video_path)
while True:
    ret,img=cam.read()
    

    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Converting clr img to gray

    face = haar_cascade.detectMultiScale(grayImg,1.3,4) #getting coordinates

    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("FaceDetection",img)

    key=cv2.waitKey(10)

    if key == 27: #esc key value is 27
        break

cam.release()
cv2.destroyAllWindows()

