from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from ruffier import *

name = ""
age = 7
p1, p2, p3 = 0, 0, 0

class Screen1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # TODO create widgets
        name_lb = Label(text="Enter your name:")
        age_lb = Label(text="Enter your age:")
        self.name_inp = TextInput(multiline=False)
        self.age_inp = TextInput(multiline=False)

        # TODO create layouts
        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(name_lb)
        line1.add_widget(self.name_inp)

        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2.add_widget(age_lb)
        line2.add_widget(self.age_inp)

        self.main_layout = BoxLayout(orientation="vertical")
        self.main_layout.add_widget(line1)
        self.main_layout.add_widget(line2)

        self.btn = Button(text='Start', size_hint=(0.2, None),
                          height='30sp', pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        self.main_layout.add_widget(self.btn)

        self.add_widget(self.main_layout)

    def next(self):
        self.manager.current = "second"
        global name, age 
        name = self.name_inp.text 
        age = int(self.age_inp.text) 


class Screen2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        txt_test1 = '''Measure your pulse for 15 seconds.\n
        Write your results in the corresponding fields.'''
        label1 = Label(text=txt_test1)

        inp1_lb = Label(text="Enter your pulse")
        self.inp1 = TextInput(multiline=False)

        self.main_layout = BoxLayout(orientation='vertical')
        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(inp1_lb)
        line1.add_widget(self.inp1)

        self.btn = Button(text='Next', size_hint=(0.2, None),
                          height='30sp', pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next

        self.main_layout.add_widget(label1)
        self.main_layout.add_widget(line1)
        self.main_layout.add_widget(self.btn)

        self.add_widget(self.main_layout)

    def next(self):
        self.manager.current = "third"
        global p1 
        p1 = int(self.inp1.text)


class Screen3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False 
        label1 = Label(text="Do squat in 45 seconds")
        
        self.lbl_sec = Label(text = "Seconds elapsed: ")
        self.time = 0
        self.btn = Button(text='Next', size_hint=(0.2, None),
                          height='30sp', pos_hint={'center_x': 0.5})
        
        self.btn.on_press = self.next
        self.main_layout = BoxLayout(orientation = 'vertical')
        self.main_layout.add_widget(self.lbl_sec)
        self.main_layout.add_widget(label1)
        self.main_layout.add_widget(self.btn)

        self.add_widget(self.main_layout)
    
    def on_enter(self):
        Clock.schedule_once(self.finished, 10)
        self.event = Clock.schedule_interval(self.display_time, 1)
    
    def finished(self, dt):
        self.next_screen = True
        self.btn.set_disabled(False)
        self.event.cancel()

    def display_time(self, dt):
        self.time += 1
        self.lbl_sec.text = "Second elapsed: " + str(self.time)

    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
        else:
            self.manager.current = 'fourth'

class Screen4(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        txt_test1 = '''Measure your pulse for 15 seconds.\nWrite your results in the corresponding fields.'''
        label1 = Label(text=txt_test1)

        inp1_lb = Label(text="Enter your pulse")
        self.inp1 = TextInput(multiline=False)

        inp2_lb = Label(text="Enter your pulse")
        self.inp2 = TextInput(multiline=False)

        self.lbl_sec = Label("Seconds elapsed: ")
        self.time = 1

        self.main_layout = BoxLayout(orientation='vertical')
        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(inp1_lb)
        line1.add_widget(self.inp1)

        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2.add_widget(inp2_lb)
        line2.add_widget(self.inp2)

        self.btn = Button(text='Next', size_hint=(0.2, None),
                          height='30sp', pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next

        self.main_layout.add_widget(label1)
        self.main_layout.add_widget(line1)
        self.main_layout.add_widget(line2)
        self.main_layout.add_widget(self.btn)

        self.add_widget(self.main_layout)
    
    def on_enter(self):
        Clock.schedule_once(self.finished, 5)
        self.event = Clock.schedule_interval(self.display_time, 1)
    
    def display_time(self, dt):
        self.time += 1
        self.lbl_sec.text = "Seconds elasped: " + str(self.time)


    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.inp1.set_disabled(True)
            self.inp2.set_disabled(True)
        else:
            self.manager.current = "fifth"

            global p2, p3 
            p2 = int(self.inp1.text)
            p3 = int(self.inp2.text)

class Screen5(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.result = Label(text = "")
        self.main_layout = BoxLayout(orientation = "vertical")
        self.main_layout.add_widget(self.result)

        self.add_widget(self.main_layout)
        self.on_enter = self.getResult
    
    def getResult(self):
        self.result.text = testResult(p1, p2, p3, age)

class MyClass(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Screen1(name="first"))
        sm.add_widget(Screen2(name="second"))
        sm.add_widget(Screen3(name="third"))
        sm.add_widget(Screen4(name="fourth"))
        sm.add_widget(Screen5(name="fifth"))
        return sm


app = MyClass()
app.run()
