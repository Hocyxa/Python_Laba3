import json
from tqdm import tqdm


def read_data(path: str) -> list:
    with open(path, mode='r') as read_from:
        _data = json.load(read_from)
        return _data


def insertion_sort(list1):
    # Outer loop to traverse through 1 to len(list1)
    with tqdm(list1, desc='Сортиртировка') as progressbar:
        for i in range(1, len(list1)):
            j = i
            while j >= 0 and int(list1[j - 1]['age']) > int(list1[j]['age']):
                list1[j - 1], list1[j] = list1[j], list1[j - 1]
                j -= 1
            progressbar.update(1)
        progressbar.update(1)
    return list1


"""data = read_data("C:/Users/matro/PycharmProjects/Python_Laba3/75_result_to_sort.txt")
sort_data = insertion_sort(data)
with open('75_sorted.txt', mode='w') as write_to_file:
    json.dump(sort_data, write_to_file, ensure_ascii=False, indent=1)
with open('75_sorted.txt', 'r') as file:
    print_data = json.load(file)
print(print_data)
"""