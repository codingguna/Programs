import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
def convert_image_to_text(image_path):
    # Open the image file using the PIL library
    image = Image.open(image_path)

    # Use the pytesseract library to extract text from the image
    text = pytesseract.image_to_string(image)

    # Save the extracted text to a text file
    with open('C:\\Users\\gs400\\Documents\\New Text Document.txt', 'w') as f:
        f.write(text)

    # Print the extracted text to the console
    print(text)
    x=int(input('enter any no to exit'))

if __name__ == '__main__':
    ima=input("enter path of image :")
    convert_image_to_text(ima)