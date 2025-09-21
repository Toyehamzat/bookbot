import sys
from stats import get_char_count, get_num_words, char_sort


def get_book_text(file_path):
    with open(file_path, encoding="utf-8") as f:
        file_content = f.read()
    return file_content



def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(get_num_words(book_text), "words found in the document")
    print("------- Character Count --------")
    print(char_sort(get_char_count(book_text)))
    print("============= END ===============")


main()
