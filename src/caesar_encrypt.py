# main.py
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            x= ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - x + shift) % 26 + x)
        else:
            result += char
    return result


def caesar_decrypt_bruteforce(text):

    for shift in range(26):
        print( )
        result = ""
        for char in text:
            if 'A' <= char <= 'Z':
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            elif 'a' <= char <= 'z':
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                result += char
        print(f"Shift {shift}: {result}")


if __name__ == "__main__":
    original_text = "hello world"
    encrypted_text = caesar_encrypt(original_text, 3)
    print(f"Original: {original_text}")
    print(f"Encrypted: {encrypted_text}") # Expected: "khoor zruog"
    original=("Uvzzrysneo Uvtu Fpubby vf n eryvtvbhf Mvbavfg oblf' uvtu fpubby ybpngrq va gur Onlvg IrTna arvtuobheubbq bs Wrehfnyrz. Vg jnf sbhaqrq va 1920 nf Zvmenḥv Uvtu Fpubby naq zbirq gb vgf pheerag pnzchf va 1968. Gur fpubby vf anzrq nsgre Nzrevpna cuvynaguebcvfg Cnhy Uvzzrysneo.")
    print(caesar_decrypt_bruteforce(original))