# Декораторы - декорирование функции без ее изменения
def decor(func):
	def wrap():
		print('============')
		func()
		print('============')
	return wrap
def print_text():
	print('Hello world!')
decorated = decor(print_text)
decorated()
# @decor декорирование функции компактный вариант
def decor(func):
	def wrap():
		print('============')
		func()
		print('============')
	return wrap
@decor
def print_text():
	print('Hello world!')
print_text()















