test='Howdy Ho'
# Здесь мы выводим переменную на экран при помощи функции print
print(test)

def Howdy_ho(name):
	'''Описание функции'''
	print('Howdy_ho'+name+'!')
def read_name():
	return ':::'+input('Enter your name: ')+':::'
Howdy_ho(read_name())

def shout(word):
	return word+'!'
speak=shout
output=speak('shout')
print(output)