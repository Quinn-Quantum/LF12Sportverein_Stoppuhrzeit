from PIL import Image
from pathlib import Path
import requests

class PictureColoredToBlack():
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
        picture_to_black_and_white.save(downloads_path +'\\'+'greyscaled_'+ imageName[:-3] + "png")
        localpath = downloads_path +'\\'+'greyscaled_'+ imageName[:-3] + "png"
        print(localpath)
        serverurl = 'https://bmxertv.de/LF12Sportverein_Stoppuhrzeit_API/view/uploadfile.php' #API ansprechen

        headers = {
            'Content-Type': 'multipart/form-data'
        }
        f = open(localpath,'rb')
        r = requests.post(serverurl ,files={'userfile':f})
        f.close()

        print(r.text)
        