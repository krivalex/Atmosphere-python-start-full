# Программа для определения много зомби или мало
# Первое знакомство с IF

zombies = int(input("Введите число зомби: "))
if zombies > 20:
    print("Много зомби")
if zombies > 50:
    print("Очень много зомби")

# Простая авторизация, проверка пароля на правильность
password = "2233"
attempt = input("Введите пароль: ")

if attempt == password:
    print("Вход выполнен")

print("Конец программы")



# Миссия: создать кратер
# Как построить алмазную коробку
# mc.setBlocks(x, y, z, x+10, y+10, z+10, 57)

# подключаемся к миру майнкрафта
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# получаем позицию игрока
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

# Идентификатор воздуха
air = 0

# Спрашиваем у пользователя, какой размер кратера он хочет
answer = input("Вы хотите создать кратер? ")
power = int(input("Какой размер кратера вы хотите? "))

# Если ответ да д 1 yes, делаем кратер блоками воздуха
if answer == "Да" or "Д" or "1" or "Yes":
    mc.setBlocks(x+power, y+power, z+power, x-power, y-power, z-power, 0)


# Миссия голый снеговик, без рук, и без глаз и рта, доделывайте)

# Подключаемся к миру майна
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Получаем позицию игрока
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

# Идентификатор снега
snow = 80

# Размера всех комов снеговика
big = 10
middle = 8
head = 6

# Создаем самый большой круг снеговика
mc.setBlocks(x, y, z, x + big, y + big, z + big, snow)
# Создаем средний блок снеговика
mc.setBlocks(x + 1, y + big + 1, z + 1, x + middle + 1, y + big + 1 + middle, z + 1 + middle, snow)
# Создаем голову снеговика
mc.setBlocks(x + 2, y + big + middle + 1, z + 2, x + head + 2, y + big + 2 + middle + head, z + 2 + head, snow)
