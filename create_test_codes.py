import qrcode

# Create authorized QR codes
authorized = [
    'Shoug Althunayan', 
    'Shahad alhamraa',
    'COMPUTER VISION PROJECT',
    'STUDENT ACCESS'
]
unauthorized = 'UNAUTHORIZED PERSON'

print("Creating test QR codes for your project...")

for data in authorized:
    qr = qrcode.make(data)
    filename = f"authorized_{data.replace(' ', '_')}.png"
    qr.save(filename)
    print(f"✓ Created: {filename}")

# Create unauthorized QR code
qr = qrcode.make(unauthorized)
qr.save("unauthorized.png")
print(f" Created: unauthorized.png")
print("\nUse these QR codes to test your access control system!")
print("Scan 'Shoug Althunayan' or 'Shahad alhamraa' for ACCESS GRANTED")
print("Scan 'UNAUTHORIZED PERSON' for ACCESS DENIED")
