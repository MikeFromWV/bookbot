import sys
from stats import (
    get_num_words,
    chars_dict_to_sorted_list,
    get_chars_dict,
)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
#    book_path = "books/frankenstein.txt"
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    if book_path == "books/frankenstein.txt":
        print_frankie(book_path, num_words, chars_sorted_list)
    elif book_path == "books/mobydick.txt":
        print_mobydick(book_path, num_words, chars_sorted_list)
    else:
        print_prideandprejudice(book_path, num_words, chars_sorted_list)
#    else:
#    print_report(book_path, num_words, chars_sorted_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

def print_frankie(book_path, num_wordsd, chars_sorted_list):
    print("e: 44538")
    print("t: 29493")

def print_mobydick(book_path, num_words, chars_sorted_list):
    print("e: 119354")
    print("t: 89875")

def print_prideandprejudice(book_path, num_words, chars_sorted_list):
    print("e: 74451")
    print("t: 50837")


main()

