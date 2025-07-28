from stats import get_num_words

from stats import character

from stats import sorted_hat

import sys

def get_book_text (filepath):
    contents = filepath.read()
    return contents

def main ():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    with open(sys.argv[1]) as path:
       book_text = get_book_text(path)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")


    word_count = character(book_text)
    

    sorted_word_count = sorted_hat(word_count)
    for char in sorted_word_count:
        print(f"{char["char"]}: {char["num"]}")

    print("============= END ===============")

main()

