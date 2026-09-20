import sys

def caesar_cipher(text, shift):
    result = ""

    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += ch

    return result


# Take input from command line
if len(sys.argv) >= 3:
    text = sys.argv[1]
    shift = int(sys.argv[2])
else:
    text = input("Enter the message: ")
    shift = int(input("Enter the shift key: "))

# Encode
encrypted = caesar_cipher(text, shift)

# Decode
decrypted = caesar_cipher(encrypted, -shift)

print("\nOriginal Text :", text)
print("Shift Key     :", shift)
print("Encrypted Text:", encrypted)
print("Decrypted Text:", decrypted)