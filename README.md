# EncryptionProject

## Description
EncryptionProject is a Python-based encryption and decryption tool for files and images using custom algorithms.

## Project Structure

- **main.py**: The main script that orchestrates the program.
- **encryption.py**: Functions for encrypting and decrypting data.
- **img_encode.py**: Functions for steganography - encrypting in images.
- **img_decode.py**: Functions for steganography extraction - decrypting encrypted images.
- **input_functions.py**: Functions for user input handling.
- **file_functions.py**: Functions for handling file operations such as reading and writing.


## Requirements
- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YehudaWieder/EncryptionProject.git
   ```

2. Navigate to the project directory:
   ```bash
   cd EncryptionProject
   ```
   
3. Before running the project, install the required dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```
   
## Usage

1. Run the main script:
   ```bash
   python main.py
   ```

2. Follow the on-screen instructions:
   - To encrypt a file, enter the path to a text file.
   - To decrypt a file, enter the path to an encrypted file.
   - Some encryption methods require a **KEY**, which is a numerical value provided by the user.

