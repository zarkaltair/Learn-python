try:
	print(7/0)
except ZeroDivisionError: #если не указывать вид исключения будут ловиться все виды исключений
	print('Зафиксировано деление на ноль') #также можно пропустить командой pass
finally:
	print('Конец проверки.')
print('Программы завершена!')

try:
	pogoda='Bed'
	if pogoda=='Bed':
		raise TypeError
except TypeError:
	print('Поймано исключение TypeError')

pogoda='Bed'
if pogoda=='Bed':
	raise TypeError('Тестовая ошибка')

try:
	print(7/0)
except:
	raise
	print('Тест')

class HowdyHoError(Exception):
	pass
raise HowdyHoError('TEST')