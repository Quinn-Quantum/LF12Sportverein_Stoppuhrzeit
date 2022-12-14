from kivy.app import App
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
import os

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

            #picture colored to black and whith
            PictureColoredToBlack.PictureColoredToBlack.ChangeToBlackWhite(self,filename[0])
           
        except:
            pass

#Class for the <SaveDialog> in the editor.kv
class SaveDialog(FloatLayout):
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)


class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    text_input = ObjectProperty(None)


    def dismiss_popup(self):
        self._popup.dismiss()



    #open data in a new window
    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()
    #init the Picture
    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.text_input.text = stream.read()

        self.dismiss_popup()

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.text_input.text)

        self.dismiss_popup()

    def test(self):
        print("Hallo")


#Start point
#mast has the same name as the kv data
class Editor(App):
    pass
    # def build(self):
    #  return StartBild()

#Dialog definition in editor.kv
Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('SaveDialog', cls=SaveDialog)

if __name__ == '__main__':
    app = Editor()
    app.run()
