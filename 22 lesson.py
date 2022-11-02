# Повторение материала


# Создание списка
from mcpi.minecraft import Minecraft
import keyboard
array = [1, 2, 3, 4, 5]
print(type(array))
print(array)

# Создание кортежа
tuple = (1, 2, 3, 4, 5)
print(type(tuple))
print(tuple)

# Создание словаря
dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(type(dict))
print(dict)


# Словарь со полными данными человека

# в словаре можно хранить любые данные
# в том числе и другие словари
dict = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "metadata": {
        "title": "Engineer",
        "department": "Engineering",
        "salary": 60000
    }
}

# Создаем иллюзию json ответов и запросов
# Модель запроса и ответа сервера
# Google Translate
response = {
    "word": "слово",
    "word_into": "russian",
    "word_from": "english",
    "encoding": "utf-8",
}

request = {
    "word": "bye",
    "word_into": "english",
    "word_from": "russian",
    "encoding": "utf-8",
}

# Считываем данные из адресной строки
google = {
    "q": "json",
    "sxsrf": "ALiCzsb9lc9JWCf9jdxvFhEFh6C6zHBrrg%3A1667391426797",
    "source": "hp",
    "ei": "1Z1tYK6yJ4KZr7wP2ZyX2A4",
}

# Учимся разворачивать массив
array = [1, 2, 3, 4, 5]
print(array)
back_array = tuple(reversed(array))
print(back_array)


# Генераторы списков
array_int = []
for i in range(1, 10):
    array_int.append(i)

print(array_int)


# миссия: создаем радужную пирамиду Атмосферы

# импортируем клавиатуру
# подключаемся к серверу
mc = Minecraft.create()

# создаем функция которая будет генерировать пирамиду
# передаем аргументами тип блока и высоту пирамиды


def pyramid(block: int, height: int):
  # получаем координаты игрока
    x, y, z = mc.player.getTilePos()
    x, y, z = x + height, y, z

  # задаем переменную для цвета
    color = -1

    # цикл для генерации пирамиды
    for level in reversed(range(height)):
      # создаем конструкцию для обновления цвета
        if color > 15:
            color = 0
        color += 1

        # устанавливаем блоки
        mc.setBlocks(x - level, y, z - level, x +
                     level, y, z + level, block, color)
        # увеличиваем высоту
        y += 1


# запускаем бесконечный цикл
while True:
  # запускаем функцию при нажатии клавиши q
    if keyboard.is_pressed("q"):
        pyramid(block=35, height=180)
  # останавливаем цикл при нажатии клавиши m
    elif keyboard.is_pressed("m"):
        break


# Разнос почему 10 булок хлеба
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(array))
