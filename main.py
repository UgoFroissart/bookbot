def get_book_text(filepath):
    with open (filepath) as frankenstein:
        file_contents = frankenstein.read()
    return file_contents

def count_words(file_contents):
    words_splits = file_contents.split()
    word_count = 0
    for word in words_splits:
        word_count += 1 
    return word_count
    
def main():
    file_contents = get_book_text("books/frankenstein.txt")
    num_words = count_words(file_contents)
    print(f"Found {num_words} total words")


main()