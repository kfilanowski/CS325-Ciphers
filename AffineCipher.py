##
# Kevin Filanowski
# Octobor 19, 2018
#
# This program encrypts and decrypts messages using an Affine Cipher.
# It will ask the user for input, whether to use encryption or decryption, and
# also what key to use.
##
import string
from fractions import gcd

# The Engligh alhabet.
_ALPHABET = list(string.ascii_lowercase)

##
# This method controls the menu of the program, where it will ask the user for
# input on what to do. 0 is to quit, 1 is to Encrypt a message, and 2 is to
# decrypt a message.
##
def menu():
    print("\nWelcome to the Affine Cipher.\nPlease pick an option.")
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
# This method is simply to ask the user for input on the key's multiplier.
# It must be an integer, so it takes care of non-integer values. 
# The key must also have a greatest common devisor of 1 with the size of the
# alphabet, which would be 26 in English.
# @return multiplier An integer number to multiplier by, the first part of
# the key.
##
def inputKeyMultiplier():
    multiplier = ""
    while type(multiplier) != int:
        try:
            multiplier = int(input("Enter a number to multiply by, where the"
                                    + " gcd of the number and 26 is 1: "))
            if abs(gcd(multiplier, len(_ALPHABET))) != 1:
                multiplier = ""
        except ValueError:
            print("Please enter an integer where the gcd of a number"
                                    + " and 26 is 1.\n")
            multiplier = ""
    return multiplier

##
# This method is simply to ask the user for input on the key.
# It must be an integer, so it takes care of non-integer values.
# @return shift An integer number to shift by, the second part of the key.
##
def inputKeyShift():
    shift = ""
    while type(shift) != int:
        try:
            shift = int(input("Enter a number to shift by: "))
        except ValueError:
            print("Please enter an integer.\n")
            shift = ""
    return shift

##
# Computes the modular inverse of a number.
# A modular inverse is a number a such that a * a^-1 = 1 mod (mod).
# @param a The number to compute the inverse of.
# @param mod The modular number.
# @return The modular inverse of the number a.
##
def inverseMod(a, mod): 
    a = a % mod
    for i in range(1, mod): 
        if ((a * i) % mod == 1): 
            return i
    return 1

##
# This method runs the encrpytion algorithm for a Affine cipher.
# It will ask the user for the key to use, and the message to encrypt.
# It will the multiply the position of the letter by a number and apply a shift 
# on the letter to the right and wrap around to the front of the alphabet if
# it goes past the letter z.
# @return The ciphertext.
##
def encrypt():
    # Get the first part of the key.
    multiplier = inputKeyMultiplier()
    # Get the second part of the key.
    shift = inputKeyShift()
    plaintext = input("Enter the message to encrypt: ").lower()
    ciphertext = list(plaintext)
    
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            # Position of the plaintext relative to the alphabet.
            position  = ord(plaintext[i])-ord('a')
            # Replace a letter.
            ciphertext[i] =_ALPHABET[(multiplier * position + shift) 
                                        % len(_ALPHABET)]
        
    return ''.join(ciphertext)

##
# This method runs the decryption algorithm for a Affine cipher.
# It will ask the user for the key to use, and the message to decrypt.
# It will perform the reverse operation of encrypt.
# @return The plaintext.
##
def decrypt():
    # Get the first part of the key.
    multiplier = inputKeyMultiplier()
    # Get the second part of the key.
    shift = inputKeyShift()
    ciphertext = input("Enter the message to decrypt: ").lower()
    plaintext = list(ciphertext)
    
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            # Position of the plaintext relative to the alphabet.
            position  = ord(ciphertext[i])-ord('a')
            # Replace a letter.
            plaintext[i] = _ALPHABET[inverseMod(multiplier, len(_ALPHABET)) * (position - shift) 
                                        % len(_ALPHABET)]
        
    return ''.join(plaintext)

##
# The main method, runs the program.
##
def main():
    menu()
    
main()