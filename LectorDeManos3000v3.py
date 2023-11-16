import cv2
import RPi.GPIO as GPIO
from time import sleep
from HandTrackingModule import HandDetector
detector=HandDetector(detectionCon=0.5,maxHands=1)


# Pins para cada motor
Motor1A = 24
Motor1B = 23
Motor1E = 25
Motor1F = 16

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)              # GPIO Numbering
    GPIO.setup(Motor1A,GPIO.OUT)  # Salidas de los pines
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)
    GPIO.setup(Motor1F, GPIO.OUT)

def forwards():
    #Avance
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)
    GPIO.output(Motor1F,GPIO.HIGH)

    print("Avanzando")
 

def backwards():
    #Retroceso
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)
    print("Retrocediendo")
 

def fstop():
    #DetencionDelAvance
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1F, GPIO.LOW)
    print("fStop")
def bstop():
    #bDetencionDeLaReversa
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.LOW)
    print("bStop")
    
def destroy():  
    print("GPIO.cleanup()")


cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    hands,frame=detector.findHands(frame)
    if hands:
        setup()
        hands1=hands[0]
        forwards()
        print("HayManito")

    else:
        print("NoHayMano")
        setup()
        fstop()
            
    frame=cv2.imshow("AAAAAAAAAAAAAAAAAAAAAAAAAA",frame)
   
    if cv2.waitKey(0)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()
