# if - конструкция
# while - цикл

# разбираем как работает цикл while
count = 0

while count <= 5:
    print(count)
    count += 1
print("Конец цикла")

# Если напишем да - программа остановится
while input("Остановить программу? ") != "Да":
    print("Программа работает")
print("Остановить программу")

# подключаемся к миру майнкрафта
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# импортируем библиотеку
import random
import time

# берем позицию игрока
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

# задает переменную каунт
count = 0

# пока каунт меньше 5
while count <= 5:
    # увеличиваем корды на 200 или уменьшаем случайно
    x += random.randint(-200, 200)
    y += random.randint(-10, 10)
    z += random.randint(-200, 200)
    # телепортируем
    mc.player.setTilePos(x, y, z)
    count += 1
    time.sleep(2)


# как можно получить бесконечную идею
while 3>2:
    print("Это вечно")

# все логические операторы
# == != >= <= > <

# делаем проклятье
# подключаемся к миру майнкрафта
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

# топим игрока в воде каждые десятую секунды
count = 0

# пока каунт меньше 300
while count <= 300:
    # позиция игрока
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    # установить блоки воды в ногах
    mc.setBlock(x, y, z, 9)
    count += 1
    time.sleep(0.1)
    

# это бесконечный цикл
# while True:
    # бесконечно печатает инфинити
    # print("Infinity")

# никогда не выведется
print("Это сообщения никогда не выведется")

# подключаемся к миру майнкрафта
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

# запускаем бесконечный цикл
while True:
    # получаем позицию игрока
    pos = mc.player.getTilePos()
    # ставим вокруг себя цветы
    mc.setBlock(pos.x, pos.y, pos.z, 38)
    mc.setBlock(pos.x+1, pos.y, pos.z, 38, 1)
    mc.setBlock(pos.x-1, pos.y, pos.z, 38, 2)
    mc.setBlock(pos.x, pos.y, pos.z+1, 38, 3)
    mc.setBlock(pos.x, pos.y, pos.z-1, 38, 4)
    mc.setBlock(pos.x+1, pos.y, pos.z+1, 38, 5)
    mc.setBlock(pos.x-1, pos.y, pos.z-1, 38, 6)
    mc.setBlock(pos.x+1, pos.y, pos.z-1, 38, 7)
    mc.setBlock(pos.x-1, pos.y, pos.z+1, 38, 8)
    # пауза в 0.2 секунды
    time.sleep(0.2)




