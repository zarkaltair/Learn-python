#
class Pizza:
	def __init__(self, toppings):
		self.toppings = toppings

	@property
	def pineapple_allowed(self):
		return False
	
pizza = Pizza(['cheese', 'tomato'])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True

class Person:
	def __init__(self, age):
		self.age = int(age)

	@property
	def isAdult(self):
		if self.age > 18:
			return True
		else:
			return False
	
# Функция setter устанавливает значение соответствующего свойства
# Функция getter возвращает значение соответствующего свойства
class Pizza:
	def __init__(self, toppings):
		self.toppings = toppings
		self._pineapple_allowed = False

	@property
	def pineapple_allowed(self):
		return self._pineapple_allowed
	
	@pineapple_allowed.setter
	def pine_allowed(self, value):
		if value:
			password = input('Enter the password: ')
			if password == 'Sw0rdf1h!':
				self._pineapple_allowed = value
			else:
				raise ValueError('Alert! Intruder')

pizza = Pizza(['cheese', 'tomato'])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)





