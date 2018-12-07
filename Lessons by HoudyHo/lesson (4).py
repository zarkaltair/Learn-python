a = input('Введите первое число : ')
b = input('Введите второе число : ')
print(int(a) + int(b))

print(str(1) + '2' + str(3) + '4')

name = input('Enter your name: ')
count = input('How many?: ')
print(name*int(count))

pogoda = 'Зима'
time = 'День'
print( 'Программа запущена.' )
if pogoda == 'Зима':
	print( 'Сейчас холодная погода, лучше никуда не идти!' )
	if time == 'Ночь':
		print( 'Сейчас еще и ночь, ты псих вообще?' )
	if time == 'День':
		print( 'Сейчас конечно день, но холодно как...' )
if pogoda == 'Дождь':
	print( 'Ууу ... Сейчас дождик, ты блин промокнешь!' )
print( 'Программа завершена.' )