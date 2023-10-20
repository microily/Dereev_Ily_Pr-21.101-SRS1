filename = input("Введите название файла: ")
file = open(filename, "w")
while True:
    line = input("Введите строку (для выхода введите пустую строку): ")
    if not line:
        break
    file.write(line + "\n")
print("Файл записан")
file.close()