# проклятие: пинг

# Подключаемся к серверу
import keyboard
import time
import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()


# миссия: сумашедшие путешественники

# импортируем модуль random

# Записываем координаты
x, y, z = mc.player.getTilePos()

# запускаем бесконечный цикл
while True:
    # случайно изменяем координаты
    x += random.uniform(-0.2, 0.2)
    z += random.uniform(-0.2, 0.2)
    # y = mc.getHeight()
    # телепортируем игрока
    mc.player.setPos(x, y, z)
    time.sleep(0.5)
    # уберите брейк, когда будете тестить
    break

# миссия путешественник
mc = Minecraft.create()

# импортируем модуль random

# запускаем бескоенчный цикл
while True:
  # берем кординаты игрока
    x, y, z = mc.player.getTilePos()
    # случайно изменяем координаты
    x += random.uniform(-0.2, 0.2)
    z += random.uniform(-0.2, 0.2)
    y = mc.getHeight(x, z)
    # телепортируем игрока
    mc.player.setPos(x, y, z)
    time.sleep(0.1)
    # уберите брейк, когда будете тестить
    break

# миссия: генерация руд

# подключаемся к серверу
mc = Minecraft.create()

# импортируем клавиатуру

# создаем функцию для генерации руд


def ores_generation(block_id: int, height_down: int, height_up: int, cluster="middle"):
    import random

    # берем координаты игрока
    x, y, z = mc.player.getTilePos()

    # берем id камня
    air = 0
    stone = 1

    # выбираем размер кластера
    if cluster == "big":
        size = 15
    elif cluster == "middle":
        size = 10
    elif cluster == "small":
        size = 5

    # генерируем кластер
    mc.setBlocks(x, height_down, z, x+size, height_up, z+size, block_id)

    # генерируем камень внутри кластера
    stone_blocks = 0

    # запускаем цикл пока все блоки камня не заполнят лишнее пространство
    while stone_blocks <= size**6:
        stone_blocks += 1
        # случайно выбираем координаты блока камня
        stone_x = random.randint(x, x+size)
        stone_y = random.randint(height_down, height_up)
        stone_z = random.randint(z, z+size)
        # ставим блок камня
        mc.setBlock(stone_x, stone_y, stone_z, stone)


# запускаем скрипт
if __name__ == "__main__":
  # бесконечный цикл
    while True:
      # если нажата клавиша q
        if keyboard.is_pressed('q'):
          # генерируем руду
            ores_generation(169, 5, 15, "middle")
