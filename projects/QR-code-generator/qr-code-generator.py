import qrcode

def generate_qr_code(input):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border=4
    )

    qr.add_data(input)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr-img.png")


input_text = input("Enter your url ")
generate_qr_code(input_text)