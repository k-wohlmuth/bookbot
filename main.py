import sys

def check_arg():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    #sys.exit(0)

def get_book_text(path):
    print(f"Analyzing book found at {path}...")
    with open(path) as p:
        book = p.read()
    return book

from stats import work_count, char_count, sort_dict

def main():
    check_arg()
    print("============ BOOKBOT ============")
    book = get_book_text(sys.argv[1])
    num_words = work_count(book)
    num_char = char_count(book)
    sorted_dict = sort_dict(num_char)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_dict:
        if entry["char"].isalpha():
            print(f'{entry["char"]}: {entry["num"]}')    
    print("============= END ==============")

main()
