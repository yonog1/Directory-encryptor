import main_logic
import os, sys, platform


def save_key_to_file(key):
    with open("keys.txt", "ab") as file:
        file.write(key + b"\n")


def clear():
    print(platform.system())
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux" or platform.system == "Darwin":
        os.system("clear")
    else:
        raise NotImplementedError(
            "Clearing the screen is not supported on this platform."
        )


def main():
    # user_input = input()
    # Main Menu
    user_input = ""
    while user_input != "exit":
        clear()
        # [print(i) for i in sys.argv]
        print("Welcome to Yonog's encryptor")
        print("Select a menu option:\n")
        print("1 - Generate key")
        print("2 - Encrypt Dir")
        print("3 - Decrypt Dir")
        print("\n\nType 'exit' and press 'Enter' to quit the application.")

        user_input = input("\nEnter Option...\n")

        match user_input:
            case "1":
                clear()
                print("Your key:")
                key = main_logic.gen_key()
                print(key.decode())
                save_key_to_file(key)
                print(
                    "****\n"
                    "Note - All key generation history is saved in a 'keys.txt' file in the running directory"
                    "\n****"
                )
                print("Press Enter to continue...")
                input()

                pass
            case "2":
                path = input("Enter path:\n")
                key = input("Enter key to encrypt with:\n")
                recurse = input(
                    "Enter 'y' to encrypt all sub-directories. Press 'Enter' otherwise.\n  "
                )
                recurse = True if recurse.lower() == "y" else False
                main_logic.main(path, "e", key, recurse)
            case "3":
                path = input("Enter path:\n")
                key = input("Enter key to decrypt with:\n")
                recurse = input(
                    "Enter 'y' to decrypt all sub-directories. Press 'Enter' otherwise.\n  "
                )
                recurse = True if recurse.lower() == "y" else False
                main_logic.main(path, "d", key, recurse)


if __name__ == "__main__":
    main()
