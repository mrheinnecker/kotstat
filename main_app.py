from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import datetime
Builder.load_string("""
<KOT>:
    BoxLayout:
        TextInput:
            id: time
            text: 'jou'
            size_hint: (0.2, 0.5)
            cursor_blink: True
            font_size: 10
            multiline: False
        Button:
            text: 'food'
            on_press: root.manager.current = 'food'
        Button:
            text: 'enter'
            on_press: 
                root.on_press_button()

<FOOD>:
    BoxLayout:
        TextInput:
            id: time
            text: ''
            size_hint: (0.2, 0.5)
            cursor_blink: True
            font_size: 10
            multiline: False
        TextInput:
            id: txtinp
            text: 'jou'
            size_hint: (0.2, 0.06)
            pos_hint: {"center_x": 0.5, "center_y": 0.2}
            cursor_blink: True
            font_size: 15
            multiline: False
        Button:
            text: 'Goto kot'
            size_hint: (0.1, 0.1)
            pos_hint: {"center_x": 0, "center_y": 0.9}
            on_press: root.manager.current = 'kot'            
        Button:
            text: 'enter'
            size_hint: (0.1, 0.1)
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            on_press: 
                root.on_press_button(txtinp.text)
            on_press: root.get_time()
""")

# Declare both screens
class KOT(Screen):
    def on_press_button(self):
        print("hello")

    def get_time(self):
        return datetime.datetime.now()

    pass

class FOOD(Screen):
    def on_press_button(self, inp):
        print(inp)
    def get_time(self):
        now = datetime.datetime.now()
        self.ids.time.text = str(now)
    pass

class TestApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(KOT(name='kot'))
        sm.add_widget(FOOD(name='food'))
        return sm

if __name__ == '__main__':
    TestApp().run()