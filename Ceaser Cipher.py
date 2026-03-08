import art
print(art.logo)

should_continue = True



def ceaser(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:

            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position = shifted_position % len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


while should_continue:
    alphabet = ["a", "b", "c", "d", "e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    direction = input("Type 'encode to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(text, shift, direction)
    restart = input("Type 'Yes' if you want to go again. Otherwise, type 'No.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")
