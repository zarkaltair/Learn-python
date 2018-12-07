# Множества set
num_set = {1, 2, 3, 4, 5}
word_set = set(['spam', 'eggs', 'sausage'])
print(3 in num_set)
print('spam' not in word_set)

letters = {'a', 'b', 'c', 'd'}
if 'e' not in letters:
	print(1)
else:
	print(2)

# методы для работы с множествами
nums = {1, 2, 1, 3, 4, 5, 6}
nums.add(-7)                # метод .add добавляет элемент во множество
if -2 in nums:
	nums.remove(3)          # метод .remove удаляет указанный элемент из множества
elif 5 not in nums:
	nums.add(-5)
elif 9 in nums:
	nums.remove(4)
else:
	nums.add(8)
nums.pop()                  # метод .pop удаляет случайный элемент из множества
print(nums)

# Операторы для работы с множествами
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}
print(first | second)       # оператор обединения, объединяет два множества
print(first & second)       # оператор пересечения, возвращает только те элементы которые есть в обоих множествах
print(first - second)       # оператор разности, возвращает элементы только из первого множества
print(second - first)       # оператор разности, возвращает элементы только из первого множества
print(first ^ second)       # оператор симметрической разности, возвращает все элементы обоих множеств кроме пересекающихся













