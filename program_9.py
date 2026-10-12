
def clean_text(text):
    return ''.join(char.lower() for char in text if char.isalnum())


def are_anagrams(text1, text2):
    return sorted(clean_text(text1)) == sorted(clean_text(text2))


def create_pattern_key(text):
    cleaned = clean_text(text)
    frequency = {}

    for char in cleaned:
        frequency[char] = frequency.get(char, 0) + 1

    return tuple(sorted(frequency.items()))


def find_anagrams(words):
    groups = {}

    for word in words:
        key = create_pattern_key(word)
        groups.setdefault(key, []).append(word)

    return [group for group in groups.values() if len(group) > 1]


# Example
word1 = "Listen"
word2 = "Silent"

print("Are anagrams:", are_anagrams(word1, word2))

words = ["listen", "silent", "enlist", "hello", "below", "elbow"]

print("Anagram Groups:", find_anagrams(words))