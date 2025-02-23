from flask import Flask, render_template, request, send_file, jsonify
from encryption import encrypt_message
from decryption import decrypt_message
import os
import cv2
import numpy as np
import mimetypes  # ✅ Replaces deprecated imghdr

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp', 'tiff'}

def is_allowed_file(filename):
    file_type, _ = mimetypes.guess_type(filename)  # ✅ Get file type
    return file_type and file_type.startswith('image/')  # ✅ Ensure it's an image

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    try:
        img = request.files['image']
        msg = request.form['message']
        password = request.form['password']

        if not is_allowed_file(img.filename):
            return jsonify({"error": "Invalid file format. Allowed: PNG, JPG, BMP, TIFF"}), 400

        img_path = "temp_image.png"  # Convert to PNG format for consistency
        img_cv = cv2.imdecode(np.frombuffer(img.read(), np.uint8), cv2.IMREAD_COLOR)
        cv2.imwrite(img_path, img_cv)  # Save as PNG

        encrypted_img_path = encrypt_message(img_path, msg, password)
        return send_file(encrypted_img_path, as_attachment=True)
    
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    try:
        img = request.files['image']
        password = request.form['password']

        if not is_allowed_file(img.filename):
            return jsonify({"error": "Invalid file format. Allowed: PNG, JPG, BMP, TIFF"}), 400

        img_path = "temp_image.png"  # Convert to PNG for processing
        img_cv = cv2.imdecode(np.frombuffer(img.read(), np.uint8), cv2.IMREAD_COLOR)
        cv2.imwrite(img_path, img_cv)  

        message = decrypt_message(img_path, password)
        return jsonify({"decrypted_message": message})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
