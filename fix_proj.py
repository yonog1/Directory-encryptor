import os
import cryptography
from cryptography.fernet import Fernet


def gen_key():
    key = Fernet.generate_key()
    with open("new_key", "w") as f:
        f.write("SAVE THIS KEY TO DECRYPT DATA\nDO NO SHARE THIS KEY WITH ANYONE\n==============================================\n")
        f.write(key.decode("ASCII"))
    return key


#secret_key = gen_key()

def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)


def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    #key = input("enter key: ")
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)


def main(directory, option, secret_key):

    # assign directory
    # directory = input("Enter path pls: ") | taken as parameter
    # option = input("(E)ncryption or (D)ecryption?: ")  | taken as parameter
    # iterate over files that directory
    if option.lower() == "e":
        #secret_key = input("Enter key to encrypt with: ")
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f): # checking if it is a file
                encrypt(f, secret_key)
    elif option.lower() == "d":
        #secret_key = input("Enter key to decrypt with: ")
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f): # checking if it is a file
                decrypt(f, secret_key)


if __name__ == "__main__":
    main()
