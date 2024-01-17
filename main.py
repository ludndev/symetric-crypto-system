import random
import argparse

class SymetricCryptoSystem:
    def __init__(self, seed):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.seed = seed
        self.random_generator = random.Random(seed)
        self.mapping = self.generate_mapping()

    def generate_mapping(self):
        shuffled_alphabet = list(self.alphabet)
        self.random_generator.shuffle(shuffled_alphabet)
        mapping = dict(zip(self.alphabet, shuffled_alphabet))
        return mapping

    def encrypt(self, message):
        encrypted_message = ''
        for char in message:
            if char.upper() in self.alphabet:
                encrypted_message += self.mapping[char.upper()]
            else:
                encrypted_message += char
        return encrypted_message

    def decrypt(self, encrypted_message):
        decrypted_message = ''
        reverse_mapping = {v: k for k, v in self.mapping.items()}
        for char in encrypted_message:
            if char.upper() in self.alphabet:
                decrypted_message += reverse_mapping[char.upper()]
            else:
                decrypted_message += char
        return decrypted_message

def main():
    parser = argparse.ArgumentParser(description='Symmetric CryptoSystem')
    parser.add_argument('--seed', type=int, required=True, help='Seed for the random number generator')
    parser.add_argument('--message', type=str, required=True, help='Message to encrypt or decrypt')
    parser.add_argument('--encrypt', action='store_true', help='Encrypt the message')
    parser.add_argument('--decrypt', action='store_true', help='Decrypt the message')

    args = parser.parse_args()

    crypto_system = SymetricCryptoSystem(args.seed)

    if args.encrypt:
        result = crypto_system.encrypt(args.message)
        print("Encrypted Message:", result)
    elif args.decrypt:
        result = crypto_system.decrypt(args.message)
        print("Decrypted Message:", result)
    else:
        print("Please specify either --encrypt or --decrypt")

if __name__ == "__main__":
    main()
