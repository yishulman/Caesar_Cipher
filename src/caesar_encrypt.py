import csv
# main.py

LAST_LETTER_ID_UPPER = ord("Z")
LAST_LETTER_ID_LOWER = ord("z")

FIRST_LETTER_ID_UPPER = ord("A")
FIRST_LETTER_ID_LOWER = ord("a")

LETTER_RANGE = LAST_LETTER_ID_LOWER-FIRST_LETTER_ID_LOWER +1
def caesar_encrypt(text, shift):
    result = ""
    for letter in text:
        if(letter.isalpha()):
            if(letter.isupper()):
                letterID = ord(letter)
                newLetterId = (letterID + shift)%LETTER_RANGE
                while newLetterId > LAST_LETTER_ID_UPPER:
                    newLetterId -= LETTER_RANGE
                while newLetterId <FIRST_LETTER_ID_UPPER:
                    newLetterId += LETTER_RANGE
                newLetter = chr(newLetterId)
                result += newLetter
            else:
                letterID = ord(letter)
                newLetterId = letterID + shift
                while newLetterId > LAST_LETTER_ID_LOWER:
                    newLetterId -= LETTER_RANGE
                while newLetterId < FIRST_LETTER_ID_LOWER:
                    newLetterId += LETTER_RANGE
                newLetter = chr(newLetterId)
                result += newLetter
        else:
            result+= letter
    return result

def bruteForce(text):
    for i in range(1, LETTER_RANGE):
            print(caesar_encrypt(text, -i))
        

if __name__ == "__main__":
    original_text = "hello world"
    encrypted_text = caesar_encrypt(original_text, 3)
    print(f"Original: {original_text}")
    print(f"Encrypted: {encrypted_text}") # Expected: "khoor zruog"
