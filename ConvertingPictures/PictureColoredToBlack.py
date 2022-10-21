from PIL import Image

class PictureColoredToBlack():
    
    def ChangeToBlackWhite(picture):
        picture_to_black_and_white = Image.open(picture).convert('L')

        picture_to_black_and_white.save('greyscaled_'+ picture)
        
