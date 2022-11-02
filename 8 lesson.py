# первое знакомство с else
number1 = 10
number2 = 20

if number1 > number2:
    print("Первое число больше второго")
if number1 < number2:
    print("Второе число больше первого")

# else - программа которая считает зомби, и будем ли мы с ними воевать или будем бежать
zombies = int(input("Введите число зомби"))
if zombies <= 10:
    print("Сейчас поразвлекаемся")
else:
    print("Пора бежать")

# Более полноценная программа для авторизации

# логин и пароль из базы данных
login = "Alexey"
password = "cats"

# то что вводит пользователь
attempt_login = input("Введите логин: ")
attempt_password = input("Введите пароль: ")

# Если попытка == логину и попытка == паролю
if attempt_login == login and attempt_password == password:
    print("Доступ выполнен")
else:
    print("Неправильный логин или пароль")

# Как работает блок elif
# elif

# Программа которая определяет какое мороженое я выберу

# Наличие разных вкусов мороженого
hasChocolate = False
hasStrawberry = False
hasRaspberry = True
hasPopcorn = False
hasVanilla = True


# Единный цикл конструкции if
if hasChocolate:
    print("возьму шоколадное")
elif hasStrawberry:
    print("возьму клубничное")
elif hasRaspberry:
    print("возьму малиновое")
elif hasPopcorn:
    print("возьму попкорновое")
elif hasPopcorn:
    print("возьму ванильное")
else:
    print("нет в магазине мороженого")


# программа которая тонко считает что делать в зависимости от числа зомби
zombies = int(input("Введите число зомби"))
if zombies > 30:
    print("я сдаюсь")
elif zombies > 20:
    print("пора бежать")
elif zombies == 0:
    print("нет ниодного зомби")
else:
    print("да будет бой")



# Программа которая счиатает и определяет ценность подарка

# Подключаемся к миру майнкрафта
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Определяем позицию игрока
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

# Телепортируем игрока
mc.player.setTilePos(x, y, z)

# Получаем айди подарка
gift = mc.getBlock(x, y, z)

# Идентификаторы хорошего и плохого подарка
diamond = 57
bad_present = 6

# Если подарок == алмазный блок
if gift == diamond:
    mc.postToChat("Good present")
# Если подарок == саженец
elif gift == bad_present:
    mc.postToChat("Bad present")
# Если подарка нет, пишем положите подарок
else:
    mc.postToChat("положите подарок на координаты" + str(x) + ", " + str(y) + ", " + str(z))


# программа для банкомата, которую нельзя сломать
# баланс на карте
balance = 100000

# обрабатываем ошибки
try:
    # сумма которую мы хотим снять
    withdraw = int(input("какое кол-во денег он хочет снять? "))

    # проверка не пытаемся ли мы снять больше денег чем есть на балансе
    if withdraw <= balance:
        # Проверка Да-Нет
        confirm = input("Вы уверены? ")
        if confirm == "Да":
            # Вывод
            print("Вот ваши деньги", withdraw)
            print("Остаток на счету", balance-withdraw)
        else:
            # Если пользователь не согласился
            print("Операция отменена")
    else:
        # Если пытаются снять больше чем есть
        print("Недостаточно средств на балансе")
except ValueError:
    # Если вводят не число
    print("Введите число")


