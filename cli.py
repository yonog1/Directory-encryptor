import os
import platform
import main_logic


def main_menu():
    user_input = ""
    while user_input != "exit":
        clear_screen()
        print("Welcome to Yonog's encryptor")
        print("Select a menu option:\n")
        print("1 - Generate key")
        print("2 - Encrypt Dir")
        print("3 - Decrypt Dir")
        print("\nType 'exit' and press 'Enter' to quit the application.")

        user_input = input("\nEnter Option...\n")

        menu_options = {
            "1": generate_key,
            "2": encrypt_directory,
            "3": decrypt_directory,
        }

        selected_option = menu_options.get(user_input)
        if selected_option:
            try:
                selected_option()
            except FileNotFoundError as e:
                clear_screen()
                print(f"Error: {e.strerror}: '{e.filename}'")
                input("Press Enter to continue...")
            except ValueError as e:
                clear_screen()
                print(f"Error: Key is invalid.\n{e}")
                input("Press Enter to continue...")


def save_key_to_file(key):
    with open("keys.txt", "ab") as file:
        file.write(key + b"\n")


def clear_screen():
    system = platform.system()
    if system == "Windows":
        os.system("cls")
    elif system in ("Linux", "Darwin"):
        os.system("clear")
    else:
        raise NotImplementedError(
            "Clearing the screen is not supported on this platform."
        )


def generate_key():
    clear_screen()
    print("Your key:")
    key = main_logic.gen_key()
    print(key.decode())
    save_key_to_file(key)
    print(
        f"{'*' * 90}\nNote - All key generation history is saved in a 'keys.txt' file in the running directory\n{'*' * 90}"
    )
    input("Press Enter to continue...")


def encrypt_directory():
    path = input("Enter path:\n")
    key = input("Enter key to encrypt with:\n")
    recurse = input(
        "Enter 'y' to encrypt all sub-directories. Press 'Enter' otherwise.\n"
    )
    recurse = True if recurse.lower() == "y" else False
    main_logic.main(path, "e", key, recurse)
    print("Encryption completed.")
    input("Press Enter to continue...")


def decrypt_directory():
    path = input("Enter path:\n")
    key = input("Enter key to decrypt with:\n")
    recurse = input(
        "Enter 'y' to decrypt all sub-directories. Press 'Enter' otherwise.\n"
    )
    recurse = True if recurse.lower() == "y" else False
    main_logic.main(path, "d", key, recurse)
    print("Decryption completed.")
    input("Press Enter to continue...")


if __name__ == "__main__":
    main_menu()
