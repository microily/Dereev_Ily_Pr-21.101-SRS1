A = int(input('Введите целое число A: '))
B = int(input('Введите целое число B: '))

sum = 0
if A < B:
    for i in range(A, B + 1):
        sum += i
    print(f'Сумма всех целых чисел от {A} до {B}: {sum}')
else:
    print('Число A меньше B')