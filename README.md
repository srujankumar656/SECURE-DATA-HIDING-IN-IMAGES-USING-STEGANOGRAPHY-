# SECURE-DATA-HIDING-IN-IMAGES-USING-STEGANOGRAPHY-
# Steganography App 🔐

## 📌 Project Overview
This project is a **Steganography App** that allows users to **hide and retrieve secret messages inside images** securely using **Flask, OpenCV, and JavaScript**.

# 📑 Project Presentation
> For a detailed overview of the project, you can refer to the project presentation:

[AICTE x IBM-INTERN-PROJECT-PPT (2).pptx](./AICTE%20x%20IBM-INTERN-PROJECT-PPT.pptx)
## 🚀 Features
- **Secure Encryption**: Hide messages inside images with password protection.
- **Decryption Mechanism**: Retrieve the hidden message only with the correct passcode.
- **User-Friendly UI**: A modern, responsive interface for easy interaction.
- **Multiple Image Formats Supported**: Works with PNG, JPG, BMP, and TIFF images.

## 🛠️ Technologies Used
- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Flask (Python), OpenCV (for image processing)
  
# 📂 Steganography-App
````
│── 📂 static              # Static files (CSS, JS, Images)
│   ├── styles.css        # Styling for the app
│   ├── script.js         # JavaScript for client-side logic
│── 📂 templates           # HTML templates
│   ├── index.html        # Main webpage
│── 📂 encryption_module   # Encryption-related files
│   ├── encryption.py     # Encryption logic
│── 📂 decryption_module   # Decryption-related files
│   ├── decryption.py     # Decryption logic
│── app.py                # Main Flask application
│── requirements.txt       # Dependencies (Flask, OpenCV, etc.)
│── README.md              # Project Documentation
│── .gitignore             # Files to ignore in GitHub
````

## 📂 How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/steganography-app.git
   cd steganography-app

### 2. Install Dependencies
```
npm install 
pip install opencv-python
pip install Flask
pip install pillow
```

### Backend dependencies
```
pip install -r requirements.txt
```
## Frontend dependencies
```
npm install 
```

## Start the frontend
```
npm run dev
```

## Start the backend
````
python src/app.py
````
# Access the Application
```
Open http://localhost:5173/ in your browser
```

# 📜 Key Functions
* encrypt_message(image, message, password)  # Encrypts and hides a message in an image
* decrypt_message(image, password)  # Retrieves the hidden message from an image
