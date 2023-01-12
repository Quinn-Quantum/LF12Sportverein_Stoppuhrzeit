from PIL import Image
from pytesseract import pytesseract
from pathlib import Path
import datetime

class getText:
    #This Method changes the selected picture into a greyscaled version 
    #and saves the modified picture in the Downloads Folder
    def ChangeToBlackWhite(self,picture):  
        #sets the Download path where to safe the changed picture
        downloads_path = str(Path.home() / "Downloads")
        #Modifies the Selected Picture into a greyscaled version
        picture_to_black_and_white = Image.open(picture).convert('L')
        splitted = picture.split("\\")
        imageName = splitted[len(splitted)-1]
        #Saves the picture into the Download Folder 
        picture_to_black_and_white.save(downloads_path +'/'+'greyscaled_'+ imageName[:-3] + "png")

    #This Method gets the text from the selected picture and turns it 
    #into a string. It will be displyed as a Time scale
    def extract_text_from_image(image_path):
        # Laden des Bildes
        image = Image.open(image_path)

        #Verwendung von pytesseract, um Text aus dem Bild zu extrahieren
        text = pytesseract.image_to_string(image)

        #Ausgabe des extrahieren Texts
        print(text)

    #Beispieleaufruf TODO
    extract_text_from_image("")  
    
    #This Method checks the formate of the String. Needs to be time-format
    def check_time_format(text):
        current_time = datetime.datetime.now().time()

        current_time_short = current_time.strftime("%H:%M")
        print(current_time_short)