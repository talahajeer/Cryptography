from ceasar_encryption.ceasar_encryption import *

def test_cipher():
    pins = [
        "azy",
        "TaLa" ,
        "LET US PLAY"
    ]
    actual = []
    for pin in pins:
        key = random.randint(1, 26)
        encrypted_pin = encrypt2(pin, key)
        decrypted_pin = decrypt(encrypted_pin,key)
        actual.append(decrypted_pin)
    expected = [
        "azy",
        "TaLa" ,
        "LET US PLAY"
    ]
    assert actual == expected

def test_cipher_cracker():
    word =  "It was the best of times, it was the worst of times"
    key = random.randint(1, 26)
    encrypted = encrypt2(word, key)
    actual = crack(encrypted)
    expected = word

  
  
    assert actual == expected