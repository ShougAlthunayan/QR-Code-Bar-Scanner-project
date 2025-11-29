import cv2
from pyzbar.pyzbar import decode

print("Webcam QR Scanner Starting...")

def scan_qr_code_webcam():
    # Open webcam
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return
    
    print("Webcam started! Press 'q' to quit.")
    
    while True:
        # Read frame
        ret, frame = cap.read()
        
        if not ret:
            break
        
        # Detect QR codes
        decoded_objects = decode(frame)
        
        # Process detected QR codes
        for obj in decoded_objects:
            data = obj.data.decode('utf-8')
            qr_type = obj.type
            
            # Draw rectangle around QR code
            x, y, w, h = obj.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            
            # Display text
            cv2.putText(frame, f'{data}', (x, y-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
            
            print(f"Detected QR: {data}")
        
        # Show video
        cv2.imshow('QR Code Scanner - Webcam', frame)
        
        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Clean up
    cap.release()
    cv2.destroyAllWindows()
    print("Scanner stopped.")

if __name__ == "__main__":
    scan_qr_code_webcam()
