def get_num_words(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    char_count = {}
    for char in text:
        lowercase_char = char.lower()
        if lowercase_char in char_count:
            char_count[lowercase_char] += 1
        else:
            char_count[lowercase_char] = 1
    return char_count


def char_sort(char_count):
    def sort_on(item):
        return item["num"]

    char_list = []
    for char, num in char_count.items():
        char_list.append({"char": char, "num": num})

    char_list.sort(reverse=True, key=sort_on)
    return char_list