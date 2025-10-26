# main.py
def caesar_encrypt(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result
if __name__ == "__main__":
    original_text = "hello world"
    encrypted_text = caesar_encrypt(original_text, 3)
    print(f"Original: {original_text}")
    print(f"Encrypted: {encrypted_text}")  # Expected: "khoor zruog"
def caesar_decrypt(text: str, shift: int) -> str:
    return caesar_encrypt(text, -shift)
def brute_force_caesar(filename_in: str, filename_out: str):
    with open(filename_in, 'r', encoding='utf-8') as f:
        encrypted_text = f.read()
    for shift in range(1, 26):
        decrypted_text = caesar_decrypt(encrypted_text, shift)
        print(f"Shift {shift}: {decrypted_text[:100]}...")  
    correct_shift = 3 
    final_decrypted = caesar_decrypt(encrypted_text, correct_shift)
    with open(filename_out, 'w', encoding='utf-8') as f:
        f.write(final_decrypted)
if __name__ == "__main__":
    brute_force_caesar("secret", "non_secret")