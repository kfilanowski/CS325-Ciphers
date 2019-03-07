##
# Kevin Filanowski
# Octobor 19, 2018
#
# This program checks the md5, SHA-224, SHA-256, SHA-384, and SHA-512 hashes of
# a file input by the user.
##
import hashlib, sys, time

##
# Computes the md5 hash of a string and returns this hash.
# @param text The string to take a md5 hash of.
# @return The md5 hash of the text.
##
def md5_hash(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()

##
# Computes the SHA-224 hash of a string and returns this hash.
# @param text The string to take a SHA-224 hash of.
# @return The SHA-224 hash of the text.
##
def sha_224(text):
    return hashlib.sha224(text.encode('utf-8')).hexdigest()

##
# Computes the SHA-256 hash of a string and returns this hash.
# @param text The string to take a SHA-256 hash of.
# @return The SHA-256 hash of the text.
##
def sha_256(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

##
# Computes the SHA-384 hash of a string and returns this hash.
# @param text The string to take a SHA-384 hash of.
# @return The SHA-384 hash of the text.
##
def sha_384(text):
    return hashlib.sha384(text.encode('utf-8')).hexdigest()

##
# Computes the SHA-512 hash of a string and returns this hash.
# @param text The string to take a SHA-512 hash of.
# @return The SHA-512 hash of the text.
##
def sha_512(text):
    return hashlib.sha512(text.encode('utf-8')).hexdigest()
    
##
# Computes md5, SHA-224, SHA-256, SHA-384, and SHA-512 hash algorithms and
# prints out their hash numbers.
# @param text The string to compute hashes for.
##
def print_results(text):
    print("Hash results from imported file:\n")
    print("md5:", md5_hash(text))
    print("\nSHA-224:", sha_224(text))
    print("\nSHA-256:", sha_256(text))
    print("\nSHA-384:", sha_384(text))
    print("\nSHA-512:", sha_512(text))

##
# Asks the user for the name of the text file, reads that file and returns a 
# string containing all the text in a file.
# @return A string containing all the text in the file specified.
##
def read_file():
    filename = input("Enter filename to input: ")
    try:
        # Open the file
        file = open(filename, 'r', encoding="utf-8")
        # Read the file
        contents = file.read()
        # Return the contents
        return contents
    except FileNotFoundError:
        print("File not found, program exiting.")
        sys.exit(0)

##
# Main method, runs the program.
##
def main():
    print_results(read_file())

# Run the program
main()