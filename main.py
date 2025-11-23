from stats import words_numbers, counting_caracters, sorting_list
import sys

def get_book_text(path):
    file = ""
    with open(path) as f:
        file = f.read()
    return file
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    string = get_book_text(sys.argv[1])
    count = words_numbers(string)
    char_count = counting_caracters(string)
    sorted_list = sorting_list(char_count)
    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for char in sorted_list:
        if char.isalpha():
            print(f"{char}: {sorted_list.get(char)}")
    print("============ END ============")

main()
