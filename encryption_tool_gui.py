# Import necessary libraries
from cryptography.fernet import Fernet  # For encryption and decryption
import os  # For checking file existence
import tkinter as tk  # For creating GUI (Graphical User Interface)
from tkinter import filedialog  # For opening a file dialog to select files

# Generate and save a key for encryption (this only needs to be done once)
def generate_key():
    key = Fernet.generate_key()  # Generate a new encryption key
    with open("secret.key", "wb") as key_file:  # Save the key to a file
        key_file.write(key)  # Write the key to the file

# Load the encryption key from the saved file
def load_key():
    return open("secret.key", "rb").read()  # Read the key from the saved file

# Encrypt the selected file
def encrypt_file(filename, key):
    fernet = Fernet(key)  # Initialize the encryption tool with the key
    with open(filename, "rb") as file:  # Open the file in read-binary mode
        data = file.read()  # Read the file's data
    encrypted_data = fernet.encrypt(data)  # Encrypt the data
    with open(filename + ".enc", "wb") as file:  # Save the encrypted data as a new file
        file.write(encrypted_data)  # Write encrypted data to a new file
    print(f"Encrypted and saved as {filename}.enc")  # Print success message

# Decrypt the selected file
def decrypt_file(filename, key):
    fernet = Fernet(key)  # Initialize the decryption tool with the key
    with open(filename, "rb") as file:  # Open the encrypted file in read-binary mode
        encrypted_data = file.read()  # Read the encrypted data
    decrypted_data = fernet.decrypt(encrypted_data)  # Decrypt the data
    new_filename = filename.replace(".enc", ".dec")  # Change the file extension for decrypted file
    with open(new_filename, "wb") as file:  # Save the decrypted data as a new file
        file.write(decrypted_data)  # Write decrypted data to a new file
    print(f"Decrypted and saved as {new_filename}")  # Print success message

# Create the GUI window
root = tk.Tk()
root.title("Encryption Tool")  # Set the window title
root.configure(bg="lightblue")  # Set background color

# Check if the encryption key exists; if not, generate a new key
if not os.path.exists("secret.key"):  # If the encryption key doesn't exist
    generate_key()  # Generate the key and save it to a file
    print("Encryption key created and saved.")  # Print a message about the key creation

# Load the key from the file
key = load_key()  # Read the saved encryption key

# Create a Tkinter StringVar to store the file path
filepath = tk.StringVar()

# Function to open a file dialog and select a file
def select_file():
    filepath.set(filedialog.askopenfilename())  # Open file dialog and set the file path

# Function to encrypt the selected file
def encrypt_action():
    file = filepath.get()  # Get the file path from the text box
    if os.path.exists(file):  # If the file exists
        encrypt_file(file, key)  # Call the function to encrypt the file
        status_label.config(text="File Encrypted Successfully!", fg="green")  # Show success message
    else:
        status_label.config(text="File Not Found!", fg="red")  # Show error message

# Function to decrypt the selected file
def decrypt_action():
    file = filepath.get()  # Get the file path from the text box 
    if os.path.exists(file):  # If the file exists
        decrypt_file(file, key)  # Call the function to decrypt the file
        status_label.config(text="File Decrypted Successfully!", fg="green")  # Show success message
    else:
        status_label.config(text="File Not Found!", fg="red")  # Show error message

# Function to exit the application
def exit_app():
    root.destroy()  # Close the application window

# Entry widget to show the file path (textbox)
entry = tk.Entry(root, textvariable=filepath, width=50)
entry.pack(pady=5)

# Button to open file dialog and select a file
select_button = tk.Button(root, text="Select File", command=select_file, bg="white")
select_button.pack(pady=5)

# Button to encrypt the selected file
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_action, bg="white")
encrypt_button.pack(pady=5)

# Button to decrypt the selected file
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_action, bg="white")
decrypt_button.pack(pady=5)

# Button to exit the application
exit_button = tk.Button(root, text="Exit", command=exit_app, bg="white", fg="red")
exit_button.pack(pady=5)

# Label to display status messages (empty initially)
status_label = tk.Label(root, text="", fg="green", bg="lightblue")
status_label.pack(pady=5)

# Start the Tkinter event loop to keep the window open
root.mainloop()

