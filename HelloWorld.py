def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted = ord(char) + shift
            if shifted > ord('z'):
                shifted -= 26
            char = chr(shifted)
            if is_upper:
                char = char.upper()
        encrypted_text += char
    return encrypted_text

def encrypt_file(input_file, output_file, shift):                                       #makes it possible to create a new file with the encrypted text
    try:
        with open(input_file, 'r') as file:                                             #opens the inputed file
            plain_text= file.read()                                                     #reads the file
            encrypted_text = caesar_cipher(plain_text, shift)                           #encrypts the file 

        with open(output_file, 'w') as file: 
            file.write(encrypted_text)
        print(f'File "{input_file}" encrypted successfully.')
    except FileNotFoundError:
        print(f'File not Found: "{input_file}"')
    except Exception as e:
        print(f'An error occured: {str(e)}')

import random
import argparse 
input_file= ""
output_file= "encrypted_file.txt"

if __name__ == "__main__":                                                             #prompts the user to enter the file pathway 
    parser= argparse.ArgumentParser(description= "Caesar Cipher encryption")           #defines the command-line arguments that the script needs 
    parser.add_argument("input_file", help="Path to the file you want to encrypt")
    parser.add_argument("shift", type=int, help="Caesar Cipher shift value")
    
    file_path= input("Enter file path here:")                                          #asks the user to put in the file path
    shift= random.randint(1,25)                                                        #makes the shift of the text random 
   
    encrypt_file(input_file, output_file, shift)                                      #encrypts the input_file and puts it in the output_file 
    print(f"File '{input_file}' encrypted and saved as '{output_file}'.")



#args= parser.parse_args()