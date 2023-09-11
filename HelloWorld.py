import string

regular_file = "hello world"
shift = 1

alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)

encrypted = regular_file.translate(table)
print(encrypted)