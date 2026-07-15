def word_count(text: str) -> int:
    """Counts the number of words in a given text string."""
    words = text.split()
    return len(words)

def character_count(text: str) -> dict[str, int]:
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(text: tuple[str, int]) -> int:
    return text[1]

def chars_dict_to_sorted_list(chars_dict: dict[str,int]) -> list[tuple[str,int]]:
    empty_list = list(chars_dict.items())
    # for k,v in chars_dict.items():
        # print(k)
        # empty_list.append((k,v))
    sorted_list = sorted(empty_list,reverse=True, key=sort_on)

    return sorted_list