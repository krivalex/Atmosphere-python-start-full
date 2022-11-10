# создаем двумерный массив
from mcpi.minecraft import Minecraft
import time
import keyboard
import random
array = [
    [1, 2, 3],
    [4, 5, 6],
]

# пробегаемся по двумерному массиву
for i in array:
    for j in i:
        # выводим элементы массива
        print(j)


# проверим если в сендвиче есть рыба, то мы не будем его есть

# создаем сендвич
sandwich = ['bread', 'cheese', 'bread']

# пробегаемся по сендвичу
for ingredient in sandwich:
    # выводим ингредиенты
    print(ingredient)
    # если ингредиент равен рыбе
    if ingredient == "fish":
        # выводим сообщение
        print("Fish doesn't tasty")
        # останавливаем цикл
        break
    # если любой ингредиент кроме рыбы
    else:
        print("It's a good sandwich")
# если цикл отработал до конца
else:
    print("That's are full sandwich")


# Генерация случайного паттерна

# создаем пустой массив
randomNumbers = []

# запускаем повторение на 10 раз
for outer in range(10):
    # добавляем пустой массив
    randomNumbers.append([])
    # запускаем повторение на 10 раз
    for inner in range(10):
        # генерируем случайное число от 1 до 100
        number = random.randint(1, 100)
        # добавляем число в массив
        randomNumbers[outer].append(number)
print(randomNumbers)


# Миссия: Многофункциональное программирование

# импорт библиотек

# подлючаем библиотеку
mc = Minecraft.create()

# создаем функцию для генерации радужных блоков


def rainbow_wool_generation(width: int, height: int) -> list:
    # создаем пустой массив
    randomColors = []

    # запускаем повторение на ШИРИНУ раз
    for outer in range(width):
        # добавляем пустой массив
        randomColors.append([])
        # запускаем повторение на ВЫСОТУ раз
        for inner in range(height):
            # генерируем случайный цвет
            color = random.randint(0, 15)
            # добавляем цвет в массив в кортежа из 35, цвет
            randomColors[outer].append((35, color))

    # возвращаем массив
    return randomColors


# создаем функцию для генерации каменных кирпичей
def stone_bricks_generation(width: int, height: int) -> list:
    # создаем пустой массив
    stoneBlocks = []
    # создаем массив для разеых камней
    blocksToUse = [(1, 0), (1, 1), (1, 2), (1, 3),
                   (1, 4), (1, 5), (1, 6), (7, 0)]

    # запускаем повторение на ШИРИНУ раз
    for outer in range(width):
        # добавляем пустой массив
        stoneBlocks.append([])
        # запускаем повторение на ВЫСОТУ раз
        for inner in range(height):
            # генерируем случайный камень
            stoneBlocks[outer].append(random.choice(blocksToUse))

    # возвращаем массив
    return stoneBlocks


# пишем основную функцию
def generation() -> None:
    """Generates a random pattern of wool blocks in the air."""
    # получаем координаты игрока
    x, y, z = mc.player.getTilePos()
    # уменьшаем высоту на 1
    y -= 1
    # создаем итоговый массив
    blocks = []
    print("Generating...")

    # если нажата клавиша вверх
    if keyboard.is_pressed('up'):
        blocks = rainbow_wool_generation(100, 100)
    # если нажата клавиша вниз
    elif keyboard.is_pressed('down'):
        blocks = stone_bricks_generation(100, 100)

    # ставим стартовую точку по оси Х
    start_x = x
    # пробегаемся по двумерному массиву
    for array in blocks:
        # пробегаемся по одномерному массиву
        for block in array:
            # добавляем паузу
            time.sleep(0.05)
            # устанавливаем блоки
            mc.setBlock(x, y, z, block[0], block[1])
            # увеличваеи координату по оси Х
            x += 1
        # увеличиваем координату по оси Z
        z += 1
        # устанавливаем координату по оси Х на стартовую
        x = start_x


# запускаем основную функцию
if __name__ == "__main__":
    # запускаем бесконечный цикл
    while True:
        # запускаем функцию
        generation()
        # добавляем паузу
        if keyboard.is_pressed('esc'):
            break


# индексиця в трехмерных списках

# импортируем библиотеки

# создаем трехмерный массив
cube = [[[57, 57, 57, 57],
         [57, 0, 0, 57],
         [57, 0, 0, 57],
         [57, 57, 57, 57]],

        [[57, 0, 0, 57],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [57, 0, 0, 57]],

        [[57, 0, 0, 57],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [57, 0, 0, 57]],

        [[57, 57, 57, 57],
         [57, 0, 0, 57],
         [57, 0, 0, 57],
         [57, 57, 57, 57]]]

# индексируем один блок в верстак
cube[3][3][2] = 58

# создаем подключение к майнкрафту
mc = Minecraft.create()

# получаем координаты игрока
x, y, z = mc.player.getTilePos()

# пробегаемся по трехмерному массиву
for array in cube:
    # пробегаемся по двумерному массиву
    for array2 in array:
        # пробегаемся по одномерному массиву
        for block in array2:
            # устанавливаем блок
            mc.setBlock(x, y, z, block)
            time.sleep(0.2)
            # увеличиваем х на 1
            x += 1
        # увеличиваем z на 1
        z += 1
        # сбрасываем х на стартовую
        x -= 4
    # увеличваем у на 1
    y += 1
    # сбрасываем z на стартовую
    z -= 4
