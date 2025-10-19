# main.py
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
                result += chr((ord(char) - base +shift) % 26 + base)
            elif char.islower():
                base = ord('a')
                result += chr((ord(char) - base +shift) % 26 + base)
        else:
            result += char

    return result

if __name__ == "__main__":
    original_text = "hello world"
    encrypted_text = caesar_encrypt(original_text, 3)
    print(f"Original: {original_text}")
    print(f"Encrypted: {encrypted_text}") # Expected: "khoor zruog"