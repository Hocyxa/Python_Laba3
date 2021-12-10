import json
from tqdm import tqdm
import argparse
from Sort_and_Valid import MyValidator


class ReadFile:
    """
    Объект класса ReadFile считывает текст из файла и хранит их
    Он нужен для того, чтобы хранить в себе данные из файла
    для дальнейшего использования.
    Attributes
    ----------
    __data - хранит данные из файла
    """

    __data: object

    def __init__(self, path: str) -> None:
        """
        Иизиализирует экземпляр класса ReadFile
        Parameters
        ----------
        path : str
            Путь к файлу
        """

        self.__data = json.load(open(path, encoding='windows-1251'))

    @property
    def data(self) -> object:
        """
        Выполняет доступ к данным экземпляра
        Return
        -------
        object:
            Данные из файла
        """
        return self.__data


parser = argparse.ArgumentParser()
parser.add_argument('-in', type=str, dest="file_input", default='75.txt')
parser.add_argument('-out', type=str, dest="file_output", default='75_result.txt')
args = parser.parse_args()
input_file = ReadFile(args.file_input)
output_file = open(args.file_output, "w", encoding="ascii")
counter_valid = 0
counter_unvalid_of_records = [0, 0, 0, 0, 0, 0, 0, 0, 0]
data_to_save = []
with tqdm(input_file.data, desc='Процесс проверки записей(не выключайте проргамму)') as progressbar:
    for record in input_file.data:
        check = MyValidator.validator(record['email'], record['height'], record['snils'],
                                      record['passport_number'], record['university'], record['age'],
                                      record['political_views'], record['worldview'], record['address'])
        unvalid = check.chek_all()
        if unvalid == 9:
            counter_valid += 1
            data_to_save.append(record)
        else:
            counter_unvalid_of_records[unvalid] += 1
        progressbar.update(1)
    json.dump(data_to_save, output_file)
write_valid_data_to = '75_result_to_sort.txt'
with open(write_valid_data_to, mode='w') as write_to_file:
    json.dump(data_to_save, write_to_file, ensure_ascii=False, indent=1)
all_unvalid_of_record = 0
for elem in counter_unvalid_of_records:
    all_unvalid_of_record += elem
print("Количество валидных записей:", counter_valid)
print("Количество невалидных записей:", all_unvalid_of_record)
print("Количество невалидных email:", counter_unvalid_of_records[0])
print("Количество невалидных записей роста:", counter_unvalid_of_records[1])
print("Количесвто невалидных снилсов:", counter_unvalid_of_records[2])
print("Количество неалидных номеров паспорта", counter_unvalid_of_records[3])
print("Количество невалидных названий университета", counter_unvalid_of_records[4])
print("Количество невалидных возрастов", counter_unvalid_of_records[5])
print("Количество невалидных политических взглядов", counter_unvalid_of_records[6])
print("Количество невалидных вероисповеданий", counter_unvalid_of_records[7])
print("Количество невалидных адресов", counter_unvalid_of_records[8])
output_file.close()
