import cv2
import numpy as np
from pyzbar.pyzbar import decode
import argparse

print("QR Code Scanner Started!")

def scan_qr_code(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Error: Could not load image from {image_path}")
        return
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect QR codes
    decoded_objects = decode(gray)
    
    if not decoded_objects:
        print("No QR codes found in the image.")
        return
    
    print(f"Found {len(decoded_objects)} QR code(s):")
    
    # Process each QR code
    for i, obj in enumerate(decoded_objects):
        data = obj.data.decode('utf-8')
        qr_type = obj.type
        
        print(f"QR Code {i+1}:")
        print(f"  Type: {qr_type}")
        print(f"  Data: {data}")
        
        # Draw bounding box
        points = obj.polygon
        points = np.array(points, dtype=np.int32)
        cv2.polylines(image, [points], True, (0, 255, 0), 3)
        
        # Put text
        x, y, w, h = obj.rect
        cv2.putText(image, f'QR: {data}', (x, y-10), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    
    # Display result
    cv2.imshow('QR Code Scanner', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', type=str, required=True, help='Path to image file')
    args = parser.parse_args()
    
    scan_qr_code(args.image)
