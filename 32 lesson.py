# имспортируем библиотеку для работы с майнкрафтом
import mcpi.minecraft as minecraft
import mcpi.block as block

# импортируем библиотеку для работы со временем
import time
# импортируем библиотеку для работы со случайными числами
import random


# создаем переменную для работы с майнкрафтом
mc = minecraft.Minecraft.create()
# берем координаты игрока
startPos = mc.player.getTilePos()

# задаем первую позицию игрока
mc.setBlock(startPos.x, 150, startPos.z, block.GOLD_BLOCK.id)
# телепортируем игрока на первую позицию
mc.player.setTilePos(startPos.x, 152, startPos.z)

# стартовые сообщения
mc.postToChat("Игра начнется через 5 секунд")
time.sleep(5)
mc.postToChat("Игра началась! Не стой на месте!")

# создаем список блоков
blocks = []
# создаем список типов блоков
blocks_type = [(95, 14), (95, 1), (95, 4), (95, 5),
               (95, 3), (95, 11), (95, 10)]

# создаем переменную для счетчика цветов
color = 0
maxPos = 0

# добавляем первый блок в список
blocks.append([startPos.x, 150, startPos.z])

# создаем бесконечный цикл
while True:
    # генерируем случайные координаты блока
    x_random_block = random.randint(-2, 3)
    y_random_block = random.randint(0, 1)
    z_random_block = random.randint(-2, 3)

    # создаем переменную для хранения дельта координат блока
    delta_random_block = mc.player.getTilePos()
    delta_random_block.x += x_random_block
    delta_random_block.y += y_random_block-1
    delta_random_block.z += z_random_block

    # проверяем, что блок не находится на месте игрока
    if delta_random_block.x != blocks[-1][0] and delta_random_block.z != blocks[-1][2]:
        # если цвет больше 7, то обнуляем его
        if color == 7:
            color = 0
        # ставим блок
        mc.setBlock(delta_random_block.x, delta_random_block.y,
                    delta_random_block.z, blocks_type[color])
        # увеличиваем цвет
        color += 1

    # задержка
    time.sleep(1)

    # добавляем блок в список
    blocks.append([delta_random_block.x,
                  delta_random_block.y, delta_random_block.z])

    # проверяем, что в списке больше 5 блоков
    if len(blocks) > 5:
        # тогда удаляем первый блок из списка
        delete_block = blocks.pop(0)
        # и удаляем его из мира
        mc.setBlock(delete_block[0], delete_block[1],
                    delete_block[2], block.AIR.id)

        # получаем координаты игрока
        pos = mc.player.getTilePos()
        # получаем высоту игрока
        mc.postToChat("Высота: " + str(pos.y))

        # если высота игрока больше максимальной высоты, то обновляем максимальную высоту
        if pos.y > maxPos:
            maxPos = pos.y

        # если высота игрока меньше 150, то игра окончена
        if pos.y < 150:
            # удаляем все блоки из списка
            for delete_block in blocks:
                # и удаляем их из мира
                mc.setBlock(delete_block[0], delete_block[1],
                            delete_block[2], block.AIR.id)
            # выводим сообщение об окончании игры
            mc.postToChat("Игра окончена!")
            mc.postToChat("Вы достигли " + str(maxPos) + " блоков")
            break
