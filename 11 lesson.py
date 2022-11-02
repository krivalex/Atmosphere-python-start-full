# задаем переменную для числа монеток
coins = 10

# пока вы хотите продолжать вносить монетки, программа будет работать
while input("Хотите продолжить вносить монетки ") == "Да":
    coins += 1
    print("Ваш баланс", coins)

# Вывод итогового баланса
print("Итоговый баланс", coins)


# Игра которая определяет сколько секунд вы проводите под водой, 
# и награждает вас или убивает если находитесь недостаточно

# импортируем библиотеки и подключаемся к миру майнкрафта
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

# берем корды игрока 
x, y, z = mc.player.getTilePos()

# берем корды головы игрока
block_head = mc.getBlock(x, y+1, z)

# записываем идентификаторы блоков
water1 = 9
water2 = 8
flower = 38
lava = 10
diamond = 57

# записываем переменную для числа секунд которые игрок под водой
score = 0

# пока голова игрока находится в обычной или текущей воде 
while block_head == water1 or block_head == water2:
    # пауза в 1 секунду
    time.sleep(1)
    # обновляем корды игрока
    x, y, z = mc.player.getTilePos()
    # берем корды игрока
    block_head = mc.getBlock(x, y+1, z)
    # увеличиваем очки на 1 каждую секунду
    score += 1
    # Отправляем сообщение каждую секунду
    mc.postToChat("Текущий счет: " + str(score))
# выводим общий счет
mc.postToChat("Итоговый счет: " + str(score))

# если он находится под водой больше 6 секунд награждаем его
if score >= 6:
    x, y, z = mc.player.getTilePos()
    # осыпаем его цветами
    mc.setBlocks(x-5, y+10, z - 5, x+5, y+10, z+5, flower)
    mc.setBlocks(x-5, y+10, z - 5, x+5, y+10, z+5, flower)
    mc.setBlocks(x-5, y+10, z - 5, x+5, y+10, z+5, flower)
    mc.setBlocks(x-5, y +10, z - 5, x+5, y+10, z+5, flower)
    mc.setBlocks(x-5, y +10, z - 5, x+5, y+10, z+5, flower)
    # и дарим его алмазный блок
    mc.setBlocks(x-1, y, z-1, x+1, y, z+1, diamond)
else:
    # а если меньше 6 секунд под водой - топим его в лаве
    mc.setBlocks(x-5, y, z-5, x+5, y, z+5, lava)


# подключаемся к миру майнкрафта
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
# импортируем библиотеку время
import time

# берем корды двери
x_door = -366
y_door = 78
z_door = -68

# берем корды ключа
x_block = -371
y_block = 81
z_block = -68

# телепортируем игрока
mc.player.setTilePos(-366, 79, -70)

# задаем идентификаторы блоков
air = 0
stone = 1
command_block = 137

# 3 секунды паузы
time.sleep(3)
# берем и проверяем блок ключа
key = mc.getBlock(x_block, y_block, z_block)

# создаем бесконечный цикл пока истина
while True:
    # если ключ равен командному блоку то открываем дверь
    while key == command_block:
        # обновляем идентификатор блока
        key = mc.getBlock(x_block, y_block, z_block)
        # открываем дверь
        mc.setBlocks(x_door, y_door, z_door, x_door - 2, y_door + 2, z_door + 2, air)
        mc.postToChat("Дверь открыта")
    # если ключ это не командный блок
    while key != command_block:
        # опять обновляем идентификатор блока
        key = mc.getBlock(x_block, y_block, z_block)
        # заменяем дверь камнем
        mc.setBlocks(x_door, y_door, z_door, x_door - 2, y_door + 2, z_door + 2, stone)
        mc.postToChat("Вставьте ключ")

