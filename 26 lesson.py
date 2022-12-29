# Как открывать файлы

# a - добавляет в конец файла
# w - перезаписывает файл
# r - читает файл
# r+ - читает и записывает в файл
# w+ - перезаписывает и читает файл
# a+ - добавляет в конец файла и читает файл

secretFile = open("secretFile.txt", "a", encoding="utf-8")
# Запись в файл
secretFile.write("\nЮбилей")
# Закрытие файла
secretFile.close()


# Чтение файла
secretFile = open("secretFile.txt", "r+", encoding="utf-8")
# Чтение файла
for i in range(5):
    # Чтение файла построчно
    a = secretFile.readline()
    # Перезапись строки
    a = a + "awfawf"
    # Запись строки в файл
    secretFile.write(a)
# Закрытие файла
secretFile.close()
