from PIL import Image
from pathlib import Path

class PictureColoredToBlack():
    #This Method changes the selected picture into a greyscaled version 
    def ChangeToBlackWhite(self,picture):
        #sets the Path of the Project to access the image
        path = "./LF12Sportverein_Stoppuhrzeit/ConvertingPictures/"
        #sets the Download path where to safe the changed picture
        downloads_path = str(Path.home() / "Downloads")
        #Converts the selected picture into a greyscaled
        picture_to_black_and_white = Image.open(path+ picture).convert('L')
        #Saves the picture into the Download Path
        picture_to_black_and_white.save(downloads_path +'/'+'greyscaled_'+ picture)
        
