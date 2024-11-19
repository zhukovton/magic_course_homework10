# Создайте функцию для чтения файла.
# Прочитать информацию из файла, если его нет
# - обработать ошибку и вернуть пустую строку.
def read_file(filename):

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = file.readlines()
    except FileNotFoundError:
        return "пустая строка"
    return data


if __name__ == "__main__":
    print(read_file("2.txt"))
