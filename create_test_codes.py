import qrcode

# Student IDs and Names for QR codes 
student_credentials = [
   '202200662 - Shoug Althunayan',
    '202100267 - Shahad Hamraa', 
    '202201633 - Jood Alghamdi',
    '201900253 - Noura Alafaliq'
]

print("Creating student QR codes for access control...")

for name in student_credentials:
    qr = qrcode.make(name)
    filename = f"{name.replace(' ', '_')}.png"
    qr.save(filename)
    print(f" Created: {filename}")

print("\nQR codes created successfully!")
print("Use these for access control testing:")
print("202200662 - Shoug_Althunayan.png")
print("202100267 - Shahad_Hamraa.png")
print("202201633 - Jood_Alghamdi.png")
print("201900253 - Noura_Alafaliq.png")
