from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.properties import ListProperty
import random

class LoginScreen(Screen):
    pass

class HomeScreen(Screen):
    bg_color = ListProperty([1, 1, 1, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.change_bg, 1)

    def change_bg(self, dt):
        self.bg_color = [random.random() for _ in range(3)] + [1]

class Game1(Screen):
    pass

class Game2(Screen):
    pass

class Game3(Screen):
    pass

class Game4(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        return ScreenManagement()

if __name__ == '__main__':
    MyApp().run()
    
    #:import FadeTransition kivy.uix.screenmanager.FadeTransition

ScreenManagement:
    transition: FadeTransition()
    LoginScreen:
    HomeScreen:
    Game1:
    Game2:
    Game3:
    Game4:

<LoginScreen>:
    name: 'login'
    BoxLayout:
        orientation: 'vertical'
        padding: 50
        spacing: 20
        Label:
            text: 'Login Page'
            font_size: 30
        TextInput:
            id: username
            hint_text: 'Username'
        TextInput:
            id: password
            hint_text: 'Password'
            password: True
        Button:
            text: 'Login'
            on_press: root.manager.current = 'home'

<HomeScreen>:
    name: 'home'
    canvas.before:
        Color:
            rgba: root.bg_color
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: 'vertical'
        padding: 50
        spacing: 20
        Label:
            text: 'Home Page'
            font_size: 30
        Button:
            text: 'Start Game 1'
            on_press: root.manager.current = 'game1'
        Button:
            text: 'Start Game 2'
            on_press: root.manager.current = 'game2'
        Button:
            text: 'Start Game 3'
            on_press: root.manager.current = 'game3'
        Button:
            text: 'Start Game 4'
            on_press: root.manager.current = 'game4'
        Button:
            text: 'Logout'
            on_press: root.manager.current = 'login'

<Game1>:
    name: 'game1'
    CatchGame:
        on_touch_move: self.on_touch_move(args[1])

<Game2>:
    name: 'game2'
    BoxLayout:
        Label:
            text: "Game 2 Placeholder"

<Game3>:
    name: 'game3'
    BoxLayout:
        Label:
            text: "Game 3 Placeholder"

<Game4>:
    name: 'game4'
    BoxLayout:
        Label:
            text: "Game 4 Placeholder"

<CatchGame@Widget>:
    canvas:
        Color:
            rgb: 0.5, 0.5, 0.5
        Rectangle:
            pos: self.pos
            size: self.size
    Paddle:
        id: paddle
        size_hint: None, None
        size: 100, 20
        pos: self.center_x - 50, 20
    Ball:
        id: ball
        size_hint: None, None
        size: 30, 30
        pos: self.center_x, self.height - 50

    on_touch_move:
        paddle.center_x = args[1].x

<Ball@Widget>:
    canvas:
        Color:
            rgb: 1, 0, 0
        Ellipse:
            pos: self.pos
            size: self.size

<Paddle@Widget>:
    canvas:
        Color:
            rgb: 0, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size