import os
import sys
import math
import random
import smtplib
import time

from camera import *


from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

#main function
def main():
    digits="0123456789"
    OTP=""


    for i in range(6):
        OTP+=digits[math.floor(random.random()*10)]
    otp = OTP + " is your OTP"

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("secucam11@gmail.com", "wotwgfipxsznioit")

    print("\nWelcome to SecuCam Console")
    time.sleep(2)
    print("\n-------------------------------------------------")
    print("\nPlease verify your account")
    print("Warning! You have only one chance to enter the correct OTP")
    print("\n-------------------------------------------------")
    time.sleep(3)


    #getting the email-id of the owner
    emailid = input("\nEnter your email: ")
    s.sendmail('&&&&&&&&&&&',emailid,otp)
    time.sleep(2)
    

    #sending sms otp
    client = Client(account_sid, auth_token)
    my_msg = "\nYour one-time password for SecuCam is " + OTP + " \nPlease do NOT share it with anybody."
    message = client.messages.create(to=my_cell, from_=my_twilio,body=my_msg)
    print("\nAn otp has been sent on your registered mobile number and email id.")
    

    a = input("\nEnter Your OTP >>: ")
    if a == OTP:
        print("Verified!")
        time.sleep(2)
        print('\nChecking for cameras...')
        time.sleep(4)
        print('\nRunning security checks...')
        time.sleep(4)
        print('\nGettings things ready..')
        time.sleep(2)
        print('\nSecuCam is starting.')
        

        #run the main program only if the otp is correct
        cam()
    else:
        print("Please Check your OTP again")
        
