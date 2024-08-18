from PIL import Image
import pytesseract
import os

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def recText(filename):
    """Convert image to text using Tesseract OCR."""
    try:
        text = pytesseract.image_to_string(Image.open(filename))
        return text
    except Exception as e:
        return str(e)

info = recText('test1.png')
print(info)

# Save the extracted text to a file
try:
    with open("New.txt", "w") as file:
        file.write(info)
    print("Written successfully")
except Exception as e:
    print(f"Error writing to file: {e}")
