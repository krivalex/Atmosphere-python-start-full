# Миссия: Копирование структуры

# импорт библиотек
from tqdm import tqdm

# импорт библиотек
import time
import keyboard
import pickle

# подключаемся к серверу
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# пишем функцию для сортировки пары


def sortPair(val1, val2):
    # если первое значение больше второго
    if val1 > val2:
        # меняем их местами
        return val2, val1
    # иначе возвращаем их как есть
    else:
        # возвращаем их как есть
        return val1, val2


# функция для копирования структуры
def copyScructure(x1, y1, z1, x2, y2, z2) -> list:
    # сортируем точки
    x1, x2 = sortPair(x1, x2)
    y1, y2 = sortPair(y1, y2)
    z1, z2 = sortPair(z1, z2)

    # считаем размеры структуры
    width = x2 - x1
    height = y2 - y1
    depth = z2 - z1

    # создаем пустой список
    structure = []
    print("Copying structure...")

    # открываем файл для записи
    with open("structure.txt", "wb") as f:
        # проходимся по высоте
        for y in tqdm(range(height)):
            # создаем пустой список
            structure.append([])
            # проходимся по глубине
            for z in range(depth):
                # создаем пустой список
                structure[y].append([])
                # проходимся по ширине
                for x in range(width):
                    # получаем блок с датой
                    structure[y][z].append(
                        mc.getBlockWithData(x1 + x, y1 + y, z1 + z))
        # записываем структуру в файл
        pickle.dump(structure, f)
    # возвращаем структуру
    print("Structure copied.")
    return structure


# функция для вставки структуры
def buildStructure():
    # первая точка
    while not keyboard.is_pressed("up"):
        print("Выберите первую точку")
        # получаем координаты первой точки
        x1, y1, z1 = mc.player.getTilePos()

    # вторая точка
    while not keyboard.is_pressed("down"):
        print("Выберите вторую точку")
        # получаем координаты второй точки
        x2, y2, z2 = mc.player.getTilePos()

    # получаем структуру
    structure = copyScructure(x1, y1, z1, x2, y2, z2)
    # получаем координаты игрока
    while not keyboard.is_pressed("left"):
        print("Выберите точку, куда построить")
        # получаем координаты игрока
        x, y, z = mc.player.getTilePos()

        # записываем старовые координаты
        yStart = y
        xStart = x
        zStart = z

        print("Building structure...")

        # открыли файл для чтения
        with open("structure.txt", "rb") as f:
            # загрузили структуру из файла
            structure = pickle.load(f)
            # проходимся по высоте
            for y in tqdm(range(len(structure))):
                # проходимся по глубине
                for z in range(len(structure[y])):
                    # проходимся по ширине
                    for x in range(len(structure[y][z])):
                        # получаем блок
                        time.sleep(0.01)
                        # если блок не пустой
                        if structure[y][z][x].id != 0:
                            # ставим блок
                            mc.setBlock(xStart + x, yStart + y, zStart + z,
                                        structure[y][z][x].id, structure[y][z][x].data)


# запускаем функцию
buildStructure()
