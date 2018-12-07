def exc(text):
	assert text!=''
	print(str(text)+'!')
exc('Hi')

def  test(number):
	assert number>0, 'Number should be bigger than 0.'
	print(str(number))
test(10)

file=open('test.txt','r')
print(file.read())
file.close()

filename = input('Укажите файл?: ')
file = open(filename,'r')
print('В данном файле '+str(len(file.read()))+' символов')
file.close()

file = open('test.txt','w')
file.write('Hello world!')
file.close()

filename = input('Введите имя файла: ')
text = input('Введите текст: ')
file = open(filename,'w')
file.write(text)
file.close()

file = open('test.txt','a')
file.write(' It is.')
file.close()

file = open('somefile.txt','r')
for i in range(21):
	print(file.read(8))
file.close()





