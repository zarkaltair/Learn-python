test = None
if(test == None):
	print(test)

foo = print()
if foo == None:
	print(1)
else:
	print(2)

# Dictionary - Словарь
test = {
	'ключ1':'значение1',
	'ключ2':'значение2',
}
try:
	print(test['тестовый_ключ'])
except KeyError:
	print('Такого ключа не существует!')

test = {
	'ключ1':'значение1',
	125:'сто двадцать пять',
}
if 125 in test:
	print('exist')
else:
	print('not exist')

primes = {1:2,2:3,4:7,7:17}
print(primes[primes[4]])

contacts = {
	'Андрей Змеевский':'+153654665132',
	'Никита Хогвартс' :'+265465416351',
	'Роман Таненбаум' :'+151635415513'
}
testing = input('Кого ишем?: ')
if testing in contacts:
	print('Контакт найден, номер телефона: '+contacts[testing])
else:
	print('Контакт не найден!')

contacts = {
	'Андрей Змеевский':'+153654665132',
	'Никита Хогвартс' :'+265465416351',
	'Роман Таненбаум' :'+151635415513'
}
print(contacts.get('Никита Хогвартс','Номер не найден!'))

contacts = {
	'Андрей Змеевский':'+153654665132',
	'Никита Хогвартс' :'+265465416351',
	'Роман Таненбаум' :'+151635415513'
}
print(contacts.get('Даша Шармбатон','Номер не найден!'))

fib = {1:1,
	   2:1,
	   3:2,
	   4:3
}
print(fib.get(4,0)+fib.get(7,5))



