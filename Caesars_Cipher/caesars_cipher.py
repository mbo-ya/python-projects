import string

text = 'Love is tough but loneliness is twice as hard,'
shift = 3

def caesar(message, offset, direction=1):
    alphabet = string.ascii_letters + string.punctuation
    # alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message:
    # for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            encrypted_text += alphabet[new_index]
    
    return encrypted_text


encryption = caesar(text, shift)
print(encryption)

decryption = caesar(encryption, shift, -1)
print(decryption)