# миссия: Посчитать число ударов по блокам

# подключиться к миру майна
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# импортируем время
import time

# ставим паузу в 15 секунд
time.sleep(15)

# получаем число ударов по блокам
blockHits = mc.events.pollBlockHits()
print(blockHits)
print(len(blockHits))


# вспоминаем как работать со списками
array = [10, 10.2, "awfawf", True]
print(array)
print(array[0])

# понмиаем что в списки и кортежи можно положить другой список или кортеж
huh = (10.2, 45, True, "awfawf", [12, 13])

# создаем словарь
dictionary = {"Katya": 12,
              "Nyrsylatan": 22,
              "Vladimir": 45,
              "Amogus": 1000-7}

# выводим все типы данных, для всего
print(type(array))
print(type(huh))
print(type(dictionary))


# создаем карточку человека-словарь
personCard = {
    "name": "Igbragim",
    "age": 40,
    "color": "red",
    "phrase": "I back out the Vietham War"
}

# выводим ее
print(personCard)
print(personCard["name"])


# создаем словарик с временем отправки поездов
trainTimes = {
    13.00: "Almaty",
    13.25: "Astana",
    14.00: "Aktau",
    15.00: "Karamogus"
}

# выводим поезд в 13-25
print(trainTimes[13.25])


# миссия: телепортер

# подключаемся к миру майнкрафта
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# создаем словарь со списком мест куда можно тепехнуться
places = {"home": (134952, 109, 518),
          "country-side-house": (134845, 97, 452)}


# создаем переменную для выбора
choice = ""

# пока выбор не равен выход
while choice != "exit":
    # запрашиваем у игрока куда он хочет тп
    choice = input("Write the point to teleport: ")
    # если место есть в словаре
    if choice in places:
        # записываем корды
        x, y, z = places[choice]
        # телепортируем его
        mc.player.setTilePos(x, y, z)




# снова создаем словарь
trainTimes = {
    13.00: "Almaty",
    13.25: "Astana",
    14.00: "Aktau",
    15.00: "Karamogus"
}

# учимся перезаписывать
print(trainTimes)
trainTimes[14.00] = "Zheskasgan"

# и удалять данные из словаря
del trainTimes[15.00]
print(trainTimes)