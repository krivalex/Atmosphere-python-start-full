# повторяем как работаю булеан флаги
light = True
night = False

# операторы сравнения, кратко вспоминаем
# ==, =>, <=, !=, >, <

# вспоминаем чем отличается != от ==
print(light != night)
print(light == night)

# Логические операторы
# and, or, not

# Оператор или
# and

age = 15
owernsCar = True
print(age >= 18 and owernsCar == True)

# Пытаемся исправить код который определяет игрок в воде или нет
# Подключаемся к миру майнкрафта
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Определяем позицию игрока
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

# Задаем воду
water = 9

# Берем координаты ног и головы игрока
block = mc.getBlock(x, y, z)
head = mc.getBlock(x, y+1, z)
mc.postToChat("Игрок в воде: " + str(block == water and head == water))

# Логический оператор ИЛИ
# or

# Пишем программу которая определит могу я себе взять кошку или нет
catColor = input("Какого цвета кошка?")
myCatNow = catColor == "черный" or catColor == "рыжая"
print("Я заведу такого цвета: " + str(myCatNow))

# Миссия: игрок в воде, игрок на дереве, игрок в тесноте?

# Подключаемся к миру майнкрафта
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Определяем позицию игрока
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

# Идентификаторы блоков
water = 9
air = 0

# Берем координаты ног игрока, головы игрока, и блока под игроком
block_foots = mc.getBlock(x, y, z)
block_head = mc.getBlock(x, y+1, z)
block_under_foots = mc.getBlock(x, y-1, z)

# Берем координаты блоков во всех четырех сторонах от ног игрока
block_foots_up = mc.getBlock(x+2, y, z)
block_foots_right = mc.getBlock(x, y, z+2)
block_foots_left = mc.getBlock(x-2, y, z)
block_foots_down = mc.getBlock(x, y, z-2)

# пишем конечный вывод, который работает на основе сравнений и логических операторов
mc.postToChat("Игрок в воде: " + str(block_foots == water or block_head == water))
mc.postToChat("Игрок на дереве: " + str(block_under_foots == 18 or block_under_foots == 17))
mc.postToChat("Игрок в тесноте: " + str(block_foots_up != air and block_foots_down != air and block_foots_left != air and block_foots_down != air))


# True False and or not
# Порядок исполнения логических операций
print(True and not False or False)
print(True and True or False)
print(True or False)
print(True)

# Двойные неравенства
villagers = int(input("Введите число жителей в деревне: "))
enoughVillagers = 10 < villagers < 40
print("Жителей достаточно: " + str(enoughVillagers))





