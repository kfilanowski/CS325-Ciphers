##
# Kevin Filanowski
# Octobor 19, 2018
#
# This program encrypts and decrypts messages using a Caesar Shift Cipher.
# It will ask the user for input, whether to use encryption or decryption, and
# also what key to use.
##
import string

# The Engligh alhabet.
_ALPHABET = list(string.ascii_lowercase)

##
# This method controls the menu of the program, where it will ask the user for
# input on what to do. 0 is to quit, 1 is to Encrypt a message, and 2 is to
# decrypt a message.
##
def menu():
    print("\nCaesar Shift Cipher.\nPlease pick an option.")
    option = -1
    while option != 0:
        try:
            option = int(input("\n0) Quit\n1) Encrypt\n2) Decrypt\n> "))
        except ValueError:
            print("Bad input. Please pick 0, 1, or 2.")
            option = -1
        if option == 1:
            print("\nEncrypted message:", encrypt())
        elif option == 2:
            print("\nDecrypted message:", decrypt())

    print("\nGoodbye!")

##
# This method is simply to ask the user for input on the key to shift with.
# It must be an integer, so it takes care of non-integer values.
# @return shift An integer number to shift by, known as the key.
##
def inputKey():
    shift = ""
    while type(shift) != int:
        try:
            shift = int(input("Enter a number to shift by: "))
        except ValueError:
            print("Please enter an integer.\n")
            shift = ""
    return shift

##
# This method runs the encrpytion algorithm for a caesar shift cipher.
# It will ask the user for the key to use, and the message to encrypt.
# It will the shift every letter in the plaintext by the key to the right and 
# wrap around to the front of the alphabet if it goes past the letter z.
# @return The ciphertext.
##
def encrypt():
    shift = inputKey()
    plaintext = input("Enter the message to encrypt: ").lower()
    ciphertext = list(plaintext)
    
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            # Position of plaintext relative to alphabet.
            position = ord(plaintext[i])-ord('a')
            # Replace a single letter.
            ciphertext[i] = _ALPHABET[(position + shift) % len(_ALPHABET)]
        
    return ''.join(ciphertext)

##
# This method runs the decryption algorithm for a caesar shift cipher.
# It will ask the user for the key to use, and the message to decrypt.
# It will the shift every letter in the ciphertext by the key to the left and 
# wrap around to the end of the alphabet if it goes before the letter a.
# @return The plaintext.
##
def decrypt():
    shift = inputKey()
    ciphertext = input("Enter the message to decrypt: ").lower()
    plaintext = list(ciphertext)
    
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            # Position of ciphertext relative to alphabet.
            position = ord(ciphertext[i])-ord('a')
            # Replace a single letter.
            plaintext[i] = _ALPHABET[(position - shift) % len(_ALPHABET)]
    
    return ''.join(plaintext)

##
# The main method, runs the program.
##
def main():
    menu()
    
main()