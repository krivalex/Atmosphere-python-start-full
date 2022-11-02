# Миссия: Пишем рабочий и полностью сделанный калькулятор

# функция в себя что-то принимает
# функция из себя что-то возвращает

# input
# output

# Создаем функцию она принимает в себя
# Число1, Число2, и тип операции который хотим использовать

def calculator(number1: float = 0, number2: float = 0, operation: str = "+"):
    # добавляем документацию
    """Вызов простого калькулятора"""
    # добавляем проверку на ошибки
    try:
        # Запускаем цепочку проверок на операции
        if operation == "+":
            return number1 + number2
        elif operation == "-":
            return number1 - number2
        elif operation == "*":
            return number1 * number2
        elif operation == "/":
            return number1 / number2
    # отлавливаем ошибки
    except TypeError:
        return "Введите число" 
    except ZeroDivisionError:
        return "Нельзя делить на ноль"
    # отлавливаем ошибку когда пользователь не вводит операцию
    else:
        return "Нет такой операции"

# Проверка стандартной работы
print(calculator(15, 25, "+"))
print(calculator(15, 25, "-"))
print(calculator(15, 25, "*"))
print(calculator(15, 25, "/"))

# Проверка, добавляем аргументы
print(calculator(operation="+", number1=41, number2=85))

# Проверка, добавляем не все аргументы
print(calculator(number1 = 10, number2 = 20))

# Проверка, проверяем все ошибки
print(calculator(number1 = "wafaw", number2 = 20))
print(calculator(number1 = 10, number2 = 0, operation="/"))

# Проверка, прверяем на операции
print(calculator(number1 = 10, number2 = 0, operation="+++"))

