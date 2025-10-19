# main.py
def caesar_encrypt(text, shift):
    result = ""
    for i in range(0, len(text)):
        if text[i] != " ":
            result += chr(ord(text[i])+shift)
        else:
            result += text[i]

    return result

if __name__ == "__main__":
    original_text = "hello world"
    encrypted_text = caesar_encrypt(original_text, 3)
    print(f"Original: {original_text}")
    print(f"Encrypted: {encrypted_text}") # Expected: "khoor zruog"