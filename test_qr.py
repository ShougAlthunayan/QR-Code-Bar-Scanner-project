import qrcode
import cv2
from pyzbar.pyzbar import decode

print("=== QR Code Test Generator ===")

# Create a test QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to QR code
data = "https://github.com/your-repo"
qr.add_data(data)
qr.make(fit=True)

# Create and save image
img = qr.make_image(fill_color="black", back_color="white")
img.save("test_qr_code.png")
print(" Test QR code saved as 'test_qr_code.png'")
print(f" QR code contains: {data}")

# Test scanning it back
print("\nTesting scanner...")
image = cv2.imread("test_qr_code.png")
decoded_objects = decode(image)

if decoded_objects:
    for obj in decoded_objects:
        scanned_data = obj.data.decode('utf-8')
        print(f" Scanner successfully read: {scanned_data}")
        print(" SUCCESS: Scanner is working perfectly!")
else:
    print(" ERROR: Scanner could not read the QR code")
