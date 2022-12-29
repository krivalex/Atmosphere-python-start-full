# пишем полноценный декоратор

# импортируем библиотеку для работы с датой и временем
import time
# импортируем библиотеку для работы с процессами
import psutil


# создаем декоратор для форматирования вывода
def formatter(func):
    # создаем функцию внутри функции
    def wrapper():
        print("</-----------------------------------------------------\>")
        result = func()
        print("<\-----------------------------------------------------/>")
        return result
    # возвращаем функцию
    return wrapper


# создаем декоратор для замера времени выполнения
# и для вывода информации о процессе
def benchmark(func):
    # создаем функцию внутри функции
    def wrapper():
        # засекаем время
        start = time.time()
        result = func()
        # выводим информацию о процессе
        print("Memory: ", psutil.virtual_memory())
        print("CPU: ", psutil.cpu_percent())
        print("Process: ", psutil.Process())
        print("ID: ", psutil.Process().pid)
        print("Name: ", psutil.Process().name())
        print("Status: ", psutil.Process().status())
        print("Memory info: ", psutil.Process().memory_info())
        print("Memory percent: ", psutil.Process().memory_percent())
        print("IO info: ", psutil.Process().io_counters())
        print("Number of threads: ", psutil.Process().num_threads())
        print("Children: ", psutil.Process().children())
        print("Parent: ", psutil.Process().parent())
        print("Username: ", psutil.Process().username())
        print("Nice: ", psutil.Process().nice())
        print("CWD: ", psutil.Process().cwd())
        print("Memory maps: ", psutil.Process().memory_maps())
        print("Open files: ", psutil.Process().open_files())
        print("Connections: ", psutil.Process().connections())
        print("Threads: ", psutil.Process().threads())
        print("Num threads: ", psutil.Process().num_threads())
        print("Memory percent: ", psutil.Process().memory_percent())
        print("CPU times: ", psutil.Process().cpu_times())
        print("Status: ", psutil.Process().status())
        print("Name: ", psutil.Process().name())

        # засекаем время
        end = time.time()
        print(f'Время выполнения: {end - start}')
        return result
    # возвращаем функцию
    return wrapper


# выдаем результаты
# первый декоратор
@formatter
# второй декоратор
@benchmark
# функция
def fetch_webpage():
    # импортируем библиотеку для работы с веб-страницами
    import requests
    # получаем веб-страницу
    url = "https://jsonplaceholder.typicode.com/posts"
    # разбираем веб-страницу
    webpage = requests.get(url)
    # выводим результаты
    print("Статус кода ", webpage.status_code)
    print("Тип кода ", webpage.headers['content-type'])
    print("Кодировка ", webpage.encoding)
    print("Длина ", len(webpage.text))
    print("Первые 100 символов ", webpage.text[:100])
    print("Текст ", webpage.text)


# выводим результаты
fetch_webpage()
