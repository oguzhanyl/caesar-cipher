alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    new_text = []
    for i in text:
        # To fix the spacing error
        if i == " ":
            i = " "
        else:
            x = alphabet.index(i) + shift
            # To fix list out of range error
            if x > 25:
                x -= 26
                i = alphabet[x]
            else:
                i = alphabet[x]
        new_text.append(i)
    # To combine encrypted letters
    concat_text = "".join(new_text)
    print("The encoded text is : " + concat_text)

def decode(text, shift):
    new_text = []
    for i in text:
        # To fix the spacing error
        if i == " ":
            i = " "
        else:
            x = alphabet.index(i) - shift
            # To fix list out of range error
            if x < 0:
                x += 26
                i = alphabet[x]
            else:
                i = alphabet[x]
        new_text.append(i)
    # To combine encrypted letters
    concat_text = "".join(new_text)
    print("The decoded text is : " + concat_text)

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decode(text,shift)


# Second way
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
  
# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#       position = alphabet.index(letter)
#       new_position = position + shift_amount
#       cipher_text += alphabet[new_position]
#     print(f"The encoded text is {cipher_text}")
  
# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#       position = alphabet.index(letter)
#       new_position = position - shift_amount
#       plain_text += alphabet[new_position]
#     print(f"The decoded text is {plain_text}")
  
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)