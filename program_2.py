import string

def analyze_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()

    total_words = len(words)

    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    palindromes = []

    for word in frequency:
        if len(word) > 1 and word == word[::-1]:
            palindromes.append(word)

    print("\n--- Text Analysis Report ---")
    print("Total Words:", total_words)

    print("\nWord Frequency:")
    for word, count in frequency.items():
        print(word, ":", count)

    print("\nPalindrome Words:")
    if palindromes:
        print(", ".join(palindromes))
    else:
        print("No palindrome words found.")


print("Enter text (press Enter twice to finish):")

lines = []

while True:
    line = input()

    if line == "":
        break

    lines.append(line)

text = " ".join(lines)

analyze_text(text)