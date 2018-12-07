# Программа для чтения из файла и вывода данных в строку
file = open('test.txt','r')
strings = file.readlines()
print(strings)
file.close()

# Программа для чтения из файла и вывода данных по строкам
file = open('test.txt','r')
strings = file.readlines()
for string in strings:
	print(string)
file.close()

# Программа для копирования файлов
filename1 = input('Какой файл забэкапить?: ')
filename2 = 'backup_'+filename1
file1 = open(filename1,'r')
file2 = open(filename2,'w')
file2.write(file1.read())
file1.close()
file2.close()
print('Копирование успешно завершено!')

# Программа для копирования бинарных файлов (фото, видео, музыка)
filename1 = input('Какой файл забэкапить?: ')
filename2 = 'backup_'+filename1
file1 = open(filename1,'rb')
file2 = open(filename2,'wb')
file2.write(file1.read())
file1.close()
file2.close()
print('Копирование успешно завершено!')




