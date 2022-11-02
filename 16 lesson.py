# Миссия: написать случайный дождь из блоков вокруг игрока

# Подключаемся к миру майнкрафта
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# импортируем библиотеки
import random
import keyboard

# Создаем функцию - в аргументы передаем переменные, которые будем использовать
# внутри функции - тип блока, число повторений, радиус вокруг игрока
def randomBlockGenerator(blockType, repeats, radius):

    # берем позицию игрока
    x, y, z = mc.player.getTilePos()
    # создаем динамические переменные для блоков
    x_block, y_block, z_block = x, y, z

    # создаем переменную для ведения числа итераций в цикле while
    count = 0

    # цикл while должен отработать столько раз, сколько повторений мы передали
    while count <= repeats:

        # увеличиваем переменную каунт, на единицу
        count += 1

        # случайно изменяем корды на каждой итерации цикла для каждого блока
        x_block += random.randint(-radius, radius) 
        z_block += random.randint(-radius, radius) 
        # y_block = mc.getHeight(x_block, z_block)
        y_block = 150

        # устанавливаем блок
        mc.setBlock(x_block, y_block, z_block, blockType)

# вводим проверку для запуска скрипта, подробнее в уроке
if __name__ == "__main__":
    # если на клавиатуре нажата q
    while not keyboard.is_pressed('q'):
        # вызываем функцию
        randomBlockGenerator(blockType=145, repeats=200, radius=15)


# Миссия: Черепашка

# Импортируем библиотеки
from mcpi.minecraft import Minecraft
# Импортируем новую
from minecraftstuff import MinecraftDrawing, MinecraftShape, MinecraftTurtle

# Подлкючаемся к миру майнкрафта
mc = Minecraft.create()

# Берем позицию игрока
pos = mc.player.getTilePos()

# Создаем черепашку - называем стив
steve = MinecraftTurtle(mc, pos)

# Просто так пишем две функции чтобы упростить код
# и поворачивать одной строчкой
def right():
    steve.right(90)
    steve.forward(15)

def left():
    steve.left(90)
    steve.forward(15)

# Устанавливаем идентификатор блока для строительства
steve.penblock(169)

# Идем прямо
steve.forward(15)

# Поворачиваем налево и идем прямо
steve.left(90)
steve.forward(15)

# Поворачиваем направо и идем прямо
steve.right(90)
steve.forward(15)

steve.right(90)
steve.forward(15)

steve.left(90)
steve.forward(15)

steve.right(90)
steve.forward(15)

steve.right(90)
steve.forward(15)

steve.left(90)
steve.forward(15)

steve.right(90)
steve.forward(15)

steve.right(90)
steve.forward(15)

steve.left(90)
steve.forward(15)

steve.right(90)
steve.forward(15)

# повторяем функции

# input metall

def factory(metall):
    gvozdi = metall ** 2
    return gvozdi

# output gvozdi

# вызываем и смотрим что делает
a = factory(100)
print(a)




