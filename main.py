from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from os.path import dirname, join, exists
import datetime
import pandas as pd
Builder.load_string("""
<KOT>:
    on_enter: root.get_time()
    on_enter: root.show_last()
    BoxLayout:
        id: master_screen
        orientation: 'vertical'  
        BoxLayout:
            id: time_sign
            orientation: 'horizontal' 
            TextInput:
                id: day
                text: ''
                size_hint: (1/2, 1)
                cursor_blink: True
                font_size: 80
                multiline: False    
            TextInput:
                id: month
                text: ''
                size_hint: (1/2, 1)
                cursor_blink: True
                font_size: 80
                multiline: False  
            TextInput:
                id: year
                text: ''
                size_hint: (1, 1)
                cursor_blink: True
                font_size: 80
                multiline: False  
            TextInput:
                id: time
                text: ''
                size_hint: (1, 1)
                cursor_blink: True
                font_size: 80
                multiline: False  
            Button:
                text: 'food'
                size_hint: (0.75, 1)
                pos_hint: {"right": 1}
                on_press: root.manager.current = 'food'  
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text: '+ 1d'
                size_hint: (1, 1)
                pos_hint: { 'left' : 0}  
                on_press:
                    root.change_time(86400, day.text, month.text, year.text, time.text)   
            Button:
                text: '+ 1h'
                size_hint: (1, 1)
                pos_hint: { 'left' : 0.1}   
                on_press:
                    root.change_time(3600, day.text, month.text, year.text, time.text) 
            Button:
                text: '+ 30m'
                size_hint: (1, 1)
                pos_hint: { 'left' : 0.2}  
                on_press:
                    root.change_time(1800, day.text, month.text, year.text, time.text)
        BoxLayout:
            orientation: 'horizontal'                               
            Button:
                text: '- 1d'
                size_hint: (1, 1)
                pos_hint: { 'left' : 0.4}
                on_press:
                    root.change_time(-86400, day.text, month.text, year.text, time.text)  
            Button:
                text: '- 1h'
                size_hint: (1, 1)
                pos_hint: { 'left' : 0.6}
                on_press:
                    root.change_time(-3600, day.text, month.text, year.text, time.text)                                 
            Button:
                text: '- 30m'
                size_hint: (1, 1)
                pos_hint: { 'left' : 0.8} 
                on_press:
                    root.change_time(-1800, day.text, month.text, year.text, time.text) 
        BoxLayout:
            orientation: 'horizontal'    
            TextInput:
                id: category
                text: '0'
                size_hint: (0.2, 1)
                pos_hint: { 'left' : 0.8}
                cursor_blink: True
                font_size: 55
                multiline: False 
            Button:
                text: '+'
                size_hint: (0.15, 1)
                pos_hint: { 'left' : 0.7}   
                on_press: 
                    root.change_amount("+", category.text)                             
            Button:
                text: '-'
                size_hint: (0.15, 1)
                pos_hint: { 'left' : 0.85}  
                on_press: 
                    root.change_amount("-", category.text)  
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
                        root.store_kot_input(category.text, year.text, month.text, day.text, time.text)        
                        root.show_last()
                Button:
                    text: 'Goto food'
                    size_hint: (1, 1)
                    pos_hint: {"right": 1}
                    on_press: root.manager.current = 'food'   
        Label:
            id: dir_kot
            text: '' 
            multiline: False   

<FOOD>:
    on_enter: root.get_time()
    on_enter: root.show_last()
    BoxLayout:
        id: master_screen
        orientation: 'vertical'  
        BoxLayout:
            id: time_sign
            orientation: 'horizontal' 
            TextInput:
                id: day
                text: ''
                size_hint: (1/2, 1)
                cursor_blink: True
                font_size: 80
                multiline: False    
            TextInput:
                id: month
                text: ''
                size_hint: (1/2, 1)
                cursor_blink: True
                font_size: 80
                multiline: False  
            TextInput:
                id: year
                text: ''
                size_hint: (1, 1)
                cursor_blink: True
                font_size: 80
                multiline: False  
            TextInput:
                id: time
                text: ''
                size_hint: (1, 1)
                cursor_blink: True
                font_size: 80
                multiline: False  
            Button:
                text: 'kot'
                size_hint: (0.75, 1)
                pos_hint: {"right": 1}
                on_press: root.manager.current = 'kot'  
        BoxLayout:
            orientation: 'horizontal'
            size_hint: (1, 2) 
            Button:
                text: '+ 1d'
                size_hint: (1, 1)
                pos_hint: { 'left' : 0}  
                on_press:
                    root.change_time(86400, day.text, month.text, year.text, time.text)   
            Button:
                text: '+ 1h'
                size_hint: (1, 1)
                pos_hint: { 'left' : 0.1}   
                on_press:
                    root.change_time(3600, day.text, month.text, year.text, time.text) 
            Button:
                text: '+ 30m'
                size_hint: (1, 1)
                pos_hint: { 'left' : 0.2}  
                on_press:
                    root.change_time(1800, day.text, month.text, year.text, time.text)
        BoxLayout:
            orientation: 'horizontal'   
            size_hint: (1, 2)                             
            Button:
                text: '- 1d'
                size_hint: (1, 1)
                pos_hint: { 'left' : 0.4}
                on_press:
                    root.change_time(-86400, day.text, month.text, year.text, time.text)  
            Button:
                text: '- 1h'
                size_hint: (1, 1)
                pos_hint: { 'left' : 0.6}
                on_press:
                    root.change_time(-3600, day.text, month.text, year.text, time.text)                                 
            Button:
                text: '- 30m'
                size_hint: (1, 1)
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
                font_size: 55
                multiline: False    
            TextInput:
                id: amount
                text: '1'
                size_hint: (0.2, 1)
                pos_hint: { 'left' : 0.8}
                cursor_blink: True
                font_size: 55
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
            size_hint: (1, 7)  
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
                        root.store_input(food.text, amount.text, year.text, month.text, day.text, time.text, dir_food.text)        
                        root.show_last()
                Button:
                    text: 'placeholder'
                    size_hint: (1, 1)
                    pos_hint: {"right": 1}
                    on_press: root.manager.current = 'kot'  
        Label:
            id: dir_food
            text: '' 
            multiline: True           

""")

