x = float(input('Введите x: '))
y = float(input('Введите y: '))
if (x>=0 and x**2+y**2<=1) or (x>=0 and y<=0 and y>= x-1):
    print('Точка входит в область')
else:
    print('Точка не входит в область')