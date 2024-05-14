from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class Calculator(BoxLayout):
    display_text = StringProperty('')

    def update_display(self, text):
        self.display_text += text

    def clear_display(self):
        self.display_text = ''

    def calculate(self):
        try:
            self.display_text = str(eval(self.display_text))
        except:
            self.display_text = 'Error'

class CalculatorApp(App):
    def build(self):
        return Calculator()

if __name__ == "__main__":
    CalculatorApp().run()

