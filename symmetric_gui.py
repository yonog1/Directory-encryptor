import main_logic
from cryptography.fernet import InvalidToken

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

        self.gen_key = Button(
            text="Generate Key: ", font_size=30, on_press=self.gen_key_press
        )
        self.key_output = TextInput()

        self.add_widget(self.gen_key)
        self.add_widget(self.key_output)

        self.encrypt = Button(
            text="Encrypt Directory: ", font_size=30, on_press=self.encrypt_popup_key
        )
        self.encrypted_dir = TextInput()
        self.add_widget(self.encrypt)
        self.add_widget(self.encrypted_dir)

        self.decrypt = Button(
            text="Decrypt Directory: ", font_size=30, on_press=self.decrypt_popup_key
        )
        self.decrypted_dir = TextInput()
        self.add_widget(self.decrypt)
        self.add_widget(self.decrypted_dir)

    def gen_key_press(self, event):
        self.key_output.text = main_logic.gen_key()

    def encrypt_popup_key(self, event):
        layout = GridLayout(cols=1, padding=10)

        key_input = TextInput(text="")
        closeButton = Button(text="Apply")

        layout.add_widget(key_input)
        layout.add_widget(closeButton)

        # Instantiate the modal popup and display
        popup = Popup(
            title="Enter key:", content=layout, size_hint=(None, None), size=(200, 200)
        )
        popup.open()

        # Attach close button press with popup.dismiss action
        closeButton.bind(on_press=lambda *args: self.enc_dir_input(key_input.text))

    def decrypt_popup_key(self, event):
        layout = GridLayout(cols=1, padding=10)

        key_input = TextInput(text="")
        closeButton = Button(text="Apply")

        layout.add_widget(key_input)
        layout.add_widget(closeButton)

        # Instantiate the modal popup and display
        popup = Popup(
            title="Enter key:", content=layout, size_hint=(None, None), size=(200, 200)
        )
        popup.open()
        # Attach close button press with popup.dismiss action
        closeButton.bind(on_press=lambda *args: self.dec_dir_input(key_input.text))

    def enc_dir_input(self, text):
        try:
            main_logic.main(self.encrypted_dir.text, "e", text)
        except FileNotFoundError:
            print("The directory is invalid")
        except ValueError:
            print("Enter a key")
        except InvalidToken:
            print("Incorrect key")

    def dec_dir_input(self, text):
        try:
            main_logic.main(self.encrypted_dir.text, "d", text)
        except FileNotFoundError:
            print("The directory is invalid")
        except ValueError:
            print("Enter a key")
        except InvalidToken:
            print("Incorrect key")


class Encryptor(App):
    def build(self):
        self.icon = "mazi.ico"
        return MyGrid()


if __name__ == "__main__":
    Encryptor().run()
