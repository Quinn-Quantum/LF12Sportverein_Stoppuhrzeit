from kivy.app import App
from kivy.factory import Factory
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

#https://www.youtube.com/watch?v=YlRd4rw_vBw
#https://www.youtube.com/watch?v=U9j2ztt8xvM
#https://kivy.org/doc/stable/api-kivy.uix.filechooser.html

#Class for the <LordDialog> in the editor.kv
from server import PictureColoredToBlack

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    selected = ObjectProperty(None)

    #function shows the pricture in the app and get the file
    def selected(self, filename):
        try:
            self.ids.my_image.source = filename[0]
            print(filename[0])

        except:
            pass


class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    text_input = ObjectProperty(None)
    run_time = StringProperty()


    def dismiss_popup(self):
        self._popup.dismiss()

    #open data in a new window
    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    #aktiviert die funktion zum schwarz weiß machen
    def load(self, filename):
        if len(filename) != 0:
            file_data_type = filename[0][-3:].lower()
            if file_data_type != "png" or file_data_type != "jpg":
                # Changing Uploaded Picture into Greyscaled
                PictureColoredToBlack.PictureColoredToBlack.ChangeToBlackWhite(self, filename[0])
                self.run_time = "Hier sollte die Laufzeit stehen"
                self.dismiss_popup()
            else:
                # Error Meldung in TextFeld
                self.run_time ="falscher datein  Typ"
                self.dismiss_popup()
        else:
            # Error Meldung in TextFeld
            self.run_time = "extern Fehler"
            self.dismiss_popup()












#Start point
#mast has the same name as the kv data
class Editor(App):
    pass
    # def build(self):
    #  return StartBild()

#Dialog definition in editor.kv
Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)

if __name__ == '__main__':
    app = Editor()
    app.run()
