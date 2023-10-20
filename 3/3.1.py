negative_numbers = []
zeroes = []
positive_numbers = []

while True:
    user_input = input('Введите целое число(или оставьте стрроку пустой для ввода)')
    if user_input == "":
        break
    number = int(user_input)
    if number < 0:
        negative_numbers.append(number)
    elif number == 0:
        zeroes.append(number)
    else:
        positive_numbers.append(number)

for number in negative_numbers:
    print(number)
for number in zeroes:
    print(number)
for number in positive_numbers:
    print(number)