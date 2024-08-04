alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position+shift_key)%26
            cipher_text +=alphabet[new_position]
        else:
            cipher_text += char
    print(f"here's is the text after encryption: {cipher_text}")
def decryption(cipher_text,shift_key):
    plain_text=""
    for char in cipher_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position-shift_key)%26
            plain_text +=alphabet[new_position]
        else:
            plain_text += char
    print(f"here's is the text after decryption: {plain_text}")

want_to_end=False
while not want_to_end:
    what_to_do=input("Type 'encrypt' for encryption,type 'decrypt' for decryption: \n")
    text=input("enter your message:\n").lower()
    shift_number=int(input("Enter shift key:\n"))
    if what_to_do=="encrypt":
        encryption(plain_text=text,shift_key=shift_number)
    elif what_to_do=="decrypt":
        decryption(text,shift_number)
    play_again=input("type 'yes' to continue,type 'no' to exit.\n")
    if play_again=='no':
        want_to_end=True
        print("BYE...!")