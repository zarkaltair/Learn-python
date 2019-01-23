a = [1, 2, 2, 4, 8]
print(len(a[:3]) % 3) # len считает количество элементов в списке
# print 0

for i in range(0, 2): # результат два элемента
	for i in range(0, 4): # для каждого элемента из предыдущего кода i равно 0,1,2,3
		print(list(str(i)))
# print 0 1 2 3 0 1 2 3

n = [1, 2, 3, 4]
print(list(filter(lambda x: x > 2, n))) # результат все значения из списка где х > 2
# print [3,4]

arr = [7, [[[[2]]], [[[0]], [3]], [4, 5, [6, 7]]], 8] # как преобразовать этот список в последовательный список?

print(arr)

a0 = arr[0]
a1 = arr[1][0][0][0][0]
a2 = arr[1][1][0][0][0]
a3 = arr[1][1][1][0]
a4 = arr[1][2][0]
a5 = arr[1][2][1]
a6 = arr[1][2][2][0]
a7 = arr[1][2][2][1]
a8 = arr[2]

print(a0)
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print(a6)
print(a7)
print(a8)

arr = [1, [1, 2]]

def listmerge1(lstlst):
    all=[]
    for lst in lstlst:
        for el in lst:
            all.append(el)
    return all


x = (0, 1, 2)
[a, b, c] = x
print(a + b + c)
# print 3

count = 0
for i in range(5):
	for j in range(i):
		count += 1
print(count)
# print 10

my = [i for i in range(0, 10, 2)]
print(my[1])
# print 2

for x in range(3, 18):
	if x % 2 != 0:
		print(x)
# print 3 5 7 9 11 13 15 17

t1 = (1, 2, 3)
t2 = ('a', 'b', 'c')
print(tuple(zip(t1, t2))[1][0])

a, b, *c = [1, 3, 5, 7]
print(c)

str = 'CaSe FoLd'
print(str.casefold())

y = [x for x in range(10) if x//3 == 2]
print(sum(y))
# print 21

i = 0
while i < 5:
	i += 1
	if i == 3:
		break
	else:
		print(0)
# print 0

a = {'b': 'c', 'c': 'd', 'd': 'b'}
b = a[a['b']]
print(a[b])
# print b

def f(x):
	return g(x) + 3 % 2
def g(x):
	return x ** 2 + 2
print(f(g(1)))
# print 12

a = [0, 1, 0]
b = [1, 1, 0]
s = 0
for x in (a, b, a):
	s += x.count(1)
print(s)
# print 4

a = {j for x in range(10) for j in range(x)};
print(len(a));
# print 9

x = 3
y = 1
while x > 0:
	y += x
	x -= 2
print(y)
# print 5

x = 10
y = 30
print([i for i in range(x, y, 3) if i % 2 == 1][2])
# print 25

a = enumerate(range(10))
b = enumerate(range(1, 10))
c = list(zip(a, b))
print(c[-1])
# print ((8, 8), (8, 9))

for i in range(1, 5):
	print(i % 3)
# print 1 2 0 1

p, p, p = 1, 2, 3
print(p)
# print 3

a = 'solo'
print(a.zfill(6))
# print 00solo

nums = set([1, 1, 2, 3, 3, 4]) # в множестве len считает только разные числа
print(len(nums))
# print 4

backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove('dagger')
print(len(backpack))
# print 3

a, b = [1, 2], [1, 2]
if id(a) == id(b):
	print('y')
else:
	print('n')
# print n

chars = ['a', 'b', 'c', 'd', 'e']
i = chars.index('c')
chars = chars[i:] + chars[:i] # c = i служит как точка отсчета для дальнейших действий
print(chars[4])
# print b

def f(x = []):
	x += [3]
	return sum(x)
print(f() + f() + f())
# print 18

list1 = [1, 2]
list2 = list1
list3 = list2[:]
a = list2 is list1
b = list3 is list1
print(a, b)
# print True False

a = [1, 2, ':', 3]
del a[:]
print(a)
# print []

my_list = [i for i in range(10) if i % 2 == 0]
print(my_list[3])
# print 6

a = [0, 1, 2]
b = [0, 1, 2]
print(a is b)
print(a == b)

a = [4, 5, 6, 7]
print(a[True]) # True в данном случает работает как 1
# print 5

print(int(not(7 < 7.0)) * 7 - 6 % 3)
# print 7

print(0b111101) # запись в двоичной системе исчисления
print(0o0732) # запись в восьмеричной системе исчисления
print(0xfa0b) # запись в шестнадцатеричной системе исчисления
print(int('z3f', base = 36)) # запись в тридцатишестиричной системе исчисления
x = 127
print(bin(x)) # перевод из десятеричной системы в двоичную
print(oct(x)) # перевод из десятеричной системы в восьмеричную
print(hex(x)) # перевод из десятеричной системы в шестнадцатиричную
# перевоод в любую систему исчисления, указать в base
base = 7
x = int(input())
while x > 0:
	digits = x % base
	print(digits, end = '') # число выводит задом наперед!!!
	x //= base