# Function Map and filter
# Пример №1 функция map применяет другую функцию к списку
def add_five(x):
	return x + 5
nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)
# можно записать через ононимную функцию lambda
nums = [11, 22, 33, 44, 55]
result = list(map(lambda x: x + 5, nums))
print(result)
# Пример №2 функция filter удаляте элементы списка не подходящие под условие функции
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)

















