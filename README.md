# SecuCam

SecuCam is a security camera application with an OTP-based authentication system and motion detection. It integrates with Twilio for SMS alerts and plays an alarm sound upon detecting movement.

## Features
- **OTP-based authentication**: Sends an OTP via email and SMS for secure login.
- **Real-time face and body detection**: Uses OpenCV's Haar cascades for detecting motion.
- **Alarm trigger**: Plays an alarm sound when motion is detected.
- **SMS alerts**: Sends alerts via Twilio when unusual movement is detected.
- **Video recording**: Records and saves video upon detection.

## Requirements

Ensure you have the following installed before running the script:

- Python 3.x
- OpenCV (`cv2`)
- Tkinter (`tkinter`)
- Pygame (`pygame`)
- Twilio (`twilio`)
- Click (`click`)

You can install the dependencies using:
```sh
pip install opencv-python pygame twilio click
```

## Setup

1. **Twilio Credentials**: Replace the placeholders in `credentials.py` with your Twilio credentials:
   ```python
   account_sid = "your_account_sid"
   auth_token = "your_auth_token"
   my_cell = "your_phone_number"
   my_twilio = "your_twilio_number"
   ```

2. **Email Credentials**: Ensure you update your Gmail credentials in `gui.py`:
   ```python
   s.login("your_email@gmail.com", "your_app_password")
   ```
   > Note: Using app passwords is recommended instead of your main password for security reasons.

## Running the Application

Run the GUI application using:
```sh
python gui.py
```

## Usage

1. Launch the application.
2. Enter the OTP received via email and SMS.
3. Upon successful verification, the camera feed starts.
4. If movement is detected:
   - An alarm is triggered.
   - An alert SMS is sent.
   - Video recording starts.
5. The recording stops after no movement is detected for a set duration.
6. Press `q` to exit the camera feed.

## File Structure
```
CAPISTAN/
│── Main/
│   ├── alarm.py
│   ├── alert.wav
│   ├── camera.py
│   ├── gui.py
│   ├── gui.spec
│   ├── haarcascade_frontalface_default.xml
│   ├── haarcascade_fullbody.xml
│   ├── indus_alarm.mp3
│   ├── Main.py
│   ├── sampleFiles/
│   └── indus_alarm.mp3
```

## Future Improvements
- Enhance security by encrypting OTPs and credentials.
- Implement a cloud storage option for video recordings.
- Introduce face recognition for improved security.

## License
This project is open-source and available under the MIT License.

---
Developed for enhanced security monitoring.

