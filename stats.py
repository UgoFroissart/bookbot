def count_words(file_contents):
    words_splits = file_contents.split()
    word_count = 0
    for word in words_splits:
        word_count += 1 
    return word_count

def count_characters(file_contents):
    character_count={}

    for character in file_contents:
        character_lower = character.lower()

        if character_lower in character_count:
            character_count[character_lower] += 1
        else:
            character_count[character_lower] = 1

    return character_count

def sort_dictionnary(num_characters):
    char_list = [{"char": char, "num": num} for char, num in num_characters.items()]

    def get_num(d):
        return d["num"]

    char_list.sort(key=get_num, reverse=True)

    return char_list
