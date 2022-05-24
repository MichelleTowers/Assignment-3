from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class Load(Screen):
    pass

class Login(Screen):
    pass

class Disclaimer(Screen):
    pass

class TraqstarzApp(App):
    
    def build(self):
       return sm
   
kv = Builder.load_file('login.kv')
sm = ScreenManager()

sm.add_widget(Load(name='load'))
sm.add_widget(Login(name='login'))
sm.add_widget(Disclaimer(name='disclaimer'))

if __name__ == '__main__':
    TraqstarzApp().run()