from facial_emotion_recognition import EmotionRecognition
import cv2
#happy,sad,anger,fear,neutral,suprise
er=EmotionRecognition(device='cpu')
cam=cv2.VideoCapture(0)

while True:
    sucess,frame=cam.read()
    frame=er.recognise_emotion(frame,return_type='BGR')
    #check the emotion inside the frame
    #BGR-color img
    cv2.imshow("Frame",frame)
    key=cv2.waitKey(1)
    if key==27: #esc key
        break
cam.release()
cv2.destroyAllWindows()
