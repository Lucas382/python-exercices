from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import NumericProperty
from kivy.uix.floatlayout import FloatLayout

class MyGrid(Widget):
    #Recebe o id e modifica o label conforme o id passado adicionando valores
    def add(self, label):
        max = int(self.ids.pts_max.text)
        num1 = int(self.ids[label].text)
        num2 = 1
        mod = "mod_" + label
        text = int(self.ids[mod].text)

        if max == 0:
            popup = Popup(title='Ops',
                          content=Label(text='Você não possui pontos o suficente'),
                          size_hint=(None, None), size=(300, 200))
            popup.open()
        if (num1 % 2) != 0 and text < 5 and max > 0 or num1 + 1 == 10 and text < 5 and max > 0 :
            self.ids[mod].text = str(text + 1)
        if max > 0:
            if num1 <= 13 and max - 1 > -1:
                self.ids[label].text = str(num1 + num2)
                self.ids.pts_max.text = str(max - 1)

            elif num1 <= 15 and max - 2 > -1:
                self.ids[label].text = str(num1 + num2)
                self.ids.pts_max.text = str(max - 2)
            elif num1 <= 17 and max - 3 > -1:
                self.ids[label].text = str(num1 + num2)
                self.ids.pts_max.text = str(max - 3)
            else:
                popup = Popup(title='Ops',
                                content =Label(text='Você não pode colocar mais de\n 18 pontos no mesmo modificador'),
                                size_hint =(None, None), size=(300, 200))
                popup.open()

    # Recebe o id e modifica o label conforme o id passado subtraindo valores
    def sub(self, label):
        max = int(self.ids.pts_max.text)
        num1 = int(self.ids[label].text)
        num2 = 1
        mod = "mod_" + label
        text = int(self.ids[mod].text)

        if (num1 % 2) == 0 and text > - 1:
            self.ids[mod].text = str(text - 1)

        if max < 32 and num1 > 8:
            if num1 <= 14 and max + 1 < 33:
                self.ids[label].text = str(num1 - num2)
                self.ids.pts_max.text = str(max + 1)
            elif num1 == 14 or num1 == 15 or num1 == 16 and max + 2 < 21:
                self.ids[label].text = str(num1 - num2)
                self.ids.pts_max.text = str(max + 2)
            elif num1 == 17 or num1 == 18 and max + 3 < 21:
                self.ids[label].text = str(num1 - num2)
                self.ids.pts_max.text = str(max + 3)
            else:
                popup = Popup(title='Ops',
                                content =Label(text='Você não pode ter menos pontos nesse atributo'),
                                size_hint =(None, None), size=(300, 200))
                popup.open()

    pass


class MainApp(App):
    def build(self):
        return MyGrid()

if __name__=="__main__":
    MainApp().run()


