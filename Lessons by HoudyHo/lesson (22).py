# Функции для работы со строками и числами

fruits = ['Лимоны', 'Яблоки', 'Киви', 'Ананас', 'Клубника']
members = 'James,Jonny,Jessie,Jack,John'
# join, replace, startswith, endswith, lower, upper, split, min, max, abs, sum

# Преобразование списка в строку с помощью метода .join с добавлением ','
print(','.join(fruits))
# Преобразование списка в строку с помощью метода .join с добавлением ' - '
print(' - '.join(fruits))
# Замена аргумента с помощью метода .replace
print('Привет, Петр!'.replace('Петр', 'Александр'))
# Сортировка с помощью метода .startswith
name = input('Введите Ваше имя: ')
if(name.startswith('А')):
	print('Добро пожаловать!\nВы находитесь в элитном клубе людей, имена которых начинаются с буквы "А"!')
else:
	print('Добро пожаловать!')
# Сортировка с помощью метода .startswith с применением метода .lower (не чувствительность к регистру)
name = input('Введите Ваше имя на любом языке: ')
if(name.lower().startswith('а') or name.lower().startswith('a')):
	print('Добро пожаловать!\nВы находитесь в элитном клубе людей, имена которых начинаются с буквы "А"!')
else:
	print('Добро пожаловать!')
# Пример работы метода .lower
input_str = input('Enter text: ')
print(input_str.lower())
# Применение метода .endwith
word = 'Hello drudving'
if(word.endswith('ing')):
	print('Hello ING!')
else:
	print('WTF!')
# Пример работы метода .upper
input_str = input('Enter text: ')
print(input_str.upper())
# Метод split разъединяет заданную строку (противоположно методу .join)
print(members.split(','))
# Функция min возвращает самое маленькое число из списка
print(min([5,10,8,65,233,4287,56,1,58]))
# Функция max возвращает самое большое число из списка
print(max([5,10,8,65,233,4287,56,1,58]))
# Функция abs передает абсолютное число (то есть число без знака)
print(abs(235))
print(abs(-325))
# Функция sum передает сумму всех элементов в списке
print(sum([5,15,8,65]))









