from PIL import Image
from pytesseract import pytesseract

class getText:
#Define path to tessaract.exe
    path_to_tesseract = '\Tesseract-OCR\tesseract.exe'
    #Define path to image
    path_to_image = 'file:///Users/Gurjit/Downloads/istockphoto-641719442-612x612.jpg'
    #Point tessaract_cmd to tessaract.exe
    pytesseract.tesseract_cmd = path_to_tesseract
    #Open image with PIL

    img = Image.open(path_to_image)
    #Extract text from image
    text = pytesseract.image_to_string(img)
    print(text)
