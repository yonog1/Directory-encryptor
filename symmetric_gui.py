import fix_proj
import kivy
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2

        self.gen_key = Button(text="Generate Key: ",
                              font_size=30, on_press=self.gen_key_press)
        self.key_output = TextInput()

        self.add_widget(self.gen_key)
        self.add_widget(self.key_output)

        self.encrypt = Button(text="Encrypt Directory: ",
                              font_size=30, on_press=self.popup_key)
        self.encrypted_dir = TextInput()
        self.add_widget(self.encrypt)
        self.add_widget(self.encrypted_dir)

        self.decrypt = Button(text="Decrypt Directory: ", font_size=30, on_press = self.popup_key)
        self.decrypted_dir = TextInput()
        self.add_widget(self.decrypt)
        self.add_widget(self.decrypted_dir)

    def gen_key_press(self, event):
        self.key_output.text = fix_proj.gen_key()

    def popup_key(self, event):
        layout = GridLayout(cols = 1, padding = 10)
  
        popupLabel = Label(text = "Click for pop-up")
        closeButton = Button(text = "Close the pop-up")
  
        layout.add_widget(popupLabel)
        layout.add_widget(closeButton)       
  
        # Instantiate the modal popup and display
        popup = Popup(title ='Demo Popup',
                      content = layout,
                      size_hint =(None, None), size =(200, 200))  
        popup.open()   
  
        # Attach close button press with popup.dismiss action
        closeButton.bind(on_press = popup.dismiss)

    # TODO bind it to its respective button and pass params accordingly
    def enc_dir_input(self, dir):
        fix_proj.encrypt(dir)

    # TODO bind it to its respective button and pass params accordingly
    def dec_dir_input(dir):
        fix_proj.decrypt(dir)


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
