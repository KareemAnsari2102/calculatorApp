import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class myApp(App):

    def build(self):
        root_widget = BoxLayout(orientation='vertical')
        output_label = Label(size_hint_y=0.75, font_size=50)
        button_symbols = ('1', '2', '3', '+',
                          '4', '5', '6', '-',
                          '7', '8', '9', '.',
                          '0', '*', '/', '=')
        button_grid = GridLayout(cols=4, size_hint_y=2)
        for symbol in button_symbols:
            button = Button(text=symbol)
            button.bind(on_press=self.button_click)
            button_grid.add_widget(button)

        clear_button = Button(text='Clear', size_hint_y=None, height=100)
        clear_button.bind(on_press=self.clear_label)

        root_widget.add_widget(output_label)
        root_widget.add_widget(button_grid)
        root_widget.add_widget(clear_button)

        return root_widget

    def button_click(self, instance):
        output_label = self.root.children[0]
        current_text = output_label.text

        if instance.text == '=':
            try:
                output_label.text = str(eval(current_text))
            except Exception as e:
                output_label.text = "Error"
        else:
            output_label.text += instance.text

    def clear_label(self, instance):
        output_label = self.root.children[0]
        output_label.text = ""

if __name__ == '__main__':
    myApp().run()

