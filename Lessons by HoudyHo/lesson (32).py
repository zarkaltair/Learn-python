# Class
class Cat:
	def __init__(self, color, legs):
		self.color = color
		self.legs = legs
felix = Cat('ginger', 4)
print(felix.color)
rover = Cat('dog-colored', 4)
stumpy = Cat('brown', 3)

class Student:
	def __init__(self, name):
		self.name = name
test = Student('Bob')
print(test.name)

class Dog:
	def __init__(self, name, color):
		self.name = name
		self.color = color
	def bark(self):
		print('Woof!')
fido = Dog('Fido', 'brown')
print(fido.name)
fido.bark()

class Dog:
	legs = 4
	def __init__(self, name, color):
		self.name = name
		self.color = color
fido = Dog('fido', 'brown')
print(fido.legs)
print(Dog.legs)

class Student:
	def __init__(self, name):
		self.name = name
	def sayHi(self):
		print('Hi from ' + self.name)
s1 = Student('Amy')
s1.sayHi()

class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height
rect = Rectangle(7, 8)
print(rect.color)


