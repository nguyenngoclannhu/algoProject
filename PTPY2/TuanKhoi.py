from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput # * import TextInput()

class ScrButton(Button):
	def __init__(self, screen, direction, goal, **NO):
		super().__init__(**NO)
		self.screen = screen 
		self.direction = direction 
		self.goal = goal
	def on_press(self):
		self.screen.manager.transition.direction = self.direction 
		self.screen.manager.current = self.goal 
		

class MainScreen(Screen):
	def __init__(self,**NO):
		super().__init__(**NO)
		#TODO create vertical main layout 
		vl = BoxLayout(orientation = 'vertical') #QVBoxLayout

		#TODO create horizontal layout 
		hl = BoxLayout() #QHBoxLayout
		txt = Label(text = "Choose a screen")
		
		#TODO 
		vl.add_widget(ScrButton(self, direction = 'down', goal = 'first', text = 'Screen 1'))
		vl.add_widget(ScrButton(self, direction = 'up', goal = 'second', text = 'Screen 2'))
		vl.add_widget(ScrButton(self, direction = 'left', goal = 'third', text = 'Screen 3'))
		vl.add_widget(ScrButton(self, direction = 'right', goal = 'fourth', text = 'Screen 4'))



		
		hl.add_widget(txt)
		hl.add_widget(vl)
		self.add_widget(hl)

#TODO tạo class FirstScreen 
class fst_scr(Screen):
	def __init__(self, **NO):
		super().__init__(**NO)
		# * tạo layout dọc 
		vl = BoxLayout(orientation = "vertical", size_hint = (.5, .5), pos_hint = {'center_x':0.5, 'center_y':0.5})
		choice = Button(text = "Choice 1", size_hint = (.5,1), pos_hint = {"left": 0})
		back = ScrButton(self, direction = "up", goal = "main", text = "Choice 2", size_hint = (.5,1), pos_hint = {"right": 1})
		#TODO add buttons to the layout 
		vl.add_widget(choice) 
		vl.add_widget(back)

		self.add_widget(vl) 

class snc_scr(Screen):
	def __init__(self, **NO):
		super().__init__(**NO)
		lb = Label(text = "Choice 2: ")
		vl = BoxLayout(orientation = "vertical")

		hl = BoxLayout(size_hint = (0.8, None), height = "30sp")
		enter = Label(text = "Enter your password: ")
		passwd = TextInput(multiline=False)

		back = ScrButton(self, direction = "down", goal = "main", text = "Back")
		button = Button(text = "OK!")

		hl.add_widget(enter)
		hl.add_widget(passwd)

		vl.add_widget(lb)
		vl.add_widget(hl)

		self.add_widget(vl)

class MainApp(App):
	def build(self):
		sm = ScreenManager()
		sm.add_widget(MainScreen(name="main"))

		# TODO: add first screen 
		sm.add_widget(fst_scr(name = 'first'))

		# TODO: add 2nd screen 
		sm.add_widget(snc_scr(name = 'second'))
		return sm
		
app = MainApp()
app.run()		
		
		
		
		