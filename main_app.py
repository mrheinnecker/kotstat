from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import datetime
import pandas as pd
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
        id: master_screen
        orientation: 'vertical'  
        BoxLayout:
            id: time_sign
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
                on_press:
                    root.change_time(86400, day.text, month.text, year.text, time.text)   
            Button:
                text: '- 1 day'
                size_hint: (0.1, 1)
                pos_hint: { 'left' : 0.1}   
                on_press:
                    root.change_time(-86400, day.text, month.text, year.text, time.text) 
            Button:
                text: '+ 1h'
                size_hint: (0.2, 1)
                pos_hint: { 'left' : 0.2}  
                on_press:
                    root.change_time(3600, day.text, month.text, year.text, time.text)                               
            Button:
                text: '- 1h'
                size_hint: (0.2, 1)
                pos_hint: { 'left' : 0.4}
                on_press:
                    root.change_time(-3600, day.text, month.text, year.text, time.text)  
            Button:
                text: '+ 30 min'
                size_hint: (0.2, 1)
                pos_hint: { 'left' : 0.6}
                on_press:
                    root.change_time(1800, day.text, month.text, year.text, time.text)                                 
            Button:
                text: '- 30 min'
                size_hint: (0.2, 1)
                pos_hint: { 'left' : 0.8} 
                on_press:
                    root.change_time(-1800, day.text, month.text, year.text, time.text)  
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
                text: '1'
                size_hint: (0.2, 1)
                pos_hint: { 'left' : 0.8}
                cursor_blink: True
                font_size: 20
                multiline: False 
            Button:
                text: '+'
                size_hint: (0.15, 1)
                pos_hint: { 'left' : 0.7}   
                on_press: 
                    root.change_amount("+", amount.text)                             
            Button:
                text: '-'
                size_hint: (0.15, 1)
                pos_hint: { 'left' : 0.85}  
                on_press: 
                    root.change_amount("-", amount.text)  
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
                        root.store_input(food.text, amount.text, year.text, month.text, day.text, time.text)        
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
    def get_time(self):

        now = datetime.datetime.now()
        hour = now.hour
        minute_rounded = round(round(now.minute*(5/3)/50)*50/(5/3))
        time_rounded = now - datetime.timedelta(minutes=now.minute) + datetime.timedelta(minutes=minute_rounded)

        self.ids.time.text = str(time_rounded.hour) + ":" + str(time_rounded.minute)
        self.ids.day.text = str(time_rounded.day)
        self.ids.month.text = str(time_rounded.month)
        self.ids.year.text = str(time_rounded.year)
    def change_time(self, amount, current_day, current_month, current_year, current_time):

        current_hour=current_time.split(":")[0]
        current_minute = current_time.split(":")[1]
        current_date=datetime.datetime(year=int(current_year),
                                        month=int(current_month),
                                        day=int(current_day),
                                        hour=int(current_hour),
                                        minute=int(current_minute))
        new_date = current_date + datetime.timedelta(seconds=int(amount))
        self.ids.time.text = str(new_date.hour) + ":" + str(new_date.minute)
        self.ids.day.text = str(new_date.day)
        self.ids.month.text = str(new_date.month)
        self.ids.year.text = str(new_date.year)

    def change_amount(self, dir, current):
        if dir == "+":
            new = float(current)+0.5
        else:
            new = float(current)-0.5
        if new<0:
            new = 0
        self.ids.amount.text = str(new)

    def store_input(self, food, amount, year, month, day, time):
        df = pd.read_csv("C:/Users/macrh/repos/kotstat/test.csv", dtype=str)
        new_data={
            "year": [year],
            "month": [month],
            "day": [day],
            "time": [time],
            "food": [food],
            "amount": [amount]
        }
        new_df= pd.concat([df, pd.DataFrame(new_data)], ignore_index=True)
        print(new_df)
        new_df.to_csv("C:/Users/macrh/repos/kotstat/test.csv", index=False)

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