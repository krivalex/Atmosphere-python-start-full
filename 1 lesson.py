
# Необычные операторы Python

pizza = 900
piece = 123

print(pizza / piece)
print(pizza // piece)
print(pizza % piece)
print(123*7)


# Первое подлключение к миру и телепортация раз в три секунды
from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

x = 10.5
y = 110.45
z = 12.69

time.sleep(3)
mc.player.setPos(x, y, z)
time.sleep(3)
mc.player.setPos(x+10, y+10, z+10)


