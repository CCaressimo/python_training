alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            shift_position = alphabet.index(letter) + shift_amount
            shift_position %= len(alphabet)
            output_text += alphabet[shift_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")



SHOULD_CONTINUE = True

while SHOULD_CONTINUE:

    direction = input("Type 'encode' to encrypt, type 'decode' to decode\n")
    text = input("Type your message:\n").lower()
    shift = int(input("type the shift number:\n"))

    caeser(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()

    if restart == "no":
        SHOULD_CONTINUE = False
        print("Goodbye")
