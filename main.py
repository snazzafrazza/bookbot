def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_book_text(path_to_file)
    total_words = count_words(file_contents)
    
    word_count_dict = count_chars(file_contents)
    sorted_list_dict = sort_dict(word_count_dict)

    print("--- Begin report of {} ---".format(path_to_file))
    print("{} words found in document\n\n".format(total_words))

    for item in sorted_list_dict:
        if not item["char"].isalpha():
            continue
        print("The '{}' character was found {} times ".format(item['char'], item['num']))
    print("--- End Report ---")

def get_book_text(path) -> str:
    with open(path) as f:
        return f.read()

def count_words(text) -> int:
    words = text.split()
    return len(words)

def count_chars(text) -> dict:
    word_count_dict = {}
    unique_char_set = set(text.lower())
    char_list = list(text.lower())

    for word in unique_char_set:
        word_counter = 0
        for i in range(0, len(char_list)):
            if word in char_list[i]:
                word_counter += 1            
        word_count_dict[word] = word_counter
    return word_count_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    sorted_list = []
    for k,v in dict.items():
        sorted_list.append({"char" : k, "num" : v})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()
