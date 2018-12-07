test = ['a', 'b', 'c', ['d', 'e', 'f']]
print(test[3][2])
test = [1,2,3]
print(test+[4,5,6])

test = ['Alex Mercer', 'Tony Stark', 'Lenny Flawes']
if 'Alex Mercer' in test:
	print('Alex Mercer is in list')

test = [1,2,3,8,9]
if 4 in test:
	print('4')
if 3 in test:
	print('3 is in list')
if 4 not in test:
	print('4 is not in list')

test = []
test.append('Hello')
test.append(3)
test.append([1,2,3])
print(test)

test=[5,3,2,5,6,7]
test.append('5')
print('В массиве test у нас находится '+str(len(test))+' элементов')
test.remove('5')
print('В массиве test у нас находится '+str(len(test))+' элементов')

test=[1,2,3]
test.insert(0,4)
print(test)

test=[1,2,3]
print(max(test))

test=[1,2,3]
print(min(test))

test=[1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]
print(test.count(4))

test=[1,2,3,4,5]
test.reverse()
print(test)