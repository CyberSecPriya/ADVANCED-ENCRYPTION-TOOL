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
