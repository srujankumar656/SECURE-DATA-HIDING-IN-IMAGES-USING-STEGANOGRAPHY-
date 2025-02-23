import cv2
import numpy as np

def encrypt_message(img_path, msg, password):
    """
    Encrypts a message into an image using steganography.
    :param img_path: Path to the input image.
    :param msg: The secret message to hide.
    :param password: Password for encryption (not used in this basic example).
    :return: Path to the encrypted image.
    """
    img = cv2.imread(img_path)
    
    if img is None:
        raise ValueError("Error loading image. Ensure it's a valid image file.")

    msg += "~END"  # End marker to detect end of the message in decryption
    ascii_values = [ord(c) for c in msg]
    
    m, n = 0, 0  # Pixel coordinates (row, column)
    index = 0

    for val in ascii_values:
        if n < img.shape[0] and m < img.shape[1]:  # Ensure within image bounds
            img[n, m, 0] = val  # Store ASCII in the Blue channel
            index += 1
            m += 1
            if m == img.shape[1]:  # Move to the next row if needed
                n += 1
                m = 0
        else:
            raise ValueError("Message too long for the image size.")

    encrypted_img_path = "encrypted_image.png"
    cv2.imwrite(encrypted_img_path, img)  # Save encrypted image
    return encrypted_img_path
