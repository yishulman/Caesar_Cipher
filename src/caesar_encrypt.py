# main.py
def caesar_encrypt(text, shift):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h","i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    result = ""
    for let in text:
        if let.isupper():
            index=letters.index(let.lower())
            result=result+letters[(index + shift) % len(letters)].upper()
            continue
        if let not in letters:
            result=result+let
            continue
        index=letters.index(let)
        encrypted_let = letters[(index + shift) % len(letters)]
        result=result+encrypted_let
    return result

def decrypt(text):
    for i in range(26):
        print(caesar_encrypt(text, i))

if __name__ == "__main__":
    original_text = "Uvzzrysneo Uvtu Fpubby vf n eryvtvbhf Mvbavfg oblf' uvtu fpubby ybpngrq va gur Onlvg IrTna arvtuobheubbq bs Wrehfnyrz. Vg jnf sbhaqrq va 1920 nf Zvmenḥv Uvtu Fpubby naq zbirq gb vgf pheerag pnzchf va 1968. Gur fpubby vf anzrq nsgre Nzrevpna cuvynaguebcvfg Cnhy Uvzzrysneo."
    encrypted_text = caesar_encrypt(original_text, 3)
    print(f"Original: {original_text}")
    print(f"Encrypted: {encrypted_text}") # Expected: "khoor zruog"
    decrypt(original_text)