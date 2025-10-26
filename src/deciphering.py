def deciphering(text):
    for shift in range(1, 26):#try all possible shifts from 1 to 25
        result = ""
        for char in text:
            if char.islower():
                result += chr((ord(char) - ord("a") - shift) % 26 + ord("a"))#like in the encryption file, only we do the opposite with the shift.
            elif char.isupper():
                result += chr((ord(char) - ord("A") - shift) % 26 + ord("A"))
            else:
                result += char
        print(result + "\n")

file = open("secret", "r")
my_file = file.read().strip()
file.close()
deciphering(my_file)
