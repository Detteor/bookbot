from pathlib import Path
from stats import word_count, character_count

def get_book_text(file_path):
    """Reads the content of a text file and returns it as a string."""
    path = Path(file_path)
    with path.open(encoding='utf-8') as file:
        content = file.read()
    return content

def main():
    file_path = 'books/frankenstein.txt'  # Replace with your file path
    book_text = get_book_text(file_path)
    book_words = word_count(book_text)
    book_characters = character_count(book_text)
    # print(book_text)
    print(f"Found {book_words} total words")
    print(book_characters)

main()