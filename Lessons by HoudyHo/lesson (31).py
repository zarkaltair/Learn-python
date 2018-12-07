# Модуль itertools стандартная библиотека, один тип функций в этой библиотеке это бесконечные итераторы
from itertools import count                         # count выводит все элементы в соответствии с заданными параметрами
for i in count(3):
	print(i)
	if i >= 11:
		break

from itertools import accumulate, takewhile
nums = list(accumulate(range(8)))                   # accumulate выводит последовательную сумму всех элемнтов
print(nums)
print(list(takewhile(lambda x: x <= 6, nums)))      # takewhile выводит (циклически) значения

from itertools import takewhile
nums = [2, 4, 6, 7, 9, 8]
a = takewhile(lambda x: x % 2 == 0, nums)           # print[2, 4, 6] цифра 8 не входит в заданный диапазон, потому что цикл прерывается на цифре 7 (цикл выдает False и прерывается)
print(list(a))

from itertools import product, permutations
letters = ('A', 'B')
print(list(product(letters, range(2))))             # product комбинирует све заданные значния в соответствии с заданными условиями
print(list(permutations(letters)))                  # permutations комбинирует все заданные значения между собой

from itertools import product
a = {1, 2}
print(len(list(product(range(3), a))))









