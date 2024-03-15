"""src.ejercicio_1.palindrome"""

import unicodedata
import re


def normalize(text: str) -> str:
    """Return a normalized version of s."""
    # Remove punctuation
    text = re.sub(r"[^\w\s\']", "", text)
    text = text.lower().replace(" ", "").replace(".", "").replace("'", "")
    # Remove accents and other diacritics
    text = unicodedata.normalize("NFKD", text).encode("ASCII", "ignore").decode("utf-8")
    return text


def is_palindrome(text: str) -> bool:
    """Return True if s is a palindrome, False otherwise."""
    text_normalized = normalize(text)
    return text_normalized == text_normalized[::-1]


def main():
    s = input("Enter a string: ")
    if is_palindrome(s):
        print("It is a palindrome")
    else:
        print("It is not a palindrome")


if __name__ == "__main__":
    main()
