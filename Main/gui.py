


import datetime
import math
import random
import smtplib
import time
from tkinter import *
from winsound import SND_ASYNC, SND_FILENAME, PlaySound
from pygame import mixer

from click import command
import cv2
from Main import *
from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio


class Window:
    def __init__(self,win):
        self.sendchkotp()
        
    def sendchkotp(self):
        self.welcometxt=Label(window,text="Welcome to SecuCam",anchor=CENTER, font=("Arial", 20))
        self.welcometxt.place(x=150,y=50)
        self.otptxt=Label(window,text="Enter OTP:",anchor=CENTER)
        self.otptxt.place(x=150,y=100)
        digits="0123456789"
        OTP=""


        for i in range(6):
            OTP+=digits[math.floor(random.random()*10)]
        otp = OTP + " is your OTP"

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("secucam11@gmail.com", "wotwgfipxsznioit")

        

        #sending sms otp
        client = Client(account_sid, auth_token)
        my_msg = "\nYour one-time password for SecuCam is " + OTP + " \nPlease do NOT share it with anybody."
        message = client.messages.create(to=my_cell, from_=my_twilio,body=my_msg)
        

        
        self.enterotp=Entry(window)
        self.enterotp.place(x=220,y=100)
        
        self.lbl1=Label(window)
        self.lbl1.place(x=200,y=200)
                #acceptbtn
        
        def acceptbtn():
            a = self.enterotp.get()
            if a == OTP:
                self.lbl1['text']="Verified"
                #run the main program only if the otp is correct
                cam()
            else:
                self.lbl1['text']="Please Check entered OTP"
    
        self.accept=Button(window,text="Verify",anchor=CENTER,command=acceptbtn)
        self.accept.place(x=230,y=150)
        def cam():
        #accessing the webcam and viewing it in python
            cap = cv2.VideoCapture(0) #if have multiple capture devices change the "0"

            face_cascade = cv2.CascadeClassifier(
                cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
            body_cascade = cv2.CascadeClassifier(
                cv2.data.haarcascades + "haarcascade_fullbody.xml")

            detection = False
            detection_stopped_time = None
            timer_started = False
            SECONDS_TO_RECORD_AFTER_DETECTION = 5

            frame_size = (int(cap.get(3)), int(cap.get(4)))
            fourcc = cv2.VideoWriter_fourcc(*"mp4v")

            #we are reading one frame at a time and display that on the screen
            while True:
                _, frame = cap.read()

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                bodies = face_cascade.detectMultiScale(gray, 1.3, 5)

                if len(faces) + len(bodies) > 0:
                    if detection:
                        timer_started = False
                    else:
                        detection = True

                        #sms code pasted here
                        client = Client(account_sid, auth_token)
                        my_msg = "\nALERT! Unusual movement detected at your premises"
                        message = client.messages.create(to=my_cell, from_=my_twilio,body=my_msg)

                        #alarm code pasted here
                        mixer.init()
                        mixer.music.load('indus_alarm.mp3')
                        mixer.music.play()
                        

                        #continue main camera code
                        current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                        out = cv2.VideoWriter(
                            f"{current_time}.mp4", fourcc, 20, frame_size)
                        self.lbl1['text']="Started Recording"
                        self.lbl1.place(x=230, y=180)
                elif detection:
                    if timer_started:
                        if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                            detection = False
                            timer_started = False
                            out.release()
                            self.lbl1['text']="Stopped Recording"
                            self.lbl1.place(x=230, y=200)
                    else:
                        timer_started = True
                        detection_stopped_time = time.time()

                if detection:
                    out.write(frame)

                # for (x, y, width, height) in faces:
                #    cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)

                cv2.imshow("Camera", frame)

                if cv2.waitKey(1) == ord('q' or 'Q'):
                    break

            out.release()
            cap.release()
            cv2.destroyAllWindows()
    
    
    
    

    
    

window=Tk()
mywin=Window(window)
window.title('SecuCam')
window.geometry("500x500+10+20")
window.mainloop()


