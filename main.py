def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    counter = count_words(text)
    letter_count = count_letters(text)
    list_dict = dict_in_lst(letter_count)
    list_dict.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{counter} words found in the document")
    for item in list_dict:
        print(f"The {item["letter"]} character was found {item["num"]} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(book_text):
    words = book_text.split()
    return len(words)


def count_letters(text_of_book):
    lowered_text = text_of_book.lower()
    char_dict = {}
    for c in lowered_text:
        if c in char_dict:
            char_dict[c] += 1
        else: 
            char_dict[c] = 1
    return char_dict

def dict_in_lst(dict):
    lst = []
    for key, value in dict.items():
        if key.isalpha():
            new_dict = {"letter": key, "num": value}
            lst.append(new_dict)
    return lst
    
def sort_on(dict):
    return dict["num"]

main()