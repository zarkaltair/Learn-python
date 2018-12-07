# Форматирование строк
# первый метод % placeholder
# второй метод .format()

# Стандартный метод вывода без форматирования
name = 'Jone'
age = 21
print('Hello, ' + str(name) + '!\nYou are ' + str(age) + ' years old!')

# Форматирование с помощью % placeholder
name = 'Jone'
age = 21
print('Hello, %s!\nYou are %d years old!' % (name, age))
# %s - плэйсхолдер строки
# %d - плэйсхолдер числа
# %f - плэйсхолдер дроби

# Форматирование с помощью метода format()
name = 'Jone'
age = 21
print('Hello, {0}!\nYou are {1} years old!'.format(name,age))

print('{0}{1}{0}'.format('abra','cad'))

# Персонализирование аргументов
person_name = 'Jone'
person_age = 21
print('Hello, {name}!\nYou are {age} years old!'.format(name = person_name, age= person_age))

# Фопматирование строки с использованием словаря
human = {
	'name':'Jone',
	'age': 21
}
print('Hello, {person[name]}!\nYou are {person[age]} years old!'.format(person = human))

# Фопматирование строки с применением заполнителя слева справа с центрирование текста
input_str = 'Jone'
print('{0:*^8}'.format(input_str))
print('{0:_<8}'.format(input_str))
print('{0:->8}'.format(input_str))

# Jone**** < заполнение справа
# ****Jone > заполнение слева
# **Jone** ^ заполненеие по центру

input_str = 'Jessy'
length = 10
if(len(input_str) % 2):
	length += 1
print(('{0:*^' + str(length) +'}').format(input_str))


