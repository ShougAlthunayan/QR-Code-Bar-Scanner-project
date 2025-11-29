import qrcode

# Create QR codes with our names only
student_names = [
    'Shoug Althunayan', 
    'Shahad alhamraa'
]

print("Creating student QR codes for access control...")

for name in student_names:
    qr = qrcode.make(name)
    filename = f"{name.replace(' ', '_')}.png"
    qr.save(filename)
    print(f"✓ Created: {filename}")

print("\nQR codes created successfully!")
print("Use these for access control testing:")
print("- Shoug_Althunayan.png")
print("- Shahad_alhamraa.png")
