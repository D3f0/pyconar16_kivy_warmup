__version__ = "0.1.1"
from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        return Label(text="Preprandonos para el taller de Kivy")


if __name__ == '__main__':
    MyApp().run()
