## QR-Code-Bar-Scanner-project
Computer Vision project

##  Project Abstract
In this project, a QR code access control system is developed, using the Python OpenCV package to perform *real-time* QR code access control. By using a webcam, this project enables a user to continuously scan QR codes and decode them, as well as verify whether a user has been granted access.

When a user is authorized, they will see a *green* feedback overlay that says *ACCESS GRANTED. When a user is not authorized, they will see a **red* feedback overlay that says *ACCESS DENIED*. In addition, each student was assigned an individual QR code with their student ID, which was created using the qrcode Python library.



##  Introduction
This project demonstrates how to implement computer vision by *detecting and decoding QR codes* for an automated access control system. The technology can also be adapted for use in real-world applications such as access to facilities, attendance tracking, and digital ID verification.



##  Team Members
| Name  | Role                    |
| Shahad Hamraa | Development and documentation  |
| Shoug Althunayan | QR Code Generation and testing |
| Noura Alafaliq | Code Structuring and Report Writing |
| Jood Alghamdi | Research and System Design |



##  Features
- Real-time scanning of QR codes using *OpenCV QRCodeDetector*
- Automatic detection and decoding of QR codes
- Automatically drawn bounding box around detected QR code
- Access verification based on authorized student list
- User feedback via color-coded overlays
- Automatic generation of personal QR codes for students




##  Repository Structure

## project root
-access_scanner.py — Main QR scanning system.

-create_test_codes.py — QR code generator.

-README.md — Project documentation.

-requirements.txt — Required packages.

-*.png — Generated QR code files.

##  Requirements

Install these packages:

pip install opencv-python numpy qrcode
What each package does:

opencv-python - for webcam and QR code detection

numpy - for image processing

qrcode - for generating student QR codes

##  How to run the project

python create_test_codes.py
This will create:

202200662_Shoug_Althunayan.png
202100267_Shahad_Hamraa.png
202201633_Jood_Alghamdi.png
201900253_Noura_Alafaliq.png

### Run the QR Code Scanner
Ensure you are using a webcam.
python access_scanner.py

## Controls

* The QR Code Scanner Window Opens
* Hold a QR Code in front of the camera.
* Press Q to quit.


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

Scanned: 202200662 - Shoug Althunayan
Result: ACCESS GRANTED


##  Authorized Users
The following are the currently authorized users:

1. 202200662 - Shoug Althunayan"
2. 202100267 - Shahad Hamraa"
3. 202201633 - Jood Alghamdi"
4. 201900253 - Noura Alafaliq"

   ##  Suggestions for Future Work
- Add photo database with ID matching
- Add a logging system (time stamped and user identifying)
- Add facial recognition as a second authentication method



## References:
- OpenCV QRCodeDetector 
- Python qrcode library  


