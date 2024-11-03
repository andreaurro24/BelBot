import easyocr
from google.colab import files

# Prompt to upload the image file
uploaded = files.upload()

# Get the file name from the uploaded dictionary
image_path = list(uploaded.keys())[0]  # Use the uploaded filename directly

# Initialize EasyOCR reader with the language you need (e.g., 'en' for English)
reader = easyocr.Reader(['en'])  # You can add multiple languages like ['en', 'es']

def extract_text_from_image(image_path):
    # Perform OCR on the image
    result = reader.readtext(image_path, detail=0)

    # Join the list of results into a single string
    text = ' '.join(result)
    return text

# Test the function
text = extract_text_from_image(image_path)
print("Extracted Text:\n", text)
