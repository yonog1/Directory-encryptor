import os
from cryptography.fernet import Fernet


def gen_key():
    return Fernet.generate_key()


def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # Read all file data
        file_data = file.read()
    # Encrypt data
    encrypted_data = f.encrypt(file_data)
    # Write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)


def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # Read the encrypted data
        encrypted_data = file.read()
    # Decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # Write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)


def main(directory, option, secret_key):

    # Assign directory and iterate over files that directory
    if option.lower() == "e":
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f): # Checking if it is a file
                encrypt(f, secret_key)
    elif option.lower() == "d":
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f):
                decrypt(f, secret_key)


if __name__ == "__main__":
    main()
