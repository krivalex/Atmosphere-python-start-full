# импортируем библиотеки
from mcpi.minecraft import Minecraft
import time
import keyboard

# Узнаем о типе данных - ничего
print(None)
print(type(None))

# Вспоминаем зачем существуют разные типы данных

# массив изменяемый и имеет индексы
array = [1, 2, 3, 4, 5]
array.append(6)
array.remove(3)
array.insert(0, 0)

# кортеж не изменяемый и имеет индексы
tuple = (1, 2, 3, 4, 5)

# словарь изменяемый и не имеет индексов
dict = {
    'name': 'John',
}

# множество изменяемый и не имеет индексов
set = {1, 2, 3, 4, 5}
print(set)
print(type(set))
set.add(6)
print(set)

# пытаемся изменить множество
for i in range(100):
    set.add(5)
print(set)


# O(1) - константная сложность
# множеств и словарей

# O(n) - линейная сложность
# массивов, списков, кортежей


# делаем множество своими руками
for i in range(10):
    for element in array:
        if i not in array:
            array.append(i)

# сделали
print(array)


# подводим итоги
# теперь вы знаете 10 типов данных

# число
number: int = 1
# вещественное число
number: float = 1.0
# строка
message: str = "Hello"
# флаг
is_active: bool = True
# массив
numbers: list = [1, 2, 3, 4, 5]
# кортеж
numbers: tuple = (1, 2, 3, 4, 5)
# множество
numbers: set = {1, 2, 3, 4, 5}
# словарь
numbers: dict = {
    'name': 'John',
}
# ничего
nothing: None = None
# тип
types: type = type(1)


# Миссия: копирование построек - начало


# создаем объект для работы с майнкрафтом
mc = Minecraft.create()

# пишем функцию которая будет всегда возвращать нам правильные координаты


def sortPair(val1, val2):
    if val1 > val2:
        return val2, val1
    else:
        return val1, val2


# пишем функцию которая будет копировать структуру
# принимает в себя координаты начала и конца
def copyStructure(x1, y1, z1, x2, y2, z2):

    # сортируем координаты
    x1, x2 = sortPair(x1, x2)
    y1, y2 = sortPair(y1, y2)
    z1, z2 = sortPair(z1, z2)

    # считаем размеры
    width = x2 - x1
    height = y2 - y1
    length = z2 - z1

    # создаем массив для хранения блоков
    sctructure = []
    print("Создание структуры...")

    # проходимся по всем блокам
    for y in range(height):
        # создаем пустой массив для хранения блоков в высоте
        sctructure.append([])
        # проходимся по всем блокам в высоте
        for z in range(length):
            # создаем пустой массив для хранения блоков в длине
            sctructure[y].append([])
            # проходимся по всем блокам в длине
            for x in range(width):
                # получаем блок и записываем его в массив
                sctructure[y][z].append(mc.getBlock(x1 + x, y1 + y, z1 + z))

    # возвращаем массив
    return sctructure


# пишем функцию которая будет вставлять структуру
def buildScrtucture():
    # пока не нажата клавиша вверх
    while not keyboard.is_pressed('up'):
        # получаем координаты игрока
        print("Выберите первую точку")
        x1, y1, z1 = mc.player.getTilePos()
    # пока не нажата клавиша вниз
    while not keyboard.is_pressed('down'):
        # получаем координаты игрока
        print("Выберите вторую точку")
        x2, y2, z2 = mc.player.getTilePos()

    # запускаем копирование
    structure = copyStructure(x1, y1, z1, x2, y2, z2)

    # пока не нажата клавиша влево
    while not keyboard.is_pressed('left'):
        print("Выберите точку для постройки")
        # получаем координаты игрока
        x, y, z = mc.player.getTilePos()

    # записываем стартовые координаты
    yStart = y
    xStart = x
    zStart = z

    # проходимся по всем блокам
    for y in range(len(structure)):
        # проходимся по всем блокам в высоте
        for z in range(len(structure[y])):
            # проходимся по всем блокам в длине
            for x in range(len(structure[y][z])):
                # ставим блок
                time.sleep(0.2)
                mc.setBlock(xStart + x, yStart + y,
                            zStart + z, structure[y][z][x])


# запускаем функцию
buildScrtucture()


# Примерное обьяснение кода
# Все что внутри функции copyStructure() копирует структуру
# Все что внутри функции buildScrtucture() вставляет структуру
# Все что внутри функции sortPair() сортирует пару чисел
# трехмерные массивы это массивы в массивах в массивах
s = [
    [
        [1, 2, 3], [4, 5, 6], [7, 8, 9]
    ],
    [
        [1, 2, 3], [4, 5, 6], [7, 8, 9]
    ],
    [
        [1, 2, 3], [4, 5, 6], [7, 8, 9]
    ],
]
