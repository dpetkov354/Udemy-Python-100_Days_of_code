alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(plain_text, shift_amount):
    if direction == "encode":
        split_word = []
        shifted_word = []
        for letter in plain_text:
            split_word.append(letter)
        for check in split_word:
            shifted_letter = int(alphabet.index(check)) + shift_amount
            if shifted_letter > 25:
                shifted_letter = shifted_letter - 26
            shifted_word.append(alphabet[shifted_letter])
        print(''.join(shifted_word))
    elif direction == "decode":
        split_word = []
        shifted_word = []
        for letter in plain_text:
            split_word.append(letter)
        for check in split_word:
            shifted_letter = int(alphabet.index(check)) - shift_amount
            if shifted_letter < 1:
                shifted_letter = shifted_letter + 26
            shifted_word.append(alphabet[shifted_letter])
        print(''.join(shifted_word))


caesar(plain_text=text, shift_amount=shift)
