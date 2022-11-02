# Изучаем как работает try-except

try:
    countOfSheakers = int(input("Сколько у вас пар кроссовок "))
except ValueError:
    print("Напиши число")


# Подключиться к миру майнкрафта
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Определяем позицию игрока
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

# Пишем код который не дает пользователю ввести ничего кроме числа
try:
    block = int(input("Enter block type: "))
    mc.setBlock(x, y, z, block)
except:
    mc.postToChat("Введи число, надоел")


# Пишем программу которая считает какое расстояние проходит игрок за 10 секунд

# Импортируем библиотеку время
import time

# Подключаемся к миру майнкрафта
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Определяем первую позицию игрока
pos1 = mc.player.getTilePos()
x1 = pos1.x
y1 = pos1.y
z1 = pos1.z

# Ждем позицию игрока
time.sleep(10)

# Определяем вторую позицию игрока
pos2 = mc.player.getTilePos()
x2 = pos2.x
y2 = pos2.y
z2 = pos2.z

# Считаем расстояние между координатами
xDistance = x2 - x1
yDistance = y2 - y1
zDistance = z2 - z1

# Выводим в консоль ответ
message = "игрок прошел по X:{0}, по Y:{1}, по Z:{2}".format(xDistance, yDistance, zDistance)

# Выводим в чат майнкрафта
mc.postToChat(message)

