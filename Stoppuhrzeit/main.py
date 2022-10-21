from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label



class MainApp(App):
    def build(self):
        label_hallo = Label(text='Hello User',
                            size_hint=(.10, .10),
                            pos_hint={'center_x': .5, 'center_y': .5},
                            color='yellow')

        button1 = Button(text="Bild analysieren", size_hint=(.5, .10), pos_hint={'center_x': .5, 'center_y': .5},
                         color='yellow', background_color='blue')

        return button1


if __name__ == '__main__':
    app = MainApp()
    app.run()
