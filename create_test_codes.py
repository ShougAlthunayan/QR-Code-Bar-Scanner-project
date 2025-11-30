import qrcode

# Student IDs and Names for QR codes 
student_credentials = [
   '202200662 - Shoug Althunayan',
    '202100267 - Shahad Hamraa', 
    '202201633 - Jood Alghamdi',
    '201900253 - Noura Alafaliq'
]

print("Creating student QR codes for access control...")

for credential in student_credentials:
    qr = qrcode.make(credential)
    # Create filename from ID only (cleaner)
    student_id = credential.split(' - ')[0]
    filename = f"student_{student_id}.png"
    qr.save(filename)
    print(f"✓ Created: {filename} - {credential}")


print("\nQR codes created successfully!")
print("Use these for access control testing:")
for credential in student_credentials:
    student_id = credential.split(' - ')[0]
    print(f"- student_{student_id}.png")
