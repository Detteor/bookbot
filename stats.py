def word_count(text):
    """Counts the number of words in a given text string."""
    words = text.split()
    return len(words)

def character_count(text):
    for x in text:
        print(x.lower())