import math
radius = float(input('Введите радиус шара: '))
diagonal1 = float(input('Введите длину диагонали 1 отверстия: '))
diagonal2 = float(input('Введите длину диагонали 2 отверстия: '))
d = diagonal1 * diagonal2
if d >= math.pi*(radius**2):
    print('Шар может пройти через отверстие.')
else:
    print('Шар не может пройти через отверстие')