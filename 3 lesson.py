# про умножение и степени
square = 2 * 2
cube = 2 * 2 * 2
cube = 2 ** 3

# порядок исполнения операций
mooshroom = 5 * (2 - 1) ** 4 / 2

# сокращенные операции
sheep = 6
sheep = sheep + 5
sheep /= 5

# кубик от 1 до 6
import random
diceValue = random.randint(1, 6)
print(diceValue)

# Подключаемся к миру майнкрафта
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# импортируем библиотеку рандом
import random

# определеяем позицию игрока
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

# изменяем ее случайным образом
x += random.randint(-1000, 1000)
y += random.randint(-10, 100)
z += random.randint(-1000, 1000)

# телепортируем его
mc.player.setPos(x, y, z)
print(pos)

# разбираем что такое str и как с этим работать
stroka = "Зомби норм"
message = 'Давай сделаем "Привет" крышу из песка'

print(type(stroka))
print(message)


# Подключаемся к миру майнкрафта
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# определяем позицию игрока
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

# Определяем блок под его ногами
block = mc.getBlock(x, y-1, z)
mc.setBlock(x+5, y, z+5, block)

# пишем его в чат майна
mc.postToChat(block)

# учимся соединять строки
firstName = "Анатолий"
secondName = "Вассерман"
number1 = 10
number2 = 40
print(str(number1) + str(number2))


# Подключаемся к миру майна
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Спрашиваем у пользователя, его вводы
message = input("Введите сообщение: ")
user = input("Введите автора: ")

# отправляем в чат
mc.postToChat(user + ": " + message)

# считаем сколько алмазных кирок уходит в среднем на поиск алмазов
diamonds = 24
pickaxes = input("How much pickaxes was broken?")
pickaxes = int(pickaxes)
expense = diamonds / pickaxes
print(expense)


# Обьясняю принцип 
mc.setBlocks(x1, y1, z1, x2, y2, z2, block)

# подключаемся к миру майнкрафта 
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# определяем позицию игрока
position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z

# Определяем высоту, ширину, и длину кубоида которую хотим построить
width = 10
height = 10
length = 10

# Записываем идентификаторы блоков
block = 155
air = 0
water = 9

# Строим первый кубоид
mc.setBlocks(x, y, z, x+width, y+height, z+length, block)

# Строим второй кубоид
mc.setBlocks(x+1, y+1, z+1, x+width-1, y+height-1, z+length-1, water)

# Строим третий кубоид
mc.setBlocks(x, y+height, z, x+width, y+height, z+length, air)

