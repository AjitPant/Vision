from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
import Motion_Detector
import low_light
import hc2
import Low_light_reading
from os import listdir
kv_path = './kv/'
for kv in listdir(kv_path):
    Builder.load_file(kv_path+kv)


class MDButton(Button):
    pass


class POCRButton(Button):
    pass

class LLRButton(Button):
    pass


class HCButton(Button):
    pass

class Container(GridLayout):
    display = ObjectProperty()

    def MD(self):
       Motion_Detector.MD()
       pass

    def POCR(self):
       low_light.PTS()
       pass
    def LLR(self):
       Low_light_reading.LLR()
       pass
    def HC(self):
       hc2.HC()
       pass

class MainApp(App):
    def build(self):
        self.title = 'Awesome app!!!'
        return Container()


if __name__ == "__main__":
    app = MainApp()
    app.run()
