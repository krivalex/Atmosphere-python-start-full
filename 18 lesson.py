# создаем список с именами
names = ["Alexey", "Adil", "Bekzhan", "Alexander", "Codeinoslav", "Amogus", "Arman", "Madyar", "Islam"]

# создаем переменную кладем в нее журнал
magazine = "Vertigo"

# разбираемся в работе индексации
print(names[:])
print(names[-6])
print(names[-1:0])

# создаем переменные с именем и фамилией
firstName = "Marcuss"
lastName = "Persson"

# печатаем имя и фамилию, а также инициалы
print(firstName + " " + lastName)
print(firstName[0] + " " + lastName[0])


# миссия: столбик

# импортируем время
import time

# подключаемся к миру майна
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# берем кор-ды игрока
x, y, z = mc.player.getTilePos()

# берем идентификаторы блоков
barBlock = 169
glass = 20

# создаем массив блоков с заполнением блоков
blocks = [glass, glass, glass, glass, glass,
          glass, glass, glass, glass, glass]

# устанавливаем пустой столбик из стекла
mc.setBlocks(x+2, y+1, z+2, x+2, y+len(blocks), z+2, glass)


# создаем переменную счетчик
count = 0

# пока счетчик меньше чем длина массива блоков
while count <= len(blocks):
    # пробуем
    try:
        # выводим массив с блоками
        print(blocks)

        # удаляем последний элемент
        del(blocks[-1])
        # добавляем морской фонарь первым блоком
        blocks.insert(0, barBlock)
        # пауза в 1 секунду
        time.sleep(1)
        
        # переставляем блок
        mc.setBlock(x+2, y+count+1, z+2, blocks[count])
        # увеличиваем счетчик
        count += 1
    # Если ловим индексеррор
    except IndexError:
        # ничего не делаем
        pass



# создаем массив с именами
names = ["Alexey", "Adil", "Bekzhan", "Alexander", "Codeinoslav", "Amogus", "Arman", "Madyar", "Islam"]

# Адиль есть в списке имен?
print("Adil" in names)

# Если Адиля нет в списке имен
if "Adil" not in names:
    print("It's a bad news")
# Если нету
else:
    print("It's a great list")

# Вспоминаем что такое кортеж
distance = 12.03, 15.10, 11.89, 58.26
print(distance)

# Миссия: Уничтожитель мира

# импорт библиотек, подключение
import keyboard
from mcpi.minecraft import Minecraft
mc = Minecraft.create()


# Аргументами функция принимает размера мира во всех 3 плоскостях
def destroy(size_x: int, size_y: int, size_z: int) -> None:
    """Уничтожает мир"""
    x, y, z = mc.player.getTilePos()
    air = 0

    # заменяем мир воздухом
    mc.setBlocks(x, y, z, x+size_x, y+size_y, z+size_z, air)


# если скрипт запускается из других файлов
if __name__ == "__main__":
    # повторять бесконечно
    while True:
        # если нажали на Q
        if keyboard.is_pressed('q'):
            # вызываем функцию
            destroy(100, -30, 100)
