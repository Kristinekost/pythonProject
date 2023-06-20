def inputs():
    Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 25:
        shift = (shift % 25) - 1
    return Alphabet, direction, text, shift

def caesar():
    Alphabet, cipher_direction, start_text, shift_amount = inputs()
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for each_letter in start_text:
        if each_letter in Alphabet:
            position = Alphabet.index(each_letter)
            new_position = position + shift_amount
            end_text += Alphabet[new_position]
        else:
            end_text += each_letter
    print(f"The {cipher_direction}d text is {end_text}")
    restart = input(" Do you want restart the Cipher program?")
    if restart == 'yes':
        caesar()
    else:
        return


caesar()
