from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import NumericProperty
from kivy.uix.floatlayout import FloatLayout

class MyTunning(Widget):
    def calc(self):
        max = float(self.ids.max_bar.text)
        min = float(self.ids.min_bar.text)
        percent_front = float(self.ids.percent.text)
        percent_rear = 100 - float(self.ids.percent.text)
        front = (max - min) * (percent_front /100) + min
        rear =  (max - min) * (percent_rear /100) + min

        self.ids.front.text = str(f'{front:.2f}')
        self.ids.rear.text = str(f'{rear:.2f}')

    def clear(self):
        self.ids.max_bar.text = ""
        self.ids.min_bar.text = ""
        self.ids.percent.text = ""

        self.ids.front.text = "Dianteira"
        self.ids.rear.text = "Traseira"
    pass

class MainApp(App):
    def build(self):
        return MyTunning()

if __name__=="__main__":
    MainApp().run()