document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("decryptForm").addEventListener("submit", function (event) {
        event.preventDefault();
        decryptMessage();
    });
});

function decryptMessage() {
    let fileInput = document.getElementById("decryptImage");
    let passwordInput = document.getElementById("decryptPassword");
    let resultText = document.getElementById("decryptedMessage");

    if (fileInput.files.length === 0) {
        alert("Please select an image to decrypt.");
        return;
    }

    let formData = new FormData();
    formData.append("image", fileInput.files[0]);
    formData.append("password", passwordInput.value);

    resultText.innerHTML = "🔄 Processing decryption... Please wait.";

    fetch("/decrypt", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            resultText.innerHTML = `<span style="color: red;">❌ Error: ${data.error}</span>`;
        } else {
            resultText.innerHTML = `<strong>🔓 Decrypted Message:</strong> ${data.decrypted_message}`;
        }
    })
    .catch(error => {
        resultText.innerHTML = `<span style="color: red;">❌ Error: ${error.message}</span>`;
    });
}
