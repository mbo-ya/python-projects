import string

text = 'Love is tough but loneliness is twice as hard,'
custom_key = 'python'

# Define a function vigenere() that takes 3 args;
# direction has a default value of 1
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = string.ascii_letters + string.punctuation
    final_message = ''

    for char in message:
    
        # Append space to the message
        if char == ' ':
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message
    
encryption = vigenere(text, custom_key, 1)
print(encryption)
decryption = vigenere(encryption, custom_key, -1)
print(decryption)