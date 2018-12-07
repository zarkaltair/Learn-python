# Функциональное программирование
# Пример из урока №1 Функции высшего порядка (функции принимают другие функции в качестве аргументов, либо возвращают их как результат)
def apply_twice(func, arg):
	return func(func(arg))
def add_five(x):
	return x + 5
print(apply_twice(add_five, 10))
# Задача из урока №1
def test(func, arg):
	return func(func(arg))
def mult(x):
	return x * x
print(test(mult, 2))
# Пример из урока №2 (чистая функция возвращает значения только от своих аргументов)
def pure_function(x, y):
	temp = x + 2 * y
	return temp / (2 * x + y)
# функция impure не является чистой так как она изменила свое состояние some_list
some_list = []
def impure(arg):
	some_list.append(arg)
# Задача из урока №2
def func(x):
	y = x ** 2
	z = x + y
	return z

















