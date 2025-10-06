import sys

from stats import count_words
from stats import count_characters
from stats import sort_dictionnary

def get_book_text(filepath):
    with open (filepath) as frankenstein:
        file_contents = frankenstein.read()
    return file_contents
    
def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]


    file_contents = get_book_text(book_path)

    num_words = count_words(file_contents)

    num_characters = count_characters(file_contents)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    list_dictionnary = sort_dictionnary(num_characters)
    for entry in list_dictionnary:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")

main()