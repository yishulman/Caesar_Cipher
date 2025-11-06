#main
def caesar_encrypt(text, shift):
    result = ""
    char = ''
    for i in text:
        if i.isalpha() and i.islower():
            char = chr(range(ord('a'), ord('z') + 1)[(ord(i) - ord('a') + shift) % 26])
        elif i.isalpha() and i.isupper():
            char = chr(range(ord('A'), ord('Z') + 1)[(ord(i) - ord('A') + shift) % 26])
        else:
            char = i
        result += char
    return result

def decrypt_caesar():
    with open("secret", "r") as f:
        text_to_decrypt = f.read()
        for shift in range(27):
            print("shift: ", shift, ":", caesar_encrypt(text_to_decrypt, shift), "\n\n")
        shift = int(input("Enter the shift you want to use for decripting: "))
        print(caesar_encrypt(text_to_decrypt, shift))

def main():
    decrypt_caesar()

if __name__ == "__main__":
    main()
