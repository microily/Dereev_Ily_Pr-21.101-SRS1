filename = input("Введите название файла: ")
with open(filename, "r") as file:
    line_number = 1

    for line in file:
        print(f"{line_number} {line}", end="")
        line_number += 1