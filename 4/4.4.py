output_filename = input("Введите имя выходного файла: ")
input_filenames = input("Введите имена файлов для объединения через пробел: ").split()

output_file = open(output_filename, 'w')

for input_filename in input_filenames:
   input_file = open(input_filename, 'r')
   output_file.write(input_file.read())
   input_file.close()

output_file.close()