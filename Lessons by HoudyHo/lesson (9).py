number = 0
while number <= 10:
	number +=1
	if (number % 2) != 0:
		continue;
	print('Четное число ' + str(number))