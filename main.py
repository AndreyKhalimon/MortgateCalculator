from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MortgateCalculatorApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, Mortgate Calculator", halign="center")


MortgateCalculatorApp().run()