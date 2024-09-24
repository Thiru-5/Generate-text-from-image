import requests
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import io

# Replace 'your_api_key' with your actual Gemini AI API key
API_KEY = 'AIzaSyDoFBgy0xDwMIqTfYyHnheH5N7WYjOioYY'
API_URL = 'https://aistudio.google.com/app/apikey'  # Example URL, replace with actual

def choose_image():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    image_path = filedialog.askopenfilename(title="Select an image", 
                                             filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    return image_path

def extract_text_from_image(image_path):
    with open(image_path, 'rb') as image_file:
        files = {'file': image_file}
        headers = {'Authorization': f'Bearer {API_KEY}'}
        
        response = requests.post(API_URL, headers=headers, files=files)
        
        if response.status_code == 200:
            result = response.json()
            return result.get('text', 'No text found.')
        else:
            return f"Error: {response.status_code} - {response.text}"

if __name__ == "__main__":
    selected_image = choose_image()
    
    if selected_image:
        extracted_text = extract_text_from_image(selected_image)
        print("Extracted Text:")
        print(extracted_text)
    else:
        print("No image selected.")
