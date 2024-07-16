# Caesar Cipher
import art

# Alphabet list
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']

print(art.logo)


def shift_list(shift_num):
    # Shifting the alphabets and storing it in a new list
    temp = []
    # Storing the alphabets from the shift number to the last
    for index in range(shift_num, len(alphabets)):
        temp.append(alphabets[index])
    # Storing the alphabets from the starting to the shift number
    for index in range(0, shift_num):
        temp.append(alphabets[index])
    return temp


# Encrypt function
def encrypt(encode_message, shift_number):
    temp_lst = shift_list(shift_number)

    # Encrypting the message
    encoded_msg = ""
    for char in encode_message:
        if char.isalpha():
            position = alphabets.index(char)
            encoded_msg += temp_lst[position]
        else:
            encoded_msg += char
    print(f"The encoded message is: {encoded_msg}")


def decrypt(decode_message, shift_number):
    temp_lst = shift_list(shift_number)

    decoded_msg = ""
    for char in decode_message:
        if char.isalpha():
            position = temp_lst.index(char)
            new_char = alphabets[position]
            decoded_msg += new_char
        else:
            decoded_msg += char

    print(f"The decoded message is: {decoded_msg}")


repeat_task = "yes"
while repeat_task == "yes":
    # Inputs
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26  # In case the user enters a shift number greater than 26, doing a modulo will reduce the number
    # within 26
    if choice == "encode":
        encrypt(encode_message=message, shift_number=shift)
    elif choice == "decode":
        decrypt(decode_message=message, shift_number=shift)
    else:
        print("You have entered an invalid choice.")

    repeat_task = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
    if repeat_task == "no":
        print("Goodbye!")
