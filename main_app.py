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
        orientation: 'vertical'
        TextInput:
            id: time
            text: 'jou'
            size_hint: (1, 1)
            cursor_blink: True
            font_size: 10
            multiline: False
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text: 'food'
                on_press: root.manager.current = 'food'
            Button:
                text: 'enter'
                on_press: 
                    root.on_press_button()

<FOOD>:
    on_enter: root.get_time()
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            orientation: 'horizontal' 
            TextInput:
                id: day
                text: ''
                size_hint: (0.2, 1)
                pos_hint: { 'left' : 0}
                cursor_blink: True
                font_size: 20
                multiline: False    
            TextInput:
                id: month
                text: ''
                size_hint: (0.2, 1)
                pos_hint: { 'left' : 0.2}
                cursor_blink: True
                font_size: 20
                multiline: False  
            TextInput:
                id: year
                text: ''
                size_hint: (0.3, 1)
                pos_hint: { 'left' : 0.4}
                cursor_blink: True
                font_size: 20
                multiline: False  
            TextInput:
                id: time
                text: ''
                size_hint: (0.3, 1)
                pos_hint: { 'left' : 0.7}
                cursor_blink: True
                font_size: 20
                multiline: False  
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text: '+ 1 day'
                size_hint: (0.1, 1)
                pos_hint: { 'left' : 0}     
            Button:
                text: '- 1 day'
                size_hint: (0.1, 1)
                pos_hint: { 'left' : 0.1}   
            Button:
                text: '+ 1h'
                size_hint: (0.2, 1)
                pos_hint: { 'left' : 0.2}                                
            Button:
                text: '- 1h'
                size_hint: (0.2, 1)
                pos_hint: { 'left' : 0.4} 
            Button:
                text: '+ 30 min'
                size_hint: (0.2, 1)
                pos_hint: { 'left' : 0.6}                                
            Button:
                text: '- 30 min'
                size_hint: (0.2, 1)
                pos_hint: { 'left' : 0.8}  
        BoxLayout:
            orientation: 'horizontal' 
            TextInput:
                id: food
                text: ''
                size_hint: (0.5, 1)
                pos_hint: { 'left' : 0}
                cursor_blink: True
                font_size: 20
                multiline: False    
            TextInput:
                id: amount
                text: ''
                size_hint: (0.2, 1)
                pos_hint: { 'left' : 0.8}
                cursor_blink: True
                font_size: 20
                multiline: False 
            Button:
                text: '+'
                size_hint: (0.15, 1)
                pos_hint: { 'left' : 0.7}                                
            Button:
                text: '-'
                size_hint: (0.15, 1)
                pos_hint: { 'left' : 0.85}  
        BoxLayout:
            orientation: 'horizontal'
            size_hint: (1, 3)  
            Button:
                text: 'most common food'  
                size_hint: (1, 1)                                 
            BoxLayout:
                orientation: 'vertical'
                size_hint: (1, 1)  
                Button:
                    text: 'enter'
                    size_hint: (1, 1)
                    pos_hint: {"right": 1}
                    on_press: 
                        root.on_press_button(txtinp.text)
                    on_press: root.get_time()        
                Button:
                    text: 'Goto kot'
                    size_hint: (1, 1)
                    pos_hint: {"right": 1}
                    on_press: root.manager.current = 'kot'            

""")

# Declare both screens
class KOT(Screen):
    def on_press_button(self):
        print("hello")

    pass

class FOOD(Screen):
    def on_press_button(self, inp):
        print(inp)
    def get_time(self):
        now = str(datetime.datetime.now()).split(" ")
        date=now[0]
        hour = int(now[1].split(":")[0])
        minute = round(round(int(now[1].split(":")[1])*(5/3)/50)*50/(5/3))
        if minute == 60:
            hour = hour+1
            minute = 0
        if hour >= 24:
            hour = hour - 24
        if minute == 0:
            minstr = "00"
        else:
            minstr = str(minute)
        time=str(hour)+":"+minstr
        self.ids.time.text = time
        #self.ids.date.text = date
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