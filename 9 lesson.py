# Телепортируем игрока в зависимости от его очков

# Подключаемся к миру майнкрафта
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Спрашиваем очки у пользователей
points = int(input("Введите число очков: "))

# Запускаем цепочку и телепортируем его в зависимости от координат

# если число очков меньше 2
if points <= 2:
    mc.player.setPos(110, 100, 120)
# если число очков больше 3
elif points >= 3:
    mc.player.setPos(110, 100, 1200)
# если число очков меньше 11
elif points <= 11:
    mc.player.setPos(-80, 100, 1200)
# если число очков больше 20
elif points >= 20:
    mc.player.setPos(-80, 100, -1200)
# если случайные числа
else:
    mc.postToChat("Давай еще раз")


# повторяем типы данных и идентификаторы
try:
    color = input("Дай идентификатор цвета")
    print(color + 10)

# если типовая ошибка
except TypeError:
     print("Введи число")


# делаем лифт-элеватор
# подключаемся к миру майнкрафта
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# берем координаты блока ключа
x_block = -371
y_block = 81
z_block = -68

# берем координаты двери
x_door = -366
y_door = 78
z_door = -68

# пишем идентификаторы блоков
stone = 1
air = 0
snow = 182.0

# берем идентификатор блока ключа
key = mc.getBlock(x_block, y_block, z_block)

# если ключ равен снегу, то открываем дверь
if key == snow:
    # открываем дверь - меняем блоки на воздух
    mc.setBlocks(x_door, y_door, z_door,
    x_door-2, y_door+2, z_door+2, air)
else:
    # закрываем дверь - меняем блоки на камень
    mc.setBlocks(x_door, y_door, z_door,
    x_door-2, y_door+2, z_door+2, stone)


# если и логические операторы
# пишем программу для определения будете вы делится мороженным или нет
hasCake = False
wouldShare = True

# если у вас есть торт и есть желание им поделится
if hasCake and wouldShare:
    print("Thank you")
else:
    print("грустно")

# как работают логические операторы
# если у вас есть обувь будете ли вы ее носить
wearingShoes = True
if not wearingShoes:
    print("Игрок без ботинок")

# если обувь одета
if wearingShoes:
    print("Игрок в ботинках")




# Делаем рандомную телепортацию
# Как rtp на серверах

# импорт библиотек
import random
import math

# подключаемся к миру майна
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# берем позицию игрока
pos = mc.player.getTilePos()
# записываем в переменные
x_start = pos.x
y_start = pos.y
z_start = pos.z

# делаем случайные координаты для игрока
x_end = random.randint(-30000000, 30000000)
y_end = random.randint(80, 120)
z_end = random.randint(-30000000, 30000000)

# считаем какое число прошел игрок за какое-то время по теореме Пифагора
distance = math.sqrt((x_end - x_start) ** 2 + (z_end - z_start) ** 2)
# пишем ее в чат
mc.postToChat(distance)
# телепортируем игрока
mc.player.setTilePos(x_end, y_end, z_end)



# миссия: строим эскалатор

# подключаемся к миру майна
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

# берем стартовые точки эскалатора
start_x = 8874990
start_y = 72
start_z = 1786996

# делаем процесс работы, прописываем логику
time.sleep(3)
mc.player.setTilePos(start_x, start_y+1, start_z)
time.sleep(0.5)
mc.player.setTilePos(start_x-1, start_y+2, start_z)
time.sleep(0.5)
mc.player.setTilePos(start_x-2, start_y+3, start_z)
time.sleep(0.5)
mc.player.setTilePos(start_x-3, start_y+4, start_z)
time.sleep(0.5)
mc.player.setTilePos(start_x-4, start_y+5, start_z)
time.sleep(0.5)
mc.player.setTilePos(start_x-5, start_y+6, start_z)

# Программа которая определяет наши действия от числа пигманов
pigmans = int(input("Введите число пигманов: "))
if pigmans >= 30:
    print("Вызывайте армию железных големов")
elif pigmans >= 10:
    print("Где мой алмазный меч")
elif pigmans == 0:
    print("Нет ни одного пигмана")
else:
    print("Изи иди сюда")





