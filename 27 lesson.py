# делаем импорты
from tqdm import tqdm

# создаем простые переменные
a = 16
b = 24
c = 25

# делаем тестовые функции


def plus1(a, b):
    # создаем абсурдно большой цикл
    for i in tqdm(range(100000000000000000)):
        a += 1
    return a + b

# тестовая функция


def plus2(a, b, c):
    return a + b + c


# запускаем функцию
print(plus1(a, b))
print(plus2(a, b, c))


# тоже самое
def minus1(a, b):
    return a - b


def minus2(a, b, c):
    return a - b - c


print(minus1(a, b))
print(minus2(a, b, c))


# открываем файл
nameFile = open("names.txt", "r", encoding="utf-8")
# читаем его
print(nameFile.read())
# закрываем файл
nameFile.close()

# открываем файлы с помощью менеджера контекста
with open("names.txt", "r", encoding="utf-8") as nameFile:
    print(nameFile.read())


# Миссия

# пишем свою базу данных

# функция для подсчета всех имен
def all_counter() -> str:
    count = 0
    # открываем файл
    with open("names.txt", "r", encoding="utf-8") as nameFile:
        # проходимся по каждой строке
        for name in nameFile:
            # считаем количество строк
            count += 1
    # возвращаем количество строк
    return "Всего имен: " + str(count)


# функция для подсчета одного имени
def name_counter(name: str) -> str:
    # создаем переменную для подсчета
    count = 0
    # открываем файл
    with open("names.txt", "r", encoding="utf-8") as nameFile:
        # проходимся по каждой строке
        for name_index in nameFile:
            # если имя совпадает с именем из функции
            if name_index == name + '\n':
                # увеличиваем счетчик
                count += 1
    # возвращаем количество имен
    return "Всего имен: " + name + " " + str(count)


# функция для добавления имени
def name_add(name: str) -> str:
    # открываем файл на добавление
    with open("names.txt", "a", encoding="utf-8") as nameFile:
        # добавляем имя
        nameFile.write(name + '\n')
    # возвращаем сообщение
    return name + " добавлено в файл"


# функция для удаления имени
def name_delete(name: str) -> str:
    # открываем файл на чтение
    with open("names.txt", "r", encoding="utf-8") as nameFile:
        # читаем файл
        names = nameFile.readlines()
        # сохраняем длину списка
        count = len(names)
    # открываем файл на запись
    with open("names.txt", "w", encoding="utf-8") as nameFile:
        # проходимся по каждому имени
        for name_index in names:
            # если имя не совпадает с именем из функции
            if name_index != name + '\n':
                # записываем имя в файл
                nameFile.write(name_index)
                # уменьшаем количество имен
                count -= 1
    # возвращаем сообщение
    return name + " удалено из файла" + " " + str(count)


# функция для обновления всех имен
def update_name(old_name: str, new_name: str) -> str:
    # открываем файл на чтение
    with open("names.txt", "r", encoding="utf-8") as nameFile:
        # читаем файл
        names = nameFile.readlines()
        # сохраняем длину списка
        count = len(names)
    # открываем файл на запись
    with open("names.txt", "w", encoding="utf-8") as nameFile:
        # проходимся по каждому имени
        for name_index in names:
            # если имя не совпадает с именем из функции
            if name_index != old_name + '\n':
                # записываем имя в файл
                nameFile.write(name_index)
                # уменьшаем количество имен
                count -= 1
            # если имя совпадает с именем из функции
            else:
                # записываем новое имя в файл
                nameFile.write(new_name + '\n')

    # возвращаем сообщение
    return old_name + " изменено на " + new_name + " " + str(count)


# центральная функция
def main():
    print(all_counter())
    print(name_counter("Милана"))
    print(name_add("Александр"))
    print(name_delete("Венера"))
    print(update_name("Амбер", "Джамал"))
    print(update_name("Камшат", "Адиль"))


# запуск программы
if __name__ == "__main__":
    main()
