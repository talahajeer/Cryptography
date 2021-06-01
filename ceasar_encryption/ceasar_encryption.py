import random
import re
# import snoop
import string
import nltk

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

from nltk.corpus import words, names

word_list = words.words()
name_list = names.words()

# @snoop
def encrypt(plain, key):
    encrypted_text = ""

    for char in plain:
        num = ord(str(char))
        if num + key <= 122:
            shifted_num = (num + key)
        else:
            shifted_num = num + key
            while (shifted_num > 122):
                shifted_num =  ((num + key) %122)+ 65

        encrypted_text += chr(shifted_num)

    return encrypted_text


def decrypt(encoded, key):
    return encrypt(encoded, -key)


alephbet = string.ascii_uppercase 

# @snoop
def encrypt2(plain, key):
    encrypted_text = ""
    plain_len = len(plain)
    for i in range(plain_len):
        char = plain[i]
        if char.isnumeric() or char.isspace() or not char.isalpha():
            encrypted_text += char
            continue
        if char.islower():
            location = alephbet.index(char.upper()) 
            new_location = (location + key) % 26 
            encrypted_text += alephbet[new_location].lower()
        else:
            location = alephbet.index(char) 
            new_location = (location + key) % 26 
            encrypted_text += alephbet[new_location]
        


    return encrypted_text


def decrypt(encoded, key):
    return encrypt2(encoded, -key)


if __name__ == "__main__":
    pass
    pins = [
        "azy",
        "TaLa" ,
        "LET US PLAY"
    ]

    for pin in pins:
        key = random.randint(1, 26)
        print("plain pin", pin)
        encrypted_pin = encrypt2(pin, 1)
        print("encrypted_pin", encrypted_pin)
        decrypted_pin = decrypt(encrypted_pin,1)
        print("decrypted_pin", decrypted_pin)



def count_words(text):

    candidate_words = text.split()

    word_count = 0 

    for candidate in candidate_words:
        word = re.sub(r'[^A-Za-z]+','', candidate)
        if word.lower() in word_list or word in name_list:
            word_count += 1
     
    return word_count

decrypt_word =""

word = 'LET US PLAY'
encrypted = encrypt2(word, 10)
def crack(encrypted):
    percentage_init = 0
    for i in range(len(encrypted.split())*52):
        candidate_dec = decrypt(encrypted, i)
        word_count = count_words(candidate_dec)
        percentage = int(word_count / len(candidate_dec.split()) * 100)
        if percentage > percentage_init:
            percentage_init = percentage 
            decrypt_word = candidate_dec
    return decrypt_word

print("the right decrypt is ", crack(encrypted))