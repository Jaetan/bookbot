"""Bookbot, an exercise from Boot.dev"""

def count_words(text: str) -> int:
    """Returns the number of words in a given text."""
    return len(text.split())

def count_characters(text: str) -> dict[str, int]:
    """Returns the alphabetic characters' frequencies in given text."""
    frequencies: dict[str, int] = {}
    for each_char in text:
        if not each_char.isalpha():
            continue
        key_for_char = each_char.lower()
        if key_for_char in frequencies:
            frequencies[key_for_char] += 1
        else:
            frequencies[key_for_char] = 1
    return frequencies

BOOK = "books/frankenstein.txt"
with open(BOOK, encoding='utf-8') as file:
    book_text = file.read()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(book_text)} found in the document")
    print()
    for char, count in count_characters(book_text).items():
        print(f"The '{char}' character was found {count} times")
    print("--- End of report ---")
