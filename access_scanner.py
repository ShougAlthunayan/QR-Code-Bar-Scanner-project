import cv2
import numpy as np

#  authorized QR codes
authorized_codes = [
    'Shoug Althunayan', 
    'Shahad alhamraa',
    'COMPUTER VISION PROJECT',
    'STUDENT ACCESS'
]

# Initialize webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam")
else:
    print("Access Control System Started!")
    print("Authorized users: Shoug Althunayan, Shahad alhamraa")
    print("Press 'q' to quit")
    
    # Create QR detector
    qr_detector = cv2.QRCodeDetector()
    
    while True:
        success, img = cap.read()
        
        if not success:
            break
        
        # Detect QR code using OpenCV
        data, bbox, _ = qr_detector.detectAndDecode(img)
        
        if data:
            print(f"Scanned: {data}")
            
            # Draw bounding box
            if bbox is not None:
                bbox = bbox.astype(int)
                n = len(bbox)
                for i in range(n):
                    cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % n][0]), (255, 0, 255), 3)
            
            # Check access
            if data in authorized_codes:
                access_text = "ACCESS GRANTED"
                color = (0, 255, 0)  # Green
            else:
                access_text = "ACCESS DENIED"
                color = (0, 0, 255)  # Red
            
            #  access result
            cv2.putText(img, data, (10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.9, (32, 128, 255), 2)
            cv2.putText(img, access_text, (10, 70), cv2.FONT_HERSHEY_COMPLEX, 1, color, 2)
            
            print(f"Result: {access_text}")
        
        cv2.imshow('Access Control System - Press Q to quit', img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    print("System stopped")
