filename = input("Введите имя файла: ")
n = int(input("Введите максимальное количество строк в каждом файле: "))
with open(filename, 'r') as f:
    lines = f.readlines()
    num_files = (len(lines) + n - 1) // n
    for i in range(num_files):
        file_name = f"{i+1}.txt"
        with open(file_name, 'w') as out:
            start_index = i * n
            end_index = min((i + 1) * n, len(lines))
            out.writelines(lines[start_index:end_index])