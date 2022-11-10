
# Миссия: строим разноцветный столб

# одномерный массив
import time
from mcpi.minecraft import Minecraft
oneDimensionalArray = [0, 1, 2, 3, 4, 5]

# подключаемся к серверу
mc = Minecraft.create()

# получаем координаты игрока
x, y, z = mc.player.getTilePos()

# пробегаемся по одномернмоу массиву
for i in oneDimensionalArray:
    # устанавливаем блоки
    mc.setBlock(x+i, y, z, 35, oneDimensionalArray[i])


# Миссия: строим разноцветную плоскость

# подключаемся к серверу
mc = Minecraft.create()

# создаем двумерный массив
twoDimensionalArray = [
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4, 4],
    [5, 5, 5, 5, 5, 5]
]

# получаем координаты игрока
x, y, z = mc.player.getTilePos()

# пробегаемся по двумерному массиву
# устанавливаем блоки
start_x = x
for row in twoDimensionalArray:
    for color in row:
        mc.setBlock(x, y, z, 35, color)
        # увеличиваем координату x на 1, чтобы установить следующий блок
        x += 1
    # увеличиваем координату у на 1, чтобы установить следующую строку
    y += 1
    x = start_x


# повторяем индексы
scores = [1, 5, 6, 10]
print(scores[2])

# создаем вмерный массив
twoDimensionalArray = [
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 100, 2],
    [3, 3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4, 4],
    [5, 5, 5, 5, 5, 5]
]

# выводим его
print(twoDimensionalArray)

# индексация двумерного массива
twoDimensionalArray[2][4] = 2

print(twoDimensionalArray)


# Миссия: пиксель арт

mc = Minecraft.create()

# получаем координаты игрока
x, y, z = mc.player.getTilePos()

# создаем двумерный массив с блоками
blocks = [
    [35, 35, 133, 133, 133, 133, 35, 35],
    [35, 133, 35, 35, 35, 35, 133, 35],
    [133, 35, 22, 35, 35, 22, 35, 133],
    [133, 35, 35, 35, 35, 35, 35, 133],
    [133, 35, 20, 35, 35, 20, 35, 133],
    [133, 35, 35, 20, 20, 35, 35, 133],
    [35, 133, 35, 35, 35, 35, 133, 35],
    [35, 35, 133, 133, 133, 133, 35, 35]
]

# устанавливаем блоки
# записываем начальные координаты
start_x = x
# пробегаемся по двумерному массиву
for row in reversed(blocks):
    # пробегаемся по одномерному массиву
    for block in row:
        # устанавливаем блок
        mc.setBlock(x, y, z, block)
        # увеличиваем координату x на 1, чтобы установить следующий блок
        x += 1
    # увеличиваем координату у на 1, чтобы установить следующую строку
    y += 1
    # возвращаем координату x в начальное положение
    x = start_x


# Миссия: трехмерное строительство

# подключаемся к серверу
mc = Minecraft.create()

# получаем координаты игрока
x, y, z = mc.player.getTilePos()

# создаем трехмерный массив
threeDimensionalArray = [
    [
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2, 2],
        [3, 3, 3, 3, 3, 3],
        [4, 4, 4, 4, 4, 4],
        [5, 5, 5, 5, 5, 5]
    ],
    [
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2, 2],
        [3, 3, 3, 3, 3, 3],
        [4, 4, 4, 4, 4, 4],
        [5, 5, 5, 5, 5, 5]
    ],
    [
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2, 2],
        [3, 3, 3, 3, 3, 3],
        [4, 4, 4, 4, 4, 4],
        [5, 5, 5, 5, 5, 5]
    ],
    [
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2, 2],
        [3, 3, 3, 3, 3, 3],
        [4, 4, 4, 4, 4, 4],
        [5, 5, 5, 5, 5, 5]
    ],
    [
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2, 2],
        [3, 3, 3, 3, 3, 3],
        [4, 4, 4, 4, 4, 4],
        [5, 5, 5, 5, 5, 5]
    ],
    [
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2, 2],
        [3, 3, 3, 3, 3, 3],
        [4, 4, 4, 4, 4, 4],
        [5, 5, 5, 5, 5, 5]
    ],
]

# записываем начальные координаты
start_x = x
start_z = z
start_y = y

# пробегаемся по трехмерному массиву
for row in threeDimensionalArray:
    # пробегаемся по двумерному массиву
    for column in row:
        # пробегаемся по одномерному массиву
        for color in column:
            # устанавливаем блок
            mc.setBlock(x, y, z, 35, color)
            # увеличиваем координату x на 1, чтобы установить следующий блок
            x += 1
            time.sleep(0.1)
        # увеличиваем координату у на 1, чтобы установить следующую строку
        y += 1
        # возвращаем координату x в начальное положение
        x = start_x
    # увеличиваем координату z на 1, чтобы установить следующий столбец
    y = start_y
    # возвращаем координату y в начальное положение
    z += 1
