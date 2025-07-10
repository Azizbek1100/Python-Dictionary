def count_letters(text: str) -> dict[str, int]:
    freq = {}
    for char in text:
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    return freq

text = "assalomu alaykum"
print(count_letters(text))
