def anti_vowel(text: str) -> str:
    result = ""
    for char in text:
        if char not in "aeiouAEIOU":
            result += char
    return result
