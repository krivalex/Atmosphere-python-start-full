# типы данных булеан
print(type(True))
print(type(False))

# свет включен, свет выключен
light = True
light = False

# Подключаемся к миру майнкрафта
from mcpi.minecraft import Minecraft
mc = Minecraft.create()


# Как соединять boolean и строки
agree = False
message = "Я хочу пить кофе: " + str(agree)
print(message)

# Все виды операторов сравнения
# == != >= <= > <

# Как работает ==
length = 4
width = 2
print(length == width)

# миссия: игрок в воде

# Подключение к миру майнкрафта
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Отключаем возможность ломать блоки в мире
mc.setting("world_immutable", False)

# Получаем позицию игрока
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

# Задаем идентификаторы для блоков
air = 0
water = 9

# Получаем блок в котором стоит игрок
block = mc.getBlock(x, y, z)
# Печатаем в чат ответ
mc.postToChat("игрок стоит в воде: " + str(block == 9))


# не равно
# Как работает оператор == и оператор !=
width = 3
length = 2
print(width != length)
print(width == length)

# Операторы больше и меньше
limit = 100
obsidian = 120
print(limit < obsidian)
print(100 < 120)

# Операторы больше или равно и меньше или равно
stickers = 30
people = 30
print(stickers <= people)

# миссия: игрок в воде? игрок над землей? игрок далеко от своего дома?

# Подключаемся к миру майнкрафта
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# импортируем библиотеку математика
import math

# определеяем позицию игрока
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

# записивыем координаты центра дома
home_x = -385
home_y = 74
home_z = -103

# записываем идентификаторы блоков в переменные
air = 0
water = 9

# Определяем самый высокий блок по y
highestBlockY = mc.getHeight(x, z)
mc.postToChat("игрок над землей: " + str(highestBlockY <= y))

# Определяем является ли блок в ногах игрока водой
block = mc.getBlock(x, y, z)
mc.postToChat("игрок стоит в воде: " + str(block == 9))

# Считаем дистанцию до дома по теореме Пифагора
distance = math.sqrt((home_x - x) ** 2 + (home_z - z) ** 2)
# Выводим расстояние, и флаг False True
mc.postToChat("игрок больше чем 100 блоков от своего дома: " + str(distance >= 100))
mc.postToChat(distance)


