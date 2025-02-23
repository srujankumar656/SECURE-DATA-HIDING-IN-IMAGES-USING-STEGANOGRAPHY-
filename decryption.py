import cv2

def decrypt_message(img_path, password):
    """
    Decrypts a message from an image using steganography.
    :param img_path: Path to the encrypted image.
    :param password: Password for decryption (not used in this basic example).
    :return: The decrypted message.
    """
    img = cv2.imread(img_path)
    
    if img is None:
        raise ValueError("Error loading image. Ensure it's a valid image file.")

    message = ""
    m, n = 0, 0  # Pixel coordinates (row, column)

    while n < img.shape[0] and m < img.shape[1]:
        char = chr(img[n, m, 0])  # Read from the Blue channel
        if char == "~":  # Stop at end marker
            break
        message += char
        m += 1
        if m == img.shape[1]:  # Move to the next row if needed
            n += 1
            m = 0

    return message
