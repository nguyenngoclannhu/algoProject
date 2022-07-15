from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

class MainScr(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		
class MyApp(App):
	def build(self):
		btn = Button(text = "App is running")
		return btn

app = MyApp()
app.run()