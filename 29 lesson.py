# о многофункциональности функций

from tqdm import tqdm
import time
count = 0


# создаем функцию с функциями внутри
def first():
    # объявляем глобальную переменную
    global count

    # создаем функцию внутри функции
    def second1():
        return "second1"

    # создаем функцию внутри функции
    def second2():

        # создаем функцию внутри функции внутри функции
        def third1():
            return "third1"

        # создаем функцию внутри функции внутри функции
        def third2():
            return "third2"

        # вызываем основную функцию
        first()
        count += 1

        return "second2"

    # пытаемся не создать рекурсию
    if count != 10:
        second2()

    return "first"


# вызываем основную функцию
print(first())


# знакомимся с декораторами
def higher_order(func):
    print("Получена функция {}".format(func.__name__))
    func()
    return func

# создаем основную функцию


def hello():
    print("Hello world!")


# вызываем функцию которая принимает функцию
higher_order(hello)


# создаем декоратор
def decorator_function(func):
    # создаем функцию внутри функции
    def wrapper():
        # выводим информацию о функции
        print("Функция - обертка")
        print("Оборачиваемая функция - {}".format(func.__name__))
        print("Вызов оборачиваемой функции")
        func()
        print("Вызов завершен")
    # возвращаем функцию
    return wrapper


# вызываем декоратор
@decorator_function
# передаем его основной функции
def hello_world():
    print("Hello world!")


# вызываем ее
hello_world()

# тестим бенчмарк

# замеряем скорость выполнения
speed = 3479263.6812334885
timer = 0

# создаем декоратор с бенчмарком


def benchmark(func):
    global timer

    # создаем функцию внутри функции
    def wrapper():
        # замеряем время выполнения функции
        start = time.time()
        end = time.time()
        timer = end - start
        print("Время выполнения функции: {}".format(timer))
        return timer

    # возвращаем функцию
    return wrapper


# замеряем время выполнения функции
@benchmark
# передаем его основной функции
def test():
    # создаем цикл
    for i in tqdm(range(10000000)):
        pass
    return timer


# замеряем время выполнения функции и выводим результат
print(test())
print(speed * timer)
