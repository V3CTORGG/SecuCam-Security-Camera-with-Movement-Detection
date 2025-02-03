import os
import math
import random
from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

def send_sms():
    digits="0123456789"
    OTP=""

    #generation of otp
    for i in range(6):
        OTP+=digits[math.floor(random.random()*10)]
    otp = OTP

    final_otp = otp

    # Find these values at https://twilio.com/user/account
    client = Client(account_sid, auth_token)

    my_msg = "Your one-time password for SecuCam is " + final_otp

    message = client.messages.create(to=my_cell, from_=my_twilio,
                                     body=my_msg)

send_sms()