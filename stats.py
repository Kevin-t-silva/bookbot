def words_numbers(txt):
    count = 0
    txt_sample = txt.split()
    for word in txt_sample:
        count += 1
    return count
def counting_caracters(text):
    text = text.lower()
    char_counter = {}
    for char in text:
        char_counter[char] = char_counter.get(char,0) + 1
    return char_counter
def sorting_list(list):
    sorting_items = sorted(list.items())
    sorted_dic = dict(sorting_items)
    return sorted_dic
