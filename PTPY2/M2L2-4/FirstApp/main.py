from kivy.app import App 
from kivy.uix.button import Button 
from kivy.uix.label import Label 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.screenmanager import ScreenManager, Screen
from pip import main 

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        btn1 = Button(text = "Button 1")
        btn2 = Button(text = "Button 2")
        btn3 = Button(text = "Button 3")
        btn4 = Button(text = "Button 4")

        label = Label(text = "Choose a screen")

        btn_layout = BoxLayout(orientation = 'vertical') 
        main_layout = BoxLayout() 

        btn_layout.add_widget(btn1)
        btn_layout.add_widget(btn2)
        btn_layout.add_widget(btn3)
        btn_layout.add_widget(btn4)

        main_layout.add_widget(label)
        main_layout.add_widget(btn_layout)

        self.add_widget(main_layout)

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))
        return sm 
    

app = MyApp()
app.run()