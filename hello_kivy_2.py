import kivy
from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hello World')
if __name__ == '__main__':
    print 'hello world'
    print 'hello world2'
    TestApp().run()
    
