# Super Class
class Animal:
	def __init__(self, name, color):
		self.name = name
		self.color = color

class Cat(Animal):
	def purr(self):
		print('Purr...')

class Dog(Animal):
	def bark(self):
		print('Woof!')

fido = Dog('Fido', 'brown')
print(fido.color)
fido.bark()


class Wolf:
	def __init__(self, name, color):
		self.name = name
		self.color = color
	def bark(self):
		print('Grr...')

class Dog(Wolf):
	def bark(self):
		print('Woof')

husky = Dog('Max', 'grey')
husky.bark()


class A:
	def method(self):
		print('A method')

class B(A):
	def another_method(self):
		print('B method')

class C(B):
	def third_method(self):
		print('C method')

c = C()
c.method()
c.another_method()
c.third_method()


class A:
	def a(self):
		print(1)

class B(A):
	def a(self):
		print(2)

class C(B):
	def c(self):
		print(3)

c = C()
c.a()


class A:
	def spam(self):
		print(1)

class B(A):
	def spam(self):
		print(2)
		super().spam()

B().spam()

