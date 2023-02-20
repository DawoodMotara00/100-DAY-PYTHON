alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

on = True


def caesar():
    while on:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, type 'close' to close:\n").lower()
        if direction == "encode" or direction == "decode" or direction == "close":
            if direction == "close":
                print("thank you for using this service")
                exit()
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))

            if direction == "decode":
                shift *= -1
            x = []
            for letter in text:
                a = alphabet.index(letter)
                x.append(alphabet[a + shift])
            outcome = "".join(x)
            print(outcome)
        else:
            continue


caesar()
