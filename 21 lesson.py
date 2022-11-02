# импортируем время
import keyboard
import time
# подключаемся к серверу
from mcpi.minecraft import Minecraft

# создаем список ингредиентов для рамена
ramen = ["noodles", "broth", "egg", "garlic",
         "soy sauce", "sesame oil", "pepper"]

# пробегаемся по списку ингредиентов
for ingredient in ramen:
    print(ingredient)

print()


# миссия: волшебная палочка
# подключаемся к серверу
mc = Minecraft.create()

# пауза последняя
time.sleep(15)
# получаем массив ударов по блокам
hits = mc.events.pollBlockHits()

# получаем золотой блок
gold = 41

# пробегаемся по массиву ударов
for hit in hits:
    # получаем координаты блока
    x, y, z = hit.pos.x, hit.pos.y, hit.pos.z
    # ставим блок
    mc.setBlock(x, y, z, gold)

# пробегаемся по range
for count in range(0, 101):
    # выводим числа, их квадраты и кубы
    print(str(count) + " " + str(count ** 2) + " " + str(count ** 3))


# миссия: магические лестницы
# подключаемся к серверу
mc = Minecraft.create()

# создаем функцию для генерации лестницы


def add_magic_stairs(block, size, direction) -> None:
    # получаем координаты игрока
    x, y, z = mc.player.getPos()

    # если направление - вверх
    if direction == "north":
        # пробегаемся по range
        for i in range(0, size):
            # ставим блок
            mc.setBlock(x + i, y + i, z, block)


# запускаем скрипт
if __name__ == "__main__":
    # запускаем бесконечный цикл
    while True:
        # если нажата клавиша "q"
        if keyboard.is_pressed('q'):
            # вызываем функцию
            add_magic_stairs(53, 50)
        # если нажата клавиша "m"
        if keyboard.is_pressed('m'):
            # останавливаем группу
            break
