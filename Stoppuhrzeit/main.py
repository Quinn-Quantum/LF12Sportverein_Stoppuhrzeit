from kivy.app import App
from kivy.factory import Factory
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from os.path import expanduser

# sources:
# https://www.youtube.com/watch?v=YlRd4rw_vBw
# https://www.youtube.com/watch?v=U9j2ztt8xvM
# https://kivy.org/doc/stable/api-kivy.uix.filechooser.html
# https://stackoverflow.com/questions/42505450/kivy-change-filechooser-defaul-location

#Class for the LoadDialog part in Layout
class LoadDialog(FloatLayout):
    # variables
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    selected = ObjectProperty(None)

    # function displays the image in the app and recovers the filepath so that it can be displayed.
    def selected(self, filename):
        try:
            self.ids.my_image.source = filename[0]

        except NameError:
            print("File not found")


# Class for the Root part in Layout
class Root(FloatLayout):
    # variables
    loadfile = ObjectProperty(None)
    run_time = StringProperty()

    def dismiss_popup(self):
        self._popup.dismiss()

    #Opens the path to gallery
    def show_load(self):
        #The functions load and cancel are being added into the LoadDialog 
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    #activates the function to turn the selected picture into a greyscaled version
    def load(self, filename):
        if len(filename) != 0:
            # Extract file extension
            file_data_type = filename[0][-3:].lower()
            if file_data_type != "png" or file_data_type != "jpg":
                # Calls function to change uploaded picture into a modified greyscaled version
                PictureColoredToBlack().ChangeToBlackWhite(self, filename[0])
                # TODO: Receive and output return from backend
                # Message in label until access to bot does not exist
                self.run_time = "Hier sollte die Laufzeit stehen"
                self.dismiss_popup()
            else:
                # Error message in label
                self.run_time ="False filetype! Only .png and .jpg are usable"
                self.dismiss_popup()
        else:
            # Error message in label
            self.run_time = "Error! no file has been selected"
            self.dismiss_popup()

# must have the same name as the kv-data
class Editor(App):
    pass

# Dialogs defined in editor.kv
# TODO: Color matching to IMT OSZ
# Dialog defined in editor.kv
Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)

# Startpoint/Main Call
if __name__ == '__main__':
    app = Editor()
    app.run()
