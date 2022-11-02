# вспоминаем типы данных
print(type(str(10)))
print(type("10"))

# понимаем что мы уже знаем что такое функции и их постоянно используем
int()
input()

# подключаемся к миру майна
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# получаем его корды
x, y, z = mc.player.getTilePos()

# SetBlock - это тоже такая же функция
mc.setBlock()

# пишем первую функцию
def greeting():
    # создаем управляемый цикл который сработает 10 раз
    count = 0
    while count <= 10:
        count += 1
        print("Hello")
        print("Nice to meet you, amogus")

# вызываем функцию
greeting()


# разбираемся что такое аргументы
def fancyGreeting(name):
    print("Hello, " + name)
        
# понимаем что выводить функции можно выводить и внутри других циклов
try:
    fancyGreeting("Artur")
    fancyGreeting("Codeinoslav")
    fancyGreeting()
except TypeError:
    print("Введите имя")


# разбераемся с тем что такое строгая типизация в аргументах функции
import time

# создаем функцию
# в аргументы через двоеточие пишем тип данных которые ждет эта функция
# с помощью стрелки говорим какой тип данных она возвращает
def HelloAndGoodbye(name: str, sec: int) -> str:
    print("Hello, " + name)
    time.sleep(sec)
    print("Goodbye, " + name)

# вызываем функцию, первым аргументом имя, вторым - секунды
HelloAndGoodbye("Arman", 5)
HelloAndGoodbye("Adillll", 1)
HelloAndGoodbye("Amogus", 0.2)
HelloAndGoodbye("Codeinoslav", 10)


# рефакторинг кода
def helloFriend(name):
    name = input("Hello, What is your name? ")
    print("Nice to meet you " + name)