def calc_time_diff(amount, current_day, current_month, current_year, current_time):
    current_hour = current_time.split(":")[0]
    current_minute = current_time.split(":")[1]
    current_date = datetime.datetime(year=int(current_year),
                                     month=int(current_month),
                                     day=int(current_day),
                                     hour=int(current_hour),
                                     minute=int(current_minute))
    new_date = current_date + datetime.timedelta(seconds=int(amount))
    return new_date

def adjust_minutes(inp_min):
    if (int(inp_min) == 0):
        str_minute = "00"
    else:
        str_minute = "30"
    return str_minute

def get_filepath():
    #return "/sdcard/KOTSTAT"
    return "C:/Users/macrh/repos/kotstat"



# Declare both screens
class KOT(Screen):
    def show_last(self):
        filepath=join(get_filepath(), "kot.csv")
        if(exists(filepath)):
            df = pd.read_csv(filepath, dtype=str)
            self.ids.dir_kot.text = str(df.iloc[-3:]).split("\n", maxsplit=1)[1]
    def get_time(self):
        now = datetime.datetime.now()
        hour = now.hour
        minute_rounded = round(round(now.minute*(5/3)/50)*50/(5/3))
        time_rounded = now - datetime.timedelta(minutes=now.minute) + datetime.timedelta(minutes=minute_rounded)
        self.ids.time.text = str(time_rounded.hour) + ":" + adjust_minutes(time_rounded.minute)
        self.ids.day.text = str(time_rounded.day)
        self.ids.month.text = str(time_rounded.month)
        self.ids.year.text = str(time_rounded.year)
    def get_dir(self):
        self.ids.dir.text = rf
    def change_time(self, amount, current_day, current_month, current_year, current_time):
        new_date = calc_time_diff(amount, current_day, current_month, current_year, current_time)
        self.ids.time.text = str(new_date.hour) + ":" + adjust_minutes(new_date.minute)
        self.ids.day.text = str(new_date.day)
        self.ids.month.text = str(new_date.month)
        self.ids.year.text = str(new_date.year)
    def store_kot_input(self, cat, year, month, day, time):
        filepath = join(get_filepath(), "kot.csv")
        new_data = {
            "year": [year],
            "month": [month],
            "day": [day],
            "time": [time],
            "category": [cat],
        }
        if(exists(filepath)):
            df = pd.read_csv(filepath, dtype=str)
            new_df= pd.concat([df, pd.DataFrame(new_data)], ignore_index=True)
        else:
            new_df = pd.DataFrame(new_data)
        if((float(cat) > 0) and (float(cat) < 8)):
            new_df.to_csv(filepath, index=False)
        self.ids.category.text = '0'
    def change_amount(self, dir, current):
        if dir == "+":
            new = float(current)+1
        else:
            new = float(current)-1
        if new<0:
            new = 0
        if new>7:
            new = 7
        self.ids.category.text = str(int(new))
    pass

class FOOD(Screen):
    def show_last(self):
        filepath = join(get_filepath(), "food.csv")
        if(exists(filepath)):
            df = pd.read_csv(filepath, dtype=str)
            self.ids.dir_food.text = str(df.iloc[-3:]).split("\n", maxsplit=1)[1]
    def get_time(self):
        now = datetime.datetime.now()
        hour = now.hour
        minute_rounded = round(round(now.minute*(5/3)/50)*50/(5/3))
        time_rounded = now - datetime.timedelta(minutes=now.minute) + datetime.timedelta(minutes=minute_rounded)
        self.ids.time.text = str(time_rounded.hour) + ":" + adjust_minutes(time_rounded.minute)
        self.ids.day.text = str(time_rounded.day)
        self.ids.month.text = str(time_rounded.month)
        self.ids.year.text = str(time_rounded.year)
    def change_time(self, amount, current_day, current_month, current_year, current_time):
        new_date = calc_time_diff(amount, current_day, current_month, current_year, current_time)
        self.ids.time.text = str(new_date.hour) + ":" + adjust_minutes(new_date.minute)
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
    def store_input(self, food, amount, year, month, day, time, dir):
        filepath = join(get_filepath(), "food.csv")
        new_data={
            "year": [year],
            "month": [month],
            "day": [day],
            "time": [time],
            "food": [food],
            "amount": [amount]
        }
        if(exists(filepath)):
            df = pd.read_csv(filepath, dtype=str)
            new_df= pd.concat([df, pd.DataFrame(new_data)], ignore_index=True)
        else:
            new_df = pd.DataFrame(new_data)
        if(food!=''):
            new_df.to_csv(filepath, index=False)
            self.ids.food.text = ''
    pass

class TestApp(App):
    def build(self):
        global rf
        rf=self.initilize_global_vars()
        sm = ScreenManager()
        sm.add_widget(KOT(name='kot'))
        sm.add_widget(FOOD(name='food'))
        return sm
    def initilize_global_vars(self):
        root_folder = self.user_data_dir
        return root_folder
if __name__ == '__main__':
    TestApp().run()