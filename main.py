from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config

# Fixing the size of the window
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '500')


class GUI_Design(Widget):
    pass


class RoboticsApp(App):
    def build(self):
        self.title = 'Robotic Arm Control'
        return GUI_Design()


if (__name__ == "__main__"):
    RoboticsApp().run()
