import os
from PIL import Image
import pytesseract

# Set the Tesseract command path
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\patzanov\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Path to the folder containing JPEG files
folder_path = 'foto'

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.jpg') or filename.endswith('.jpeg'):
        # Construct full file path
        file_path = os.path.join(folder_path, filename)
        
        print(f'Processing file: {file_path}')  # Debugging line
        
        try:
            # Open the image file
            img = Image.open(file_path)
            
            # Use pytesseract to extract text
            text = pytesseract.image_to_string(img)
            
            # Print the extracted text
            print(f'Text from {filename}:\n{text}\n')
        except Exception as e:
            print(f'Error processing {filename}: {e}')  # Error handling
