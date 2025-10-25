# main.py
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.islower():
            result += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))#subtract the value of "a" from the ascii value of the "char" and then we get the index of the char in abc and then we check if it exceeds the number of characters there are. Then we add the value of the letter a to the number of shifts that we need to do.
        elif char.isupper():
            result += chr((ord(char) - ord("A") + shift) % 26 + ord("A")) #same as above but for uppercase letters
        else:
            result += char
    return result

if __name__ == "__main__":
    original_text = "hello world"
    encrypted_text = caesar_encrypt(original_text, 3)
    print(f"Original: {original_text}")
    print(f"Encrypted: {encrypted_text}") # Expected: "khoor zruog"