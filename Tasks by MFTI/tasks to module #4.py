try:
	print(1)
	print(20/0)
	print(2)
except ZeroDivisionError:
	print(3)
finally:
	print(4)

try:
	with open('test.txt') as f:
		print(f.read())
except:
	print('Error')

try:
	print(1)
	assert 2 + 2 == 5
except AssertionError:
	print(3)
except:
	print(4)


