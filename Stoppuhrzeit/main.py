import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]


class MainApp(App):
    def build(self):
        layout = BoxLayout(padding=10)
        colors = [red, green, blue, purple]

        for i in range(5):
            btn = Button(text="Button #%s" % (i + 1),
                         background_color=random.choice(colors),
                         size_hint=(.5, .5)
                         )

            layout.add_widget(btn)
        label = Label(text = "Hallo Welt",size_hint=(.5, .5),pos_hint={'center_x': 0, 'center_y': 0}, color = "yellow" )
        layout.add_widget(label)
        return layout


if __name__ == '__main__':
    app = MainApp()
    app.run()
