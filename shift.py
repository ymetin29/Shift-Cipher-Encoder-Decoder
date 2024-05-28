from itertools import cycle

def paddingkey(plaintext, key):
    paddedkey = ''
    i = 0
    for char in plaintext:
        if char.isalpha():
            paddedkey += key[i % len(key)]
            i += 1
        else:
            paddedkey += ' '
    return paddedkey
    
def substitutechar(plaintextchar, keychar, mode='encrypt'):
    if plaintextchar.isalpha():
        first_alphabet_letter = 'a'
        if plaintextchar.isupper():
            first_alphabet_letter = 'A'

        old_char_position = ord(plaintextchar) - ord(first_alphabet_letter)
        keychar_position = ord(keychar.lower()) - ord('a')

        if mode == 'encrypt':
            new_char_position = (old_char_position + keychar_position + 1) % 26
        else:
            new_char_position = (old_char_position - keychar_position + 25) % 26
        return chr(new_char_position + ord(first_alphabet_letter))
    return plaintextchar

def encrypt(plaintext, key):
    ciphertext = ''
    paddedkey = paddingkey(plaintext, key)
    for plaintextchar, keychar in zip(plaintext, paddedkey):
        ciphertext += substitutechar(plaintextchar, keychar)
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    paddedkey = paddingkey(ciphertext, key)
    for ciphertextchar, keychar in zip(ciphertext, paddedkey):
        plaintext += substitutechar(ciphertextchar, keychar, mode='decrypt')
    return plaintext

print("Welcome to the Shift Cipher Algorithm")
def main():
    plaintext = input('Enter a message: ')
    key = "CIPHER"
    ciphertext = encrypt(plaintext, key)
    decryptedplaintext = decrypt(ciphertext, key)
    print("Plaintext:", plaintext.replace(" ", "").upper())
    print("Key:", key.replace(" ", "").upper())
    print("Ciphertext:", ciphertext.replace(" ", "").upper())
    print("Decrypted Plaintext:", decryptedplaintext.replace(" ", "").upper())
    for i, j, z in zip(plaintext.replace(" ", "").upper(), cycle(key.upper()), ciphertext.replace(" ", "").upper()):
                print('{} + {} = {}'.format(i, j, z))
    main()
    
if __name__ == '__main__':
    main()
