import cv2
import qrcode
import numpy as np

class QRScanner:
    def __init__(self):
        self.detector = cv2.QRCodeDetector()
        print("QR Scanner initialized with OpenCV")
    
    def create_qr(self, data, filename="qr_code.png"):
        """Create a QR code"""
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
        print(f"✓ QR code created: {filename}")
        return filename
    
    def scan_image(self, image_path):
        """Scan QR code from image file"""
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error: Could not load image {image_path}")
            return None
        
        data, bbox, _ = self.detector.detectAndDecode(image)
        
        if data:
            print(f"✓ QR Code detected: {data}")
            # Draw bounding box
            if bbox is not None:
                bbox = bbox.astype(int)
                n = len(bbox)
                for i in range(n):
                    cv2.line(image, tuple(bbox[i][0]), tuple(bbox[(i+1) % n][0]), (0, 255, 0), 3)
            
            cv2.putText(image, f'QR: {data}', (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
            
            cv2.imshow('QR Code Detected', image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            return data
        else:
            print("✗ No QR code detected")
            return None
    
    def scan_webcam(self):
        """Real-time QR code scanning from webcam"""
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Could not open webcam")
            return
        
        print("Webcam started. Press 'q' to quit.")
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Detect QR code
            data, bbox, _ = self.detector.detectAndDecode(frame)
            
            if data:
                print(f"Detected: {data}")
                # Draw bounding box
                if bbox is not None:
                    bbox = bbox.astype(int)
                    n = len(bbox)
                    for i in range(n):
                        cv2.line(frame, tuple(bbox[i][0]), tuple(bbox[(i+1) % n][0]), (0, 255, 0), 3)
                
                cv2.putText(frame, data, (10, 30), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
            
            cv2.imshow('QR Scanner - Press Q to quit', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    scanner = QRScanner()
    
    # Test: Create and scan QR code
    print("=== Testing QR Code Scanner ===")
    qr_file = scanner.create_qr("Hello Computer Vision Project!")
    scanner.scan_image(qr_file)
