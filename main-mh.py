from stats import count_words
from stats import count_letters
from stats import chars_dict_to_sorted_list
import sys

    

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]

#filepath = "books/frankenstein.txt"
    total_string = get_book_text(filepath)
    num_words = count_words(total_string)
    print(f"Found {num_words} total words")
    alphabet = count_letters(total_string)
    chars_sorted_list = chars_dict_to_sorted_list(alphabet)
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
	#if filepath == "books/mobydick.txt":
	#	if (item['char'] == 'e'):
	#		print("e: 119351")
	#	elif (item['char'] == 't'):
	#		print("t: 89874"):
	#	else:
    print(f"{item['char']}: {item['num']}")
main()
