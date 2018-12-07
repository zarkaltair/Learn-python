class Hero():
	"""Class to Create Hero for our Game"""
	def __init__(self, name, level, race):
		"""Initiate our hero"""
		self.name   = name
		self.level  = level
		self.race   = race
		self.health = 100

	def show_hero(self):
		"""Print all parametrs of this Hero"""
		discription = ('Hero name is: ' + self.name          + ', '
			+ 'Level is: '              + str(self.level)    + ', '
			+ 'Race is: '               + self.race          + ', '
			+ 'Health is: '             + str(self.health)   + '; ').title()
		print(discription)

	def level_up(self):
		"""Upgrade level of Hero"""
		self.level += 1

	def move(self):
		"""Start moving Hero"""
		print('Hero ' + self.name + ' start moving...')

	def set_health(self, new_health):
		"""Health of Hero to change"""
		self.health = new_health

class SuperHero(Hero):
	"""Class to Create Super Hero"""
	def __init__(self, name, level, race, magiclevel):
		"""Initiate our Super Hero"""
		super().__init__(name, level, race)
		self.magiclevel = magiclevel
		self.magic = 100
	
	def make_magic(self):
		"""Use magic"""
		self.magic -= 10

	def show_hero(self):
		"""Print all parametrs of this Hero"""
		discription = ('Hero name is: ' +     self.name      + ', '
			+ 'Level is: '              + str(self.level)    + ', '
			+ 'Race is: '               +     self.race      + ', '
			+ 'Health is: '             + str(self.health)   + ', '
			+ 'Magic is: '              + str(self.magic)    + '; ').title()
		print(discription)

#----------------------Main--------------------

my_hero_1     = Hero     ('Zark',        15, 'Ork')
my_hero_2     = Hero     ('Altair',      21, 'Human')
my_super_hero = SuperHero('Zark_Altair', 25, 'Zombi', 20)

my_hero_1.show_hero()
my_hero_2.move()
my_hero_1.level_up()
my_hero_1.show_hero()
my_hero_2.set_health(60)
my_hero_2.show_hero()

my_super_hero.show_hero()
my_super_hero.make_magic()
my_super_hero.show_hero()


