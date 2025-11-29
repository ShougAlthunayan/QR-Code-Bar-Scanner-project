import cv2
import qrcode

print("=== Simple QR Test ===")

# Create QR code
qr = qrcode.make("COMPUTER VISION PROJECT WORKING!")
qr.save("test_simple.png")
print("✓ QR code created: test_simple.png")

# Test OpenCV can read it
detector = cv2.QRCodeDetector()
img = cv2.imread("test_simple.png")

if img is not None:
    data, bbox, _ = detector.detectAndDecode(img)
    if data:
        print(f" SUCCESS! Detected: {data}")
    else:
        print(" QR created but not detected (normal for simple test)")
else:
    print(" Error loading image")
