# пишем целую игру на питоне

# импортируем библиотеку для работы с майнкрафтом
from mcpi.minecraft import Minecraft

# импортируем библиотеку для работы со временем
import random
import time

# создаем переменную для работы с майнкрафтом
mc = Minecraft.create()

# берем координаты игрока
min_player_x, min_player_y, min_player_z = mc.player.getTilePos()

# размер игрового поля
size = 15

# координаты игрока и игрового поля
max_player_x = min_player_x + size
max_player_y = min_player_y + size
max_player_z = min_player_z + size

# список блоков
blocks = []


# функция для удаления блока
def delete(x, y, z):
    mc.setBlock(x, y, z, 0)

# создаем первую игру


def create_game_one():

    # генерируем блоки
    for x in range(size):
        blocks.append([])
        for z in range(size):
            blocks[x].append((35, random.randint(0, 15)))

    # ставим блоки
    for x in range(size):
        for z in range(size):
            mc.setBlock(min_player_x+x, 115, min_player_z +
                        z, blocks[x][z][0], blocks[x][z][1])
            z += 1
        x += 1

    # ставим игрока в центр игрового поля
    mc.player.setTilePos(min_player_x + x//2, 116, min_player_z+z//2)
    # возвращаем список блоков
    return blocks

# создаем вторую игру


def create_game_two():
    # генерируем блоки
    for x in range(size):
        blocks.append([])
        for z in range(size):
            blocks[x].append((35, z))

    # ставим блоки
    for x in range(size):
        for z in range(size):
            mc.setBlock(min_player_x+x, 115, min_player_z +
                        z, blocks[x][z][0], blocks[x][z][1])
            z += 1
        x += 1

    # ставим игрока в центр игрового поля
    mc.player.setTilePos(min_player_x + x//2, 116, min_player_z+z//2)
    return blocks


# функция для игры
def game_logic():
    # создаем первую игру
    create_game_one()

    # список блоков
    blocks_type = [(35, 0), (35, 1), (35, 2), (35, 3), (35, 4), (35, 5),
                   (35, 6), (35, 7), (35, 8), (35, 9), (35, 10), (35, 11),
                   (35, 12), (35, 13), (35, 14), (35, 15)]

    # список названий блоков
    blocks_name = ["Белый", "Оранжевый", "Пурпурный", "Голубой", "Желтый", "Лаймовый",
                   "Розовый", "Серый", "Светло-серый", "Бирюзовый", "Фиолетовый", "Синий",
                   "Коричневый", "Темно-зеленый", "Красный", "Черный"]

    # бесконечная игра
    while True:
        # выбираем случайный блок
        game_color_name = random.choice(blocks_name)
        # получаем индекс блока
        game_block_color_index = blocks_name.index(game_color_name)
        # получаем блок
        game_color_block = blocks_type[game_block_color_index]

        # выводим сообщение
        mc.postToChat("Встань на блок " + game_color_name.capitalize())
        time.sleep(3)

        # пишем основную логику игры
        for x in range(size):
            for z in range(size):
                if blocks[x][z] != game_color_block:
                    delete(min_player_x+x, 115, min_player_z+z)
                # если игрок стоит на блоке
                z += 1
            x += 1

        # обновляем список блоков
        time.sleep(1)
        create_game_one()


# запускаем игру
game_logic()
