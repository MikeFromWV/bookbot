from stats import get_num_words, get_chars_dict, chars_dict_to_sorted_list

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
#    print(text)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"Found {num_words} total words")
    print(chars_dict)



def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
