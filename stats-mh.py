def count_words(total_string):
	words =  total_string.split()
	return len(words)
	
def count_letters(string):
    alphabet = {}

    for letter in string:
        letter = letter.lower()
        alphabet[letter] = alphabet.get(letter,0) + 1
    return (alphabet)

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(alphabet):
    sorted_list = []
    for ch in alphabet:
        sorted_list.append({"char": ch, "num": alphabet[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list