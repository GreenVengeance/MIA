from random import randint

class Spieler:

	'''Konstruktor'''
	def __init__(self, name):
		self.name: str = name
		self.punkte: int = 2
		self.result: int = 0
		self.call: int = 0

	def schuetteln(self):
		random_zahl_1 = randint(1, 6)
		random_zahl_2 = randint(1, 6)
		if random_zahl_1 > random_zahl_2:
			self.result = (random_zahl_1 * 10) + random_zahl_2
		elif random_zahl_1 == random_zahl_2:
			self.result = (random_zahl_2 * 10) + random_zahl_1
		else:
			self.result = (random_zahl_2 * 10) + random_zahl_1

	def reset_values(self):
		self.result = 0
		self.call = 0
