## QR-Code-Bar-Scanner-project
Computer Vision project

##  Project Abstract
In this project, a QR code access control system is developed, using the Python OpenCV package to perform *real-time* QR code access control. By using a webcam, this project enables a user to continuously scan QR codes and decode them, as well as verify whether a user has been granted access.

When a user is authorized, they will see a *green* feedback overlay that says *ACCESS GRANTED. When a user is not authorized, they will see a **red* feedback overlay that says *ACCESS DENIED*. In addition, each student was assigned an individual QR code, which was created using the qrcode Python library.



##  Introduction
This project demonstrates how to implement computer vision by *detecting and decoding QR codes* for an automated access control system. The technology can also be adapted for use in real-world applications such as access to facilities, attendance tracking, and digital ID verification.



##  Features
- Real-time scanning of QR codes using *OpenCV QRCodeDetector*
- Automatic detection and decoding of QR codes
- Automatically drawn bounding box around detected QR code
- Access verification based on a user's status on an authorized list
- User feedback via color-coded overlays
- Automatic generation of personal QR codes for students



##  Team Members
| Name  | Role                    |
| Shahad| Development and Testing  |
| Shoug | QR Code Generation and Documentation|
| Norah | Code Structuring and Report Writing|
| Jood  | Research and System Design|



##  Repository Structure

# /project root
-scanner.py — Primary functioning QR scanning system in real-time.
-generate_qr.py — Application for generating QR codes for students.
-README.md — Project documentation.
-requirements.txt — Required Python modules/packages.
-/qr_codes — Folder containing images of created/generated QR codes.

##  Requirements
1. opencv-python==4.8.1
2. numpy==1.24.3
3. Pillow==10.0.0
4. matplotlib==3.7.1
5. qrcode==7.4.2


To install everything use: pip install -r requirements.txt


##  How to run the project
### Run the QR Code Scanner
Ensure you are using a webcam.

To run the QR Code Scanner use: python scanner.py

## Controls

* The QR Code Scanner Window Opens
* Hold a QR Code in front of the camera.
* Press Q to quit.



### Generate Student QR Codes

To generate Student QR Codes use: python generate_qr.py


This will create:
1. Shoug_Althunayan.png
2. Shahad_alhamraa.png

These files will be saved to either your project folder or /qr_codes folder if you specified one.



##  Approach (Summary)
Use *OpenCV QRCodeDetector()* to detect and decode the QR Code.


The following occurs for each frame:
1. Detect the QR Code
2. Decode the code to retrieve the string.
3. Compare the string against an allowed list of users.
4. Draw the bounding box for the QR Code
5. Provide a decision whether access is granted or denied.


QR Codes were generated using the qrcode Python library.


##  Sample Output
If you scanned:

Scanned: Shoug Althunayan
Result: Access Allowed


##  Authorized Users
The following are the currently authorized users:
1. "Shoug Althunayan"
2. "Shahad alhamraa"
3. "COMPUTER VISION PROJECT"
4. "STUDENT ACCESS"

   ##  Suggestions for Future Work
- Add photo database with ID matching
- Add a logging system (time stamped and user identifying)
- Add facial recognition as a second authentication method
- Create a GUI using Tkinter or PyQt


## References:
- OpenCV Official Documentation - QRCodeDetector  
- Python qrcode library documentation  


 ## License
This is an educational project.
