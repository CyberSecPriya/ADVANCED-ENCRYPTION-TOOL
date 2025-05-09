# ADVANCED-ENCRYPTION-TOOL

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : PRIYA BABARE

*INTERN ID* : CT04DA834 

*DOMAIN* : CYBER  SECURITY & ETHICAL  HACKING

*DURATION* : 4 WEEKS

*MENTOR* : NEELA SANTOSH

# DESCRIPTION

The **Advanced Encryption Tool** is a secure and user-friendly desktop application designed to **encrypt and decrypt files** using advanced cryptographic algorithms. Built with Python and the `cryptography` library, this tool employs **AES-256 encryption** (via the Fernet module) to ensure the confidentiality and integrity of file contents. The tool is especially useful for users who want to secure sensitive documents, such as financial records, reports, or personal data, with minimal technical complexity.

This application also includes a **Graphical User Interface (GUI)** built using the `Tkinter` library, enabling even non-technical users to perform file encryption and decryption with just a few button clicks.

# FEATURES

**AES-256 Encryption via Fernet**: Provides secure encryption using the `cryptography` library’s Fernet implementation, which uses AES in CBC mode with HMAC for authentication.
-  **Graphical User Interface**: The interface allows users to select, encrypt, and decrypt files easily.
- **File Handling Support**: Accepts any file type (e.g., `.txt`, `.pdf`, `.jpg`) for encryption or decryption.
-  **Automatic Key Management**: Generates and securely stores an encryption key in a file called `secret.key`. The same key is reused for all operations unless replaced.
- **Status Notifications**: Provides feedback to users upon successful encryption, decryption, or in the case of an error (e.g., file not found).
-  **Safe Exit**: Users can exit the application safely using the "Exit" button.

  # ADDITONAL ENHANCEMENTS

To deepen understanding of GUI development in Python and make the tool more interactive, I added the following personal enhancements:

- **Custom Background Color**: A light blue background was applied to the GUI window to make the interface visually appealing and improve readability.
- **Exit Button**: A dedicated "Exit" button was implemented that allows users to close the application easily, demonstrating proper event handling in Tkinter.
- **Hover Effects on Buttons**: To enhance the user experience and make the interface feel more dynamic, I added hover effects on the buttons. When the user hovers over any button (like "Encrypt", "Decrypt", "Select File", or "Exit"), the button color or style changes to indicate it is clickable. This improvement was made for both aesthetic appeal and improved usability.

These features were added beyond the project requirements to support my learning goals in GUI design and Python event-driven programming.

# HOW IT WORKS

1. On the first run, the program automatically creates a `secret.key` file, which stores the encryption key securely.
2. Users can select any file from their system using the "Select File" button.
3. Clicking the "Encrypt" button will encrypt the selected file and create a new file with a `.enc` extension.
4. Clicking the "Decrypt" button will decrypt any previously encrypted `.enc` file and create a new file with a `.dec` extension.
5. Status messages will notify the user of success or errors (e.g., file not found).
6. The "Exit" button cleanly shuts down the application.

# SETUP INSTRUCTIONS

 **PREREQUISITES**

- Python 3.6 or above
- Required libraries:
  ```bash
  pip install cryptography

# RUNNING THE APPLICATION

1. Save the source code in a file named encryption_tool_gui.py.

2. Run the file using:

```bash
python encryption_tool_gui.py
```
3. The GUI window will open. Use the interface to select and encrypt/decrypt files.

# FILE STRUCTURE

1. encryption_tool_gui.py → **( Main GUI and encryption/decryption logic)**
   
2. secret.key                    **( Automatically generated encryption key )**

3. sampletest.txt                 **( Example input file )**
 
4. test.txt.enc                   **( Example encrypted output file )**
 
5. test.txt.dec                   **( Example decrypted output file )**   

**IMPORTANT**: Do Not Upload `secret.key` to Public Repositories

This key is essential for both encrypting and decrypting files. Sharing it publicly would compromise the security of all encrypted files.

# OUTPUT 

Here are sample outputs demonstrating the encryption and decryption process:

- **When a file is successfully encrypted the output you will recieve as show in below:**

![Image](https://github.com/user-attachments/assets/6a785922-aa11-4594-8806-82a1c8a59e1e)

Encrypted and saved as your file.txt.enc

- **When a file is successfully decrypted the output you will recieve as show in below:**

![Image](https://github.com/user-attachments/assets/c0ddf67b-aa30-418e-a25c-b7fda2a17e72)

  Decrypted and saved as your file.txt.dec

 # NOTE

This project is intended for educational purposes during an internship and is **not licensed for commercial use** without prior approval.

 # CONCLUSION
  
This Advanced Encryption Tool was built to demonstrate secure file encryption and decryption using AES-256 through Python’s `cryptography` library, combined with a simple and user-friendly GUI developed using Tkinter. The project successfully allows users to select files, encrypt or decrypt them with a secure key, and receive visual feedback through the interface.

Some enhancements such as the background color, the Exit button, and the hover effect were added purely for my personal learning and experimentation with GUI elements in Python. These features help improve user interaction and were valuable for my growth in understanding how to make desktop applications more interactive and visually intuitive.
