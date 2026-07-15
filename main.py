from pathlib import Path
from stats import word_count, character_count, chars_dict_to_sorted_list

def get_book_text(file_path):
    """Reads the content of a text file and returns it as a string."""
    path = Path(file_path)
    with path.open(encoding='utf-8') as file:
        content = file.read()
    return content

def print_report(book_path: str, word_count: int, sorted_chars: list[tuple[str,int]]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for x,y in sorted_chars:
        if x.isalpha():
            print(f"{x}: {y}")
        # for y,d in x:
            # print(y,d)
        
    print("============= END ===============")


def main():
    file_path = 'books/frankenstein.txt'  # Replace with your file path
    book_text = get_book_text(file_path)
    book_words = word_count(book_text)
    book_characters = character_count(book_text)
    sorted_characters = chars_dict_to_sorted_list(book_characters)
    print_report(file_path, book_words, sorted_characters)

main()