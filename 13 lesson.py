# конструкция while-else

# повторим как работает стандартный if - else
# проверяем число четное или нечетное
number = 118418948418566468486464184846684846486489
if number % 2 == 0:
    print("Число четное")
else:
    print("Число нечетное")



# Простой бесконечный чат

# Запрашиваем сообщение у пользователя через инпут
message = input("Введите сообщение ")

# Запускаем while который будет работать пока пользователь не ведет выход
while message != "выход":
    # выводим сообщение
    print(message)
    # запрашиваем сообщение заново
    message = input("Введите сообщение ")
    # запоминаем что такое break
    if message == "прервать":
        # прерываем чат, когда пользователь пишет прервать
        print("Пользователь прервал чат")
        break
# если программа ломается через break - выводится else
else:
    print("Пользователь покинул чат")


# Миссия: Горячо-Холодно, пишем первую полноценную мини-игру

# Подлкючаемся к миру майнкрафта
from mcpi.minecraft import Minecraft
# импортим нужные библиотеки
import random
import math
import time
mc = Minecraft.create()

# получаем корды игрока
x, y, z = mc.player.getTilePos()

# дублируем их в корды блока
block_x, block_y, block_z = x, y, z

# изменяем x и z случайным образом, чтобы спавнить блок
block_x += random.randint(-200, 200)
block_z += random.randint(-200, 200)
# для y используем getHeight - блок заспавнился на поверхности
block_y = mc.getHeight(block_x, block_z)

# записываем идентификатор блока
block = 397, 3

# флаг для проверки создан блок или нет
block_create = False

# пока блок не создан
while not block_create:
    # делаем проверку чтобы блок не мог спавнится на воде
    if block_y - 1 != 8 or block_y - 1 != 9:
        # спавним блок
        mc.setBlock(block_x, block_y, block_z, block)
        # меняем флаг на true
        block_create = True
        # блок создан
        mc.postToChat("Блок создан")


# запускаем бесконечный цикл
while True:
    # получаем корды игрока
    x, y, z = mc.player.getTilePos()
    # считаем до него дистанцию по теореме пифагора
    distance = math.sqrt((x - block_x)**2 + (z - block_z)**2)
    # выводит ее в консоль
    print(distance)

    # если дистанция больше 300 - Антарктида
    if distance >= 300:
        mc.postToChat("Антарктида")
    # остальные части запускаем с помощью elif 
    elif distance >= 200:
        mc.postToChat("Замерзаешь")
    elif distance >= 150:
        mc.postToChat("Очень холодно")
    elif distance >= 100:
        mc.postToChat("Холодно")
    elif distance >= 50:
        mc.postToChat("Тепло")
    elif distance >= 25:
        mc.postToChat("Горячо")
    elif distance >= 10:
        mc.postToChat("Обожжешься")
    elif distance <= 1:
        # если мы в одном блоке от искомого - нужно остановить бесконечный цикл
        mc.postToChat("Блок найден")
        # используем брейк чтобы остановить
        break
    # добавляем задержку в секунду
    time.sleep(1)


# число четное или нечетное
number = 10
if number % 2 == 0:
    print("Число четное")
else:
    print("Число нечетное")




