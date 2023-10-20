import math

x = float(input('Введите x: '))
n = 0
e = 0.001
full_sum = 0
f = math.cos(x)
func = 0
while math.fabs(full_sum - f) > 0:
    func = ((-1)**n)*((x**(2*n))/math.factorial(2*n))
    full_sum += func
    n += 1
print(f'{f} - искомое')
print(f'{full_sum} - мой ответ')