from pathlib import Path

def get_book_text(file_path):
    """Reads the content of a text file and returns it as a string."""
    path = Path(file_path)
    with path.open(encoding='utf-8') as file:
        content = file.read()
    return content

def word_count(text):
    """Counts the number of words in a given text string."""
    words = text.split()
    return len(words)

def main():
    file_path = 'books/frankenstein.txt'  # Replace with your file path
    book_text = get_book_text(file_path)
    print(book_text)

main()