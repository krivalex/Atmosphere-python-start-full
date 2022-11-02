# Делаем работающий танцпол, с музыкой, 
# сменой блоков и автоматическим включением и отключением

# подключаемся к миру майнкрафта
from mcpi.minecraft import Minecraft
# импортируем библиотеку время
import time
# импортируем библиотеку плейсаунд
from playsound import playsound
mc = Minecraft.create()

# получаем координаты игрока
x, y, z = mc.player.getTilePos()

# записываем координаты самого левого крайнего блока платформы
floor_x = x - 3
floor_y = y - 1
floor_z = z - 3

# записываем ширину и высоту в переменные для того чтобы создать платформу
width = 5
length = 5

# создаем платформу
mc.setBlocks(floor_x, floor_y, floor_z, floor_x + width, floor_y, floor_z + length, 95)

# создаем переменную для смены цветов
glass_color = 0
# создаем флаг для определения проигрывания музыки
play = False

# запускаем бесконечный цикл
while 3>2:
    # берем корды игрока
    x, y, z = mc.player.getTilePos()
    # запускаем цикл который будет проверять находимся мы на платформе или нет
    while floor_x <= x <= floor_x + width and floor_z <= z <= floor_z + length:
        # обновляем цвета, когда они кончаются
        if glass_color == 16:
            glass_color = 0
        # музыка должна включаться только единожды
        if not play:
            playsound('lessons/files/Song_Bad.mp3', False)
            play = True
        # устанавливаем платформу, и каждый раз обновляем ей цвет
        mc.setBlocks(floor_x, floor_y, floor_z, floor_x + width, floor_y, floor_z + length, 95, glass_color)
        # увеличиваем переменную на каждой итерации цикла
        glass_color += 1
        # танцпол должен менятся каждые полсекунды
        time.sleep(0.5)
        # обновляем корды, мало ли уже сошли с танцпола
        x, y, z = mc.player.getTilePos()