# Symetric CryptoSystem

## Introduction

This is a simple symmetric cryptosystem implemented in Python. It uses a substitution cipher based on a random mapping of the alphabet. The script allows you to encrypt and decrypt messages using a specified seed for the random number generator.

## Usage

### Prerequisites

- Python 3.x

### Installation

No installation is required. Just make sure you have Python installed on your system.

### Execution

1. Open a terminal.

2. Navigate to the directory containing the script (`main.py`).

3. Run the following command to encrypt a message:

    ```bash
    python main.py --encrypt --seed <SEED> --message "<YOUR_MESSAGE>"
    ```

    Replace `<SEED>` with an integer value for the random seed and `<YOUR_MESSAGE>` with the message you want to encrypt.

    Example:

    ```bash
    python main.py --encrypt --seed 42 --message "HELLOWORLD"
    ```

4. Run the following command to decrypt a message:

    ```bash
    python main.py --decrypt --seed <SEED> --message "<ENCRYPTED_MESSAGE>"
    ```

    Replace `<SEED>` with the same seed used for encryption and `<ENCRYPTED_MESSAGE>` with the message you want to decrypt.

    Example:

    ```bash
    python main.py --decrypt --seed 42 --message "KTSSXIXRSZ"
    ```

### Options

- `--seed`: Specify the seed for the random number generator.
- `--message`: Specify the message to encrypt or decrypt.
- `--encrypt`: Flag to indicate encryption.
- `--decrypt`: Flag to indicate decryption.
