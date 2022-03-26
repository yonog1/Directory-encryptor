import fix_proj
import kivy
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


def func():
    print('pressed')
    return 1


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2

        self.gen_key = Button(text="Generate Key: ",
                              font_size=30, on_press=self.gen_key_press)
        self.key_output = TextInput()

        self.add_widget(self.gen_key)
        self.add_widget(self.key_output)

        self.encrypt = Button(text="Encrypt Directory: ", font_size=30) #, on_press=self.enc_dir_input(self.encrypted_dir.text))
        self.encrypted_dir = TextInput()
        self.add_widget(self.encrypt)
        self.add_widget(self.encrypted_dir)

        self.decrypt = Button(text="Decrypt Directory: ", font_size=30)
        self.decrypted_dir = TextInput()
        self.add_widget(self.decrypt)
        self.add_widget(self.decrypted_dir)

    def gen_key_press(self, event):
        self.key_output.text = fix_proj.gen_key()

    #TODO bind it to its respective button and pass params accordingly
    def enc_dir_input(self, dir):
        fix_proj.encrypt(dir)

    #TODO bind it to its respective button and pass params accordingly
    def dec_dir_input(dir):
        fix_proj.decrypt(dir)


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
