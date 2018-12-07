# Функция lambda  = анонимная функция
# Пример из урока №1
def my_func(f, arg):
	return f(arg)
my_func(lambda x: 2 * x * x, 5)
# Пример из урока №2
# named functuon именная функция
def polynomial(x):
	return x ** 2 + 5 * x + 4
print(polynomial(-4))
# lambda анонимная функция
print((lambda x: x ** 2 + 5 * x + 4)(-4))
# Задача из урока №2
a = (lambda x: x * x)(8)
print(a)
# Пример из урока №3
double = lambda x: x * 2
print(double(7))
# Задача из урока №3
triple = lambda x: x * 3
add = lambda x, y: x + y
print(add(triple(3), 4))

