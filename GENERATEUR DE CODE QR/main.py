import qrcode

lien = input("Veuillez entrer le lien : ").strip()

chemin = "C:\\Users\\sined\\OneDrive - Université Cheikh Anta DIOP de DAKAR\\Bureau\\Mes Projets\\QR Code\\votre_qrcode.png"

qr = qrcode.QRCode()
qr.add_data(lien)

image = qr.make_image()
image.save(chemin)

print(f"Votre QR Code a été généré dans le chemin fourni : {chemin}")