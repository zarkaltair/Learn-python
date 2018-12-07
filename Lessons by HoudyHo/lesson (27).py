# Генератор (тип данных как списки и кортежи), функция yield определяет генератор
# Example №1
def countdown():
	i = 5
	while i > 0:
		yield i
		i -= 1
for i in countdown():
	print(i, end = ', ')
# Example №2 infinite loop!!!
#def infinite_sevens():
#	while True:
#		yield 7
#for i in infinite_sevens():
#	print(i)
# Example №3
def numbers(x):
	for i in range(x):
		if i % 2 == 0:
			yield i
print(list(numbers(11)))
# Task #1
def make_word():
	word = ''
	for ch in 'spam':
		word += ch
		yield word
print(list(make_word()))





