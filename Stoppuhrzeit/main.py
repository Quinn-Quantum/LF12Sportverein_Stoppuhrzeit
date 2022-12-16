from kivy.app import App
from kivy.factory import Factory
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from server import PictureColoredToBlack

# sources:
# https://www.youtube.com/watch?v=YlRd4rw_vBw
# https://www.youtube.com/watch?v=U9j2ztt8xvM
# https://kivy.org/doc/stable/api-kivy.uix.filechooser.html
# https://stackoverflow.com/questions/42505450/kivy-change-filechooser-defaul-location

#Class for the LoadDialog part im Layout
class LoadDialog(FloatLayout):
    # variable
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    selected = ObjectProperty(None)

    # function displays the image in the app and recovers the file ride so that it can be displayed.
    def selected(self, filename):
        try:
            self.ids.my_image.source = filename[0]

        except NameError:
            print("File not found")


# Class for the Root part im Layout
class Root(FloatLayout):
    # variable
    loadfile = ObjectProperty(None)
    run_time = StringProperty()

    def dismiss_popup(self):
        self._popup.dismiss()

    #Opens the path to gallery
    def show_load(self):
        #With content the function load and dismiss_popup can be us in LoadDialog
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    #activates the function to make the image black and white
    def load(self, filename):
        if len(filename) != 0:
            # Extract file extension
            file_data_type = filename[0][-3:].lower()
            if file_data_type != "png" or file_data_type != "jpg":
                # Changing Uploaded Picture into Greyscaled
                PictureColoredToBlack.PictureColoredToBlack.ChangeToBlackWhite(self, filename[0])
                # TODO: Receive and output return from backend
                # Message in label until access to bot does not exist
                self.run_time = "Hier sollte die Laufzeit stehen"
                self.dismiss_popup()
            else:
                # Error message in label
                self.run_time ="falscher datein  Typ"
                self.dismiss_popup()
        else:
            # Error message in label
            self.run_time = "extern Fehler"
            self.dismiss_popup()

# must have the same name as the kv-data
class Editor(App):
    pass

# Dialog defined in editor.kv
Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)

# Startpoint
if __name__ == '__main__':
    app = Editor()
    app.run()
