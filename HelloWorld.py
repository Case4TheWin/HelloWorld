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

def encrypt_file(file_path, shift):
    try:
        with open(file_path, 'r') as file:
            plain_text = file.read()
            encrypted_text = caesar_cipher(plain_text, shift)
        with open(file_path, 'w') as file: 
            file.write(encrypted_text)
        print(f'File "{file_path}" encrypted successfully.')
    except FileNotFoundError:
        print(f'File not Found: "{file_path}"')
    except Exception as e:
        print(f'An error occured: {str(e)}')

if __name__ == "__main__":
    file_path = input("Enter the path to the file you want to encrypt: ")
    shift = int(input("Enter the Caesar cipher shift value (1 through 26):"))

    encrypt_file(file_path, shift) 





import string

regular_file = "hello world"
shift = 1

alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)

encrypted = regular_file.translate(table)
print(encrypted)