from Assets.scripts.settings import *
from Assets.scripts.testApplicattion import Aplication
import threading
import cv2
from deepface import DeepFace
TF_ENABLE_ONEDNN_OPTS=0
faceMatch = False
refImg = cv2.imread("Assets/sprites/me.png")

#Face Match not working, it says no match and does not continue to match 
def checkFace(frame):
    global faceMatch

    try:
        if DeepFace.verify(frame,refImg.copy())["verified"]:
            faceMatch = True
        else:
            faceMatch = False
    except ValueError as e:
        print("testing error")
        faceMatch = False
        
def main():
    
    # cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
    # counter = 0
    # while True:
    #     ret, frame = cap.read()
    #     if ret:
    #         if counter % 10 == 0:
    #             try:
    #                 threading.thread(target=checkFace,args=(frame.copy(),)).start()
    #             except:
    #                 pass
    #             counter +=1
    #             if faceMatch:
    #                 break
    #             else:
    #                 cv2.putText(frame,'no match',(20,450),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),5)
    #         cv2.imshow("exam id",frame)
    #     key = cv2.waitKey(1)
    #     if key == ord('q'):
    #         cv2.destroyAllWindows()
    #         quit()
                
    # cv2.destroyAllWindows()
    
    filetypes = (
        ('text files','*.txt'),
        ('All files','*.*'))
    testFile = fd.askopenfilename(title="Select Your Test",
                              initialdir="C:\\Users\\dawson.simmons\\Desktop\\Python23-24\\Term3\\TestProgram\\Assets\\TestFiles\\",
                              filetypes=filetypes)
    textToSpeach = pyttsx3.init()
    #textToSpeach.say("You have the right to remain silent. Anything you say can and will be used against you in a court of law. You have the right to speak to an attorney, and to have an attorney present during any questioning. If you cannot afford a lawyer, one will be provided for you.")
    #textToSpeach.runAndWait()
    root = Tk()
    app = Aplication(root,testFile)
    root.mainloop()

if __name__ == '__main__':
    main()
    
